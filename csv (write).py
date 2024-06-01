python
import csv

file_path = input("Enter the file path to save the CSV file (e.g., C:\\Users\\YourUsername\\Desktop\\BookRecord.csv): ")
file = open(file_path, 'w', newline='')

header = input("Enter the header for the CSV file (separated by commas): ")
header_list = header.split(',')

data = []
while True:
    name = input("Enter Name: ")
    if not name:
        break
    age = input("Enter Age: ")
    section = input("Enter Section: ")
    data.append([name, age, section])

csv_writer = csv.writer(file)
csv_writer.writerow(header_list)
for item in data:
    csv_writer.writerow(item)

file.close()

