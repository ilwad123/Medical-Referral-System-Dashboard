import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os 
import csv 

# Load the data from CSV
data = pd.read_csv('Feeding Dashboard data.csv')

# Fill missing values with 0
data.fillna(0, inplace=True)

# Extract relevant features and target variable
X = data[['feed_vol', 'oxygen_flow_rate', 'resp_rate', 'bmi']].values
y = data['referral'].values  # Assuming 'referral' is the column indicating whether a patient should be referred

# Perform feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Predict referral status for all patients
predictions = model.predict(X_scaled)

# Add predicted referral status to the dataframe
data['predicted_referral'] = predictions.round().astype(int)

# Display patients that should be referred
patients_to_refer = data[data['predicted_referral'] == 1]
print("Patients to refer:")
print(patients_to_refer)

# Write the dataframe to a new CSV file
data.to_csv('Algorithm.csv', index=False)