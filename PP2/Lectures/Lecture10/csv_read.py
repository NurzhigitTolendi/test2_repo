import csv

filename = "C:\\Users\\chris\\OneDrive\\Документы\\Demo\\PP2\\Lectures\\Lecture10\\students.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row) # ['Ruslan', '24B202424', '1', '+77007007070']
                     # ['Mariya', '24B202425', '1', '+77077077070']
        name, id, study_year, phone_number = row
        print(name, id, study_year, phone_number) # Ruslan 24B202424 1 +77007007070
                                                    # Mariya 24B202425 1 +77077077070