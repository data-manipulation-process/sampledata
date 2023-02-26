import csv

# opening the CSV file
# with open('Giants.csv', mode='r') as file:
#     # reading the CSV file
#     csvFile = csv.reader(file)
#
#     # displaying the contents of the CSV file
#     for lines in csvFile:
#         print(lines)

# Python program to demonstrate
# writing to CSV


import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open(filename, 'r') as f:
    for i, lines in enumerate(f):
        i += 1
        print(i, lines, end='')
