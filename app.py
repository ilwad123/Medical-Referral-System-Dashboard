from flask import Flask, request, session, render_template, url_for, jsonify, redirect
from flask_paginate import Pagination, get_page_parameter
import csv
import os
from distutils.log import debug 
from fileinput import filename 
from flask import *  

app = Flask(__name__)
app.secret_key = 'This is my Secret Key'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/upload')
def upload():
    return render_template('upload.html') 

@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)   
        return render_template("sucess.html", name = f.filename)   
  

@app.route('/viewpatient',methods=['GET','POST'])
def viewpatient():
    referral_filter = request.form.get('referralFilter')
    searchQuery=request.form.get('searchQuery')
    datarows = []
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(absolute_path, "Feeding Dashboard data.csv"), 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header
        for line in reader:
            data = [item.strip() if item.strip() != "" else "None" for item in line]
            ref = data[17]
            encounterid=data[0]
            
            if ref == "0":
                data[17] = "Not Referred"
            else:  
                data[17] = "Referred"
            
            datarows.append(data)
    if request.method == 'POST':
            datarows = [row for row in datarows if referral_filter == 'All' or referral_filter == row[17]]
            # datarows = [row for row in datarows if searchQuery ==row[0]
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # Adjust per_page value as needed
    offset = (page - 1) * per_page
    paginated_data = datarows[offset: offset + per_page]
    
    pagination = Pagination(page=page, total=len(datarows), per_page=per_page, css_framework='bootstrap4')

    return render_template('patient.html', datarows=paginated_data, pagination=pagination)



@app.route('/search',methods=['GET','POST'])
def search():
    searchQuery=request.form.get('searchQuery')
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
            datarows = [row for row in datarows if searchQuery == row[0]]
   
    return render_template('patient.html', datarows=datarows)




if __name__ == '__main__':
    app.run(debug=True)
