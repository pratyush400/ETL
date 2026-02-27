import csv
import os
class ETL:
    def __init__(self):
        self.reader = []
        self.treeID = []
        self.birdID = []

    def read_data(self):
        i = 1
        with open('tree.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                self.treeID.append(row[2])

        with open('junction.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in enumerate(reader):
                self.birdID.append(i)
                i = i + 1
        
        # print(self.birdID)
        print(self.treeID)


    def read_data_NestsIn():
        Tree_NestsIn = []
        Bird_NestsIn = []
        Year_NestsIn = []
        Query_NestsIn = []
        with open('junction.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                Bird_NestsIn.append(row[0])
                Tree_NestsIn.append(row[1])
                Year_NestsIn.append(row[2])
        # print(Year)



            for i in range(len(Tree_NestsIn)):
                temp = f'''INSERT INTO NestsIn (TreeID, BirdID, NestYear ){os.linesep}VALUES ({Tree_NestsIn[i]},{Bird_NestsIn[i]},{Year_NestsIn[i]}){os.linesep}{os.linesep}'''
                Query_NestsIn.append(temp)

            for i in range(len(Tree_NestsIn)):
                print(Query_NestsIn[i])

if __name__ == '__main__':
    run = ETL()
    run.read_data()


