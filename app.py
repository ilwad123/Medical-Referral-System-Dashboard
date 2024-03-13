from flask import Flask, request, session, render_template, jsonify, redirect
from flask_paginate import Pagination, get_page_parameter
import csv
import os
from enum import Enum
from flask import make_response


app = Flask(__name__)
app.secret_key = 'This is my Secret Key'

@app.route('/')
def index2():
    return render_template('index2.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Reports')
def Reports():
    return render_template('Reports.html') 

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['file']

        # Save the uploaded file
        uploaded_file.save(uploaded_file.filename)

        # Get the absolute path of the current script
        absolute_path = os.path.dirname(os.path.abspath(__file__))

        # Path to the Feeding Dashboard CSV file
        csv_file_path = os.path.join(absolute_path, "Feeding Dashboard data.csv")

        # Read the uploaded file and append its information to the Feeding Dashboard CSV file
        with open(csv_file_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # Assuming the uploaded file is a CSV with a header
            reader = csv.reader(uploaded_file)
            for row in reader:
                writer.writerow(row)
    return render_template("sucess.html", name=uploaded_file.filename)

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
                data[17] = "Need refferal"
            datarows.append(data)        
            
    if request.method == 'POST':
        if search_query:
            datarows = [row for row in datarows if search_query == row[0]]
        elif referral_filter:
            datarows = [row for row in datarows if referral_filter == 'All' or referral_filter == row[17]]
            
            
    per_page=10
    page = request.args.get('page', 1, type=int)
    pagination = Pagination(page=page, total=len(datarows), per_page=per_page)
    first_page = (page - 1) * per_page 
    last_page = first_page + per_page
    paginated_data = datarows[first_page:last_page]  # start from first page and should end with the last page

    return render_template('patient.html', datarows=paginated_data, pagination=pagination,referral_filter=referral_filter)

@app.route('/patientdetails', methods=['POST'])
def patientdetails():
    encounter_id = request.form.get('encounterId')  
    patient_data = None

    with open("NHS-App/Feeding Dashboard data.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['encounterId'] == encounter_id:
                patient_data = row
                break

    if patient_data:
        return render_template('patient_details.html', patient_data=patient_data)
    else:
        return "Patient details not found"


class ReferralStatus(Enum):
    NOT_REFERRED = '0'
    REFERRED = '1'

class PatientReferral:
    def __init__(self, encounterId, end_tidal_co2, feed_vol, feed_vol_adm, fio2, fio2_ratio, insp_time,
                 oxygen_flow_rate, peep, pip, resp_rate, sip, tidal_vol, tidal_vol_actual, tidal_vol_kg,
                 tidal_vol_spon, bmi, referral):
        self.encounterId = encounterId
        self.end_tidal_co2 = end_tidal_co2
        self.feed_vol = feed_vol
        self.feed_vol_adm = feed_vol_adm
        self.fio2 = fio2
        self.fio2_ratio = fio2_ratio
        self.insp_time = insp_time
        self.oxygen_flow_rate = oxygen_flow_rate
        self.peep = peep
        self.pip = pip
        self.resp_rate = resp_rate
        self.sip = sip
        self.tidal_vol = tidal_vol
        self.tidal_vol_actual = tidal_vol_actual
        self.tidal_vol_kg = tidal_vol_kg
        self.tidal_vol_spon = tidal_vol_spon
        self.bmi = bmi
        self.referral = ReferralStatus(referral).name

def load_data_from_csv(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(PatientReferral(**row))
    return data

# Assuming your CSV file is named 'patient_data.csv'
data = load_data_from_csv('./NHS-App/Feeding Dashboard data.csv')

@app.route('/api/patients', methods=['GET'])
def get_patient_referrals():
    json_data = [{'encounterId': patient.encounterId,
                  'end_tidal_co2': patient.end_tidal_co2,
                  'feed_vol': patient.feed_vol,
                  'feed_vol_adm': patient.feed_vol_adm,
                  'fio2': patient.fio2,
                  'fio2_ratio': patient.fio2_ratio,
                  'insp_time': patient.insp_time,
                  'oxygen_flow_rate': patient.oxygen_flow_rate,
                  'peep': patient.peep,
                  'pip': patient.pip,
                  'resp_rate': patient.resp_rate,
                  'sip': patient.sip,
                  'tidal_vol': patient.tidal_vol,
                  'tidal_vol_actual': patient.tidal_vol_actual,
                  'tidal_vol_kg': patient.tidal_vol_kg,
                  'tidal_vol_spon': patient.tidal_vol_spon,
                  'bmi': patient.bmi,
                  'referral': patient.referral}  # Get the enum value
                 for patient in data]

    response = make_response(jsonify({'patients': json_data}))
    response.headers['Access-Control-Allow-Origin'] = '*' 
    return response




if __name__ == '__main__':
    app.run(debug=True)

