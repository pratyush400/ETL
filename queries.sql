

 --Query1
USE tree;

    SELECT Neighbourhood, COUNT(ObservedDate) AS Number_of_Observations
    FROM Bird
    GROUP BY Neighbourhood
    ORDER BY COUNT(ObservedDate) DESC, Neighbourhood
    LIMIT 10;

--Query2

USE tree;

    SELECT COUNT(SpeciesCommon) AS Number_of_Species_in_Neighbourhood, Neighbourhood
    FROM BirdSpecies, Bird
    WHERE SpeciesCommon IN (Neighbourhood)
    ORDER BY COUNT(SpeciesCommon) DESC;

--Query3

USE tree;

    SELECT SpeciesCommon AS Bird_Name, BirdSpeciesID, Bird.ID
    FROM BirdSpecies
    JOIN Bird ON Bird.BirdSpeciesID = BirdSpecies.ID
	WHERE ObservedDate LIKE '2022-02-06%';

--Query4

USE tree;
    SELECT DISTINCT Species AS Species_that_has_flower, ID
    FROM Tree
	WHERE Species LIKE '%flower%';


--For a specified nest year, list each bird species and the number of different trees in which that species built nests.
USE tree;

SELECT BirdSpecies.SpeciesCommon, NestYear, COUNT(DISTINCT NestsIn.TreeID) AS TreeCount
FROM NestsIn
JOIN Bird ON NestsIn.BirdID = Bird.ID
JOIN BirdSpecies ON Bird.BirdSpeciesID = BirdSpecies.ID
WHERE NestsIn.NestYear = 2024
GROUP BY BirdSpecies.SpeciesCommon
ORDER BY TreeCount DESC;

--For a specified tree, list all birds that nested in and years it occurred 
USE tree;
SELECT BirdSpecies.SpeciesCommon, NestsIn.NestYear
FROM NestsIn
JOIN Bird ON NestsIn.BirdID = Bird.ID
JOIN BirdSpecies ON Bird.BirdSpeciesID = BirdSpecies.ID
WHERE NestsIn.TreeID = 1
ORDER BY NestsIn.NestYear;

-- Query7(add new bird species)
USE tree;
INSERT INTO BirdSpecies( SpeciesCommon, SpeciesScientific ) 
VALUES ('California Condor','Gymnogyps californianus');
INSERT INTO BirdSpecies( SpeciesCommon, SpeciesScientific ) 
VALUES ('Chukar','Alectoris chukar');

--query 8
USE tree;
INSERT INTO Bird( BirdSpeciesID, Neighbourhood, ObservedDate )
VALUES((SELECT ID From BirdSpecies WHERE BirdSpecies.SpeciesCommon = 'California Condor'), 'Lewis & Clark College', '2024-06-30 00:00:00');

INSERT INTO Bird( BirdSpeciesID, Neighbourhood, ObservedDate )
VALUES((SELECT ID From BirdSpecies WHERE BirdSpecies.SpeciesCommon = 'Chukar'), 'Pioneer Square', '2025-07-30 00:00:00');

--Query 9
USE tree;

INSERT INTO NestsIn(TreeID, BirdID, NestYear )
VALUES (2, (SELECT ID FROM Bird WHERE Bird.BirdSpeciesID = (SELECT ID From BirdSpecies WHERE BirdSpecies.SpeciesCommon = 'Chukar')),2024 )

--Query 10
USE tree;
INSERT INTO Tree(SiteID, Species, MatureSize, XCoordinate, YCoordinate)
VALUES (LAST_INSERT_ID() + 1, 'Cornus spp. - dogwood', 'Large', -13657011.1234, 5708984.7282);

