import pymongo
import csv
from pymongo import MongoClient


class MongoDB():
    def __init__(self):
        self.cluster = MongoClient('mongodb+srv://localhost:27017@cluster0.5cgqa.mongodb.net/<dbname>?retryWrites=true&w'
                                   '=majority')
        self.db = self.cluster['hetionet']
        self.collection = self.db['table']

    def create_db(self):
        table = {
            'Anatomy': {},
            'Disease': {},
            'Gene': {},
            'Compound': {}
        }

        disease = {
            'disease_id': [],
            'disease_name': [],
            'drug_name': [],
            'gene_name': [],
            'disease_occurs': []
        }

        source = {
            'AuG': ['gene_name'],
            'AeG': ['gene_name'],
            'AdG': ['gene_name'],
            'DrD': ['disease_name'],
            'DuG': ['gene_name'],
            'DaG': ['gene_name'],
            'DdG': ['gene_name'],
            'DlA': ['disease_occurs'],
            'GrG': ['gene_name'],
            'GcG': ['gene_name'],
            'GiG': ['gene_name'],
            'CrC': ['drug_name'],
            'CtD': ['drug_name'],
            'CpD': ['drug_name'],
            'CuG': ['gene_name'],
            'CbG': ['gene_name'],
            'CdG': ['gene_name']
        }

        with open('sample_nodes.tsv', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='\t')
            mylist = list(csv_reader)
            print(mylist)
            x = self.collection.insert_many(mylist)

            for x in mylist:
                print(x)

        with open('sample_edges.tsv', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='\t')
            mylist = list(csv_reader)
            print(mylist)
            x = self.collection.insert_many(mylist)

            for x in mylist:
                print(x)

    def query_db(self, query):
        input_id = self.find({'disease_id': query})

        line_count = 0

        for x in input_id:
            if line_count == 0:
                name = self.find({'disease_name': query})
                line_count += 1
            else:
                name = input_id

        disease_id = []
        disease_name = []
        drug_name = []
        gene_name = []
        disease_occurs = []

        print(
            f'Disease ID for "{query}": {disease_id}',
            f'Disease name "{query}": {disease_name}',
            f'Drug names for "{query}": {drug_name}',
            f'Gene names for "{query}": {gene_name}',
            f'Disease "{query}" occurs: {disease_occurs}'
        )
