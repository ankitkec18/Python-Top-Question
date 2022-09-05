# Python program to demonstrate
# writing to CSV
  
  
import csv 
    
# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
# data rows of csv file 
rows = [ ['Ankit', 'CSE', '3', '9.0'], 
         ['Ritik', 'CSE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'CE', '1', '9.5'], 
         ['Prateek', 'ME', '3', '7.8'], 
         ['Sahil', 'EEE', '2', '9.1']] 
    
# name of csv file 
filename = "university_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)