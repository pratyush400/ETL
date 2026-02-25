import csv

def read_data():
        with open('junction.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) # Skip header