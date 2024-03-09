from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)
app.secret_key = 'This is my Secret Key'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/upload')
def upload():
    return render_template('upload.html') 

@app.route('/viewpatient', methods=['GET', 'POST'])
def viewpatient():
    referral_filter = request.form.get('referralFilter')
    search_query = request.form.get('searchQuery')
    datarows = []
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(absolute_path, "Feeding Dashboard data.csv"), 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        for line in reader:
            data = [item.strip() if item.strip() != "" else "None" for item in line]
            ref = data[17]
            
            if ref == "0":
                data[17] = "Not Referred"
            else:  
                data[17] = "Referred"
            
            datarows.append(data)
    if request.method == 'POST':
        if search_query:
            datarows = [row for row in datarows if search_query in row[0]]
        else:
            datarows = [row for row in datarows if referral_filter == 'All' or referral_filter == row[17]]

    return render_template('patient.html', datarows=datarows)

@app.route('/search', methods=['POST'])
def search():
    return viewpatient()

@app.route('/patientdetails', methods=['POST'])
def patientdetails():
    encounter_id = request.form.get('encounterId')  
    patient_data = None

    with open("Feeding Dashboard data.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['encounterId'] == encounter_id:
                patient_data = row
                break

    if patient_data:
        return render_template('patient_details.html', patient_data=patient_data)
    else:
        return "Patient details not found"

if __name__ == '__main__':
    app.run(debug=True)
