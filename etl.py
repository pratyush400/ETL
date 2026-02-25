import csv

def read_data():
    Tree = []
    Bird = []
    with open('junction.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            Bird.append(row[0])
            Tree.append(row[1])
        

read_data()