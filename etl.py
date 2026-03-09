import csv
import os
from datetime import datetime
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
        self.bird_neighbourhood = []
        self.bird_obseredvedDate = []
        self.bird_obseredvedDate_conv = []
        self.siteID = []
        self.siteType = []
        self.siteSize = []
        self.siteWidth = []




    def read_data(self):
        i_birdID = 1
        i_birdSciID = 1
    
        with open('tree.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                self.treeID.append(row[2])
                self.siteID.append(row[2])
                self.siteType.append(row[11])
                self.siteSize.append(row[12])
                self.siteWidth.append(row[13])
        
        with open('bird.csv', mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                self.bird_SpeciesC.append(row[1])
                self.bird_SpeciesS.append(row[2])
                self.bird_neighbourhood.append(row[11])
                self.bird_SpeciesID.append(i_birdSciID)
                i_birdSciID += 1
                self.bird_obseredvedDate.append(row[7])
            
            format_code = "%d %b %Y"
            for date in range(len(self.bird_obseredvedDate)):
                data_converter = datetime.strptime(self.bird_obseredvedDate[date],format_code)
                self.bird_obseredvedDate_conv.append(data_converter)

            #     print(self.bird_obseredvedDate_conv[i])

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
        with open('birdSpecTable.sql', 'w', encoding='utf-8') as f:
            for item in birdSpecTable:
                f.write(item)

        birdTable = []
        j = 0
        for i in range(len(self.birdID)):
            if j >= 354:
                j = 0
            temp = f'''INSERT INTO Bird (ID,BirdSpeciesID , Neighbourhood, ObservedDate ){os.linesep}VALUES ({self.birdID[i]},{self.bird_SpeciesID[j]},"{self.bird_neighbourhood[j]}", "{self.bird_obseredvedDate_conv[j]}");{os.linesep}{os.linesep}'''
            birdTable.append(temp)
            j += 1
        with open('birdTable.sql', 'w', encoding='utf-8') as f:
            for item in birdTable:
                f.write(item)

        siteTable = []
        for i in range(len(self.siteID)):
            temp = f'''INSERT INTO Site (ID, SiteType, SiteSize, SiteWidth){os.linesep}VALUES ({self.siteID[i]},'{self.siteType[i]}','{self.siteSize[i]}',{self.siteWidth[i]});{os.linesep}{os.linesep}'''
            siteTable.append(temp)
        with open('siteTable.sql', 'w', encoding='utf-8') as f:
            for item in siteTable:
                f.write(item)

        treeTable = []
        for i in range(len(self.treeID)):
            temp = f'''INSERT INTO tree (ID, SiteID, Species, MatureSize, XCoordinate,  )'''
        
        
        
        
        

        

        
        

        




if __name__ == '__main__':
    run = ETL()
    run.read_data()
    run.create_table()


