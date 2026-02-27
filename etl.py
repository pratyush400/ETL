import csv
import os
class ETL:
    def __init__(self):
        self.reader = []
        self.treeID = []
        self.birdID = []
        self.tree_NestsIn = []
        self.bird_NestsIn = []
        self.year_NestsIn = []
        self.query_NestsIn = []
        self.bird_SpeciesC = []
        self.bird_SpeciesS = []
        self.bird_SpeciesID = []


    def read_data(self):
        i_birdID = 1
        i_birdSciID = 1
    
        with open('tree.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                self.treeID.append(row[2])

        with open('bird.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                self.bird_SpeciesC.append(row[1])
                self.bird_SpeciesS.append(row[2])
                self.bird_SpeciesID.append(i_birdSciID)
                i_birdSciID += 1
        # print(self.bird_SpeciesID)

        with open('junction.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                self.bird_NestsIn.append(row[0])
                self.year_NestsIn.append(row[2])
                self.tree_NestsIn.append(row[1])

            for row in range(len(self.bird_NestsIn)):
                self.birdID.append(i_birdID)
                i_birdID = i_birdID + 1

    def create_table(self):
        birdSpecTable = []

        for i in range(len(self.bird_SpeciesID)):
            temp = f'''INSERT INTO BirdSpecies (ID, SpeciesCommon, SpeciesScientific ){os.linesep}VALUES ({self.bird_SpeciesID[i]},'{self.bird_SpeciesC[i]}','{self.bird_SpeciesS[i]}');{os.linesep}{os.linesep}'''
            birdSpecTable.append(temp)

        # print(birdSpecTable)

        with open('birdSpecTable.sql', 'w', encoding='utf-8') as f:
            for item in birdSpecTable:
                f.write(item)

        




if __name__ == '__main__':
    run = ETL()
    run.read_data()
    run.create_table()


