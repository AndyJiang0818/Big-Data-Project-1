# Model HetioNet

## STEP 1:
- Open the mongodb.py file
- Then find the line "self.cluster = MongoClient('mongodb+srv://localhost:27017@cluster0.5cgqa.mongodb.net/<dbname>?retryWrites=true&w=majority')" 
- Change "localhost" to your own username 
- Change "27017" to your own password 

- Open the neo4j.py file
- Then find the line "self.username = 'localhost'" and "self.password = 'neo4j'"
- Change "neo4j" to your own username 
- Change "neo4j" to your own password 

## STEP 2:
- Open the cammand prompt
- Then type the following command: 
- cd (where you save the file)
- python project1.py

## STEP 3:
- Then follow the instructions to get the information you want. 

## STEP 4:
### Query 1: 
1. Given a disease, show what is its name, what are drug names that can treat or palliate this disease, what are gene names that cause this disease, and where this disease occurs 
2. All the data are stored in MongoDB 

### Query 2: 
1. A compound can treat a disease if the compound or its resembled compound up-regulates/down- regulates a gene, but the location down-regulates/up-regulates the gene in an opposite direction where the disease occurs. Find all compounds that can treat a new disease name (i.e. the missing edges between compound and disease excluding existing drugs) 
2. All the data are stored in neo4j 
