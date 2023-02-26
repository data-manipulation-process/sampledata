# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records.csv"

with open('samplefile.txt', 'w') as f:
    f.write(mydict)
    f.close()

with open('samplefile.txt', 'r') as f:
    for i, name in enumerate(f):
        print(i, name.strip())

with open(filename, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mydict)

with open(filename, 'r') as csv_files:
    for i, name in enumerate(csv_files):
        print(i, name, end='')
