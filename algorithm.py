import tensorflow as tf
from tensorflow.keras import layers, models
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# STEP 1 -  Load data using pandas
data = pd.read_csv('your_dataset.csv')

# 1.1 Handle Missing Values:
#Check for missing values and decide how to handle them. 
#You might choose to remove rows with missing values or impute them with mean, median, or other strategies.

#### i suspect that we would need to keep empty values?? - Ana 

# Drop rows with missing values
data = data.dropna()
# Impute missing values
data.fillna(data.mean(), inplace=True)

#1.2 Feature Scaling/Normalization: 
#It's common to scale or normalize your features to a similar range, 
#which can help improve the convergence of your neural network.

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

#Encode Categorical Variables (if any):
# If your dataset contains categorical variables, 
# you might need to encode them into numerical values.

####i'm not sure this applies to us. - Ana 

label_encoder = LabelEncoder()
data['categorical_column'] = label_encoder.fit_transform(data['categorical_column'])

#Split Data into Features and Labels: Separate your dataset into input features (X) and target labels (y).
X = data.drop(columns=['target_column'])
y = data['target_column']

#Split Data into Training and Testing Sets: Split your dataset into training and testing sets to evaluate your model's performance.

###Please edit the variables names - Ana 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

##STEP 2 - Build the Neural Network

#2.1 Define Model Architecture:
# Choose the architecture of your neural network. 
# A basic feedforward neural network is often used for simple tasks. 
# For more complex tasks, consider using convolutional layers (for image data) or recurrent layers (for sequential data).
model = models.Sequential()

#2.2 Add Layers:Add layers to your model. 
# The first layer should specify the input shape, and subsequent layers can be added using the add method.

model.add(layers.Dense(128, activation='relu', input_shape=(input_size,)))

#Here, Dense represents a fully connected layer with 128 neurons. 
# Adjust the number of neurons based on the complexity of your task. 
# The activation function 'relu' introduces non-linearity.

model.add(layers.Dense(64, activation='relu'))

#Add more layers as needed. The number of neurons and layers depend on your specific problem.
model.add(layers.Dense(output_size, activation='softmax'))

#The final layer's activation function depends on the task:
# For binary classification, use 'sigmoid'.
#For multi-class classification, use 'softmax'.
# For regression tasks, use appropriate activation functions like 'linear'.

#2.3 Model summary: View a summary of your model, including the number of parameters.
model.summary()

##STEP 3 - Compile the Model
#Specify the loss function, optimizer, and evaluation metric.
#ask CHATGPT to expand on how to do this so we can make sure that we are doing 
#everything we need.

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Adjust based on your task
              metrics=['accuracy'])

#STEP 4 - Train the model 
# Train the model on your training data. - also ask chatgpt to expand on this 
#there are more steps to follow 

model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

#STEP 5 - Evaluate the model:
#ask chatgpt to expand it 

test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_acc}')

#STEP 6 - Make predictions
#ask chatgpt to expand it. 

predictions = model.predict(new_data)