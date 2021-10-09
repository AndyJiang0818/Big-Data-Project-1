from mongodb import MongoDB
from neo4j import Neo4j

project1 = '''
Welcome to HetioNet! 

What would you like to do? 

1)MongoDB: 

Given a disease, 
show what is its name, 
what are drug names that can treat or palliate this disease, 
what are gene names that cause this disease, 
and where this disease occurs. 

2)Neo4j: 

A compound can treat a disease 
if the compound or its resembled compound 
up-regulates/down- regulates a gene, 
but the location down-regulates/up-regulates the gene 
in an opposite direction where the disease occurs. 
Find all compounds that can treat a new disease name 
(i.e. the missing edges between compound and disease excluding existing drugs). 
'''


def main():
    print(project1)

    while True:
        print('Please choose 1 or 2: ')
        choice = input('1', '2')

        if choice == '1':
            output = "Enter a disease id: "
            run = MongoDB()
        elif choice == '2':
            output = "Enter a drug name: "
            run = Neo4j()
        else:
            output = "Invalid number! Please reenter!"

        query = input(output)
        run.query_db(query)


if __name__ == "__main__":
    main()
