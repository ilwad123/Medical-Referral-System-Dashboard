import unittest
import csv
import os

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

class test_process(unittest.TestCase):
    
    def test_process_1(self):
        #test for new patients added and algorithm for those needing refferal 
        #expected number of refferal shown on the web app compared to the csv file 
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        table_data= process_csv_data(absolute_path)
        referrals_count = sum(1 for row in table_data if row[17] == "Need referral")
        # Check if the count matches the expected value
        self.assertEqual(referrals_count,795)
     
    def test_process_2(self):
        #test for new patients added and algorithm for those not needing refferal 
        #expected number of no refferal shown on the web app compared to the algorithmcsv file 
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        table_data= process_csv_data(absolute_path)
        num_of_refferal = sum(1 for row in table_data if row[17] == "Not Referred")
        self.assertEqual(num_of_refferal,4591)
    
    def test_process_3(self):
        #test for new patients added and algorithm for those  needing refferal 
        #expected number of no refferal shown on the web app compared to the initial given csv file 
        #feeding dashboard csv 
        new_one = os.path.dirname(os.path.abspath(__file__))
        table_data= not_process_csv_data(new_one)
        num_of_refferal = sum(1 for row in table_data if row[17] == "Need referral")
        self.assertEqual(num_of_refferal,1600)
        
    def test_process_4(self):
        #test for new patients added and algorithm for those not needing refferal 
        #expected number of no refferal shown on the web app compared to the initial given csv file 
        #feeding dashboard csv 
        new_one = os.path.dirname(os.path.abspath(__file__))
        table_data= not_process_csv_data(new_one)
        num_of_refferal = sum(1 for row in table_data if row[17] == "Not Referred")
        self.assertEqual(num_of_refferal,3786)
        
    def test_process_5(self):
        new_one = os.path.dirname(os.path.abspath(__file__))
        table_data= not_process_csv_data(new_one)
        if table_data[0][17] == "Not Referred":
            self.assertEqual(table_data[0][17],0)
        else:
            self.assertEqual(table_data[0][17],1)

if __name__ == '__main__':
    unittest.main()
    
