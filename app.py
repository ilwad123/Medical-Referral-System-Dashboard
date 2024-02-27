from flask import Flask, request, session, render_template, url_for, jsonify, redirect
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
  

@app.route('/viewpatient',methods=['GET','POST'])
def viewpatient():
    referral_filter = request.form.get('referralFilter')
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
        datarows = [row for row in datarows if referral_filter == 'All' or referral_filter == row[17]]
    return render_template('patient.html', datarows=datarows)






if __name__ == '__main__':
    app.run(debug=True)
