# Medical Referral System Dashboard (Group Project)

A referral web app used by medical professionals to refer patients to dieticians based on their physiological measurements.

**Features include:**  
- Multi-paged, scrollable, and searchable tables to view overall patient data  
- Analytics displaying patient information as charts  
- File upload functionality to add and update patient data required by the machine learning algorithm for patient referrals  
- Machine learning algorithm to refer patients automatically  
- Help page  

---

### Own Contributions

- Used **HTML, CSS, and JavaScript** for frontend development, and **Python with Flask** for backend development and testing  
- Collaborated on the medical referral dashboard system, responsible for:  
  - Designing and coding the patient data table with filters, real-time search, and machine learning output columns (referred and non-referred patients)  
  - Implementing file validation for CSV uploads to ensure data accuracy and protection against threats like SQL injection  
  - Conducting automated testing to verify data display and website functionality (`testingref.py`)  
  - Creating the structure of the main application file (`app.py`)  
  - Assisting with other sections of the web app  

---

### Screenshots of Application

#### Patient Page  
**Multi-paged, scrollable, filterable, and searchable tables to view overall patient data**  
![Patient Page Screenshot](/patient_part1.png)
![Patient Page Screenshot](/patient_part2.png)

---
### Installation

1. Ensure you have Python 3 installed on your system.

2. Navigate to the project directory:
   ```
   cd nhs-app
   ```
3. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask application using the following command:
   ```
   python3 app.py
   ```
2. Once the application is running, you can access it through your web browser at `http://localhost:5000`.

### Dependencies

- Flask
- Other packages as specified in `requirements.txt`


