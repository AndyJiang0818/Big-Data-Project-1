# Model HetioNet

## Overview
1. Build a database system to model HetioNet.
2. Given a disease id, what is its name, what are drug names that can treat or palliate this disease, what are gene names that cause this disease, and where this disease occurs? Obtain and ouput this info in a single query. 
3. Find all compounds that can treat a new disease name. Obtain and ouput all drugs in a single query. 

## Run
### STEP 1:
- Open the mongodb.py file
- Then find the line "self.cluster = MongoClient('mongodb+srv://localhost:27017@cluster0.5cgqa.mongodb.net/<dbname>?retryWrites=true&w=majority')" 
- Change "localhost" to your own username 
- Change "27017" to your own password 

- Open the neo4j.py file
- Then find the line "self.username = 'localhost'" and "self.password = 'neo4j'"
- Change "neo4j" to your own username 
- Change "neo4j" to your own password 

### STEP 2:
- Open the cammand prompt
- Then type the following command: 
- cd (where you save the file)
- python project1.py

### STEP 3:
- Then follow the instructions to get the information you want. 

### STEP 4:
#### Query 1: 
1. Given a disease, show what is its name, what are drug names that can treat or palliate this disease, what are gene names that cause this disease, and where this disease occurs 
2. All the data are stored in MongoDB 

#### Query 2: 
1. A compound can treat a disease if the compound or its resembled compound up-regulates/down- regulates a gene, but the location down-regulates/up-regulates the gene in an opposite direction where the disease occurs. Find all compounds that can treat a new disease name (i.e. the missing edges between compound and disease excluding existing drugs) 
2. All the data are stored in neo4j 
  
## Potential Improvements
1. Choose a better NoSQL database
2. Design a better database schema
3. Create a better index to support read operations
4. Create a better index to support the query
5. Reduce $lookup: For user running too many $lookup operations on our data. Take
advantage of MongoDB’s rich schema model to embed related data in a single collection.
6. Avoid unbounded array: If the documents contain array fields with many elements, which
can degrade query performance.
7. Remove unnecessary index: unnecessary indexes in the collection, which can consume
disk space and degrade write performance.
8. Reduce the size of large documents: If we have excessively large documents, which can
degrade the performance of our most frequent queries.
9. Reduce number of collections: If we have an exceedingly high number of collections in a
database, which can result in unnecessary disk space usage.
10. Improve of case insensitive regex queries: we are executing case-insensitive regex
queries which could be improved with an index. 
