import unittest
import csv
import os
from app import app
import pandas as pd
def not_process_csv_data(new_one):
    #data given initially csv 
    datarows=[]
    new_one = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(new_one, "Feeding Dashboard data.csv"), 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            data = [item.strip() if item.strip() != "" else "None" for item in line]
            ref = data[17]
            if ref == "1": 
                data[17] = "Need referral"
            else:
                data[17]="Not Referred"
                
            datarows.append(data)
    return datarows

def process_csv_data(absolute_path):
    #algorithm data csv
    datarows=[]
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(absolute_path, "Algorithm.csv"), 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
                data = [item.strip() if item.strip() != "" else "None" for item in line]
                ref = data[17]
                recom = data[18]
                if ref == "1" and recom == "1": 
                    data[17] = "Need referral"
                    data[18] = "Recommended"
                else:
                    data[17] = "Not Referred"
                    data[18] = "Not Recommended"
                datarows.append(data)
        return datarows
    

class check_number_patients(unittest.TestCase):
    #verify the correctness of patient referral counts based on the data processed from CSV files.
    def test_process_1(self):
        #test for new patients added and algorithm for those needing refferal 
        #expected number of refferal shown on the web app compared to the csv file 
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        table_data= process_csv_data(absolute_path)
        referrals_count = sum(1 for row in table_data if row[17] == "Need referral")
        # Check if the count matches the expected value
        self.assertEqual(referrals_count,864)
         #ADD SCREENSHOT FROM SITE TO SHOW THATS THE TOTAL 

    def test_process_2(self):
        #test for new patients added and algorithm for those not needing refferal 
        #expected number of no refferal shown on the web app compared to the algorithmcsv file 
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        table_data= process_csv_data(absolute_path)
        num_of_refferal = sum(1 for row in table_data if row[17] == "Not Referred")
        self.assertEqual(num_of_refferal,4522)
        #ADD SCREENSHOT FROM SITE TO SHOW THATS THE TOTAL 
    def test_process_3(self):
        #test for new patients added and algorithm for those  needing refferal 
        #expected number of no refferal shown on the web app compared to the initial given csv file 
        #feeding dashboard csv 
        new_one = os.path.dirname(os.path.abspath(__file__))
        table_data= not_process_csv_data(new_one)
        num_of_refferal = sum(1 for row in table_data if row[17] == "Need referral")
        self.assertEqual(num_of_refferal,1600)
        #ADD SCREENSHOT FROM SITE TO SHOW THATS THE TOTAL 
 
    def test_process_4(self):
        #test for new patients added and algorithm for those not needing refferal 
        #expected number of no refferal shown on the web app compared to the initial given csv file 
        #feeding dashboard csv 
        new_one = os.path.dirname(os.path.abspath(__file__))
        table_data= not_process_csv_data(new_one)
        num_of_refferal = sum(1 for row in table_data if row[17] == "Not Referred")
        self.assertEqual(num_of_refferal,3786)
        #ADD SCREENSHOT FROM SITE TO SHOW THATS THE TOTAL 

        #would be used if using flask dk???
        #response_text = response.data.decode('utf-8')
        #referrals_count = response_text.count("Not Reffered")
        
class TestFilterFunction(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    #tests the viewpatientroute function works 
    def test_filter_all(self):
        response = self.app.post('/viewpatient', data={'referralFilter': 'All'})
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_filter_need_referral(self):
        # Simulate HTTP GET request to viewpatient route with filter option set to "Need referral"
        response = self.app.post('/viewpatient', data={'referralFilter': 'Need referral'})
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        #list out records that need refferal
        # data = pd.read_csv('Algorithm.csv')
        # data.fillna("None", inplace=True)   
        # need_refferal = data[data['Need referral'] == '1']
        # print(need_refferal)

    def test_filter_not_referred(self):
        # Simulate HTTP GET request to viewpatient route with filter option set to "Not Referred"
        response = self.app.post('/viewpatient', data={'referralFilter': 'Not Referred'})
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        #list out records not refferal 
        # data = pd.read_csv('Algorithm.csv')
        # data.fillna("None", inplace=True)   
        # not_referred_records = data[data['Not Referred'] == '0']
        # print(not_referred_records)
           
          
if __name__ == '__main__':
    unittest.main()
    
