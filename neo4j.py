import csv
from py2neo import Graph


class Neo4j():
    def __init__(self):
        self.username = Graph('neo4j')
        self.password = Graph('neo4j')
        self.graph = Graph(user=self.username, password=self.password)

    def create_db(self):
        nodes_file = [
            'Anatomy',
            'Disease',
            'Gene',
            'Compound'
        ]

        edges_file = [
            'AuG',
            'AeG',
            'AdG',
            'DrD',
            'DuG',
            'DaG',
            'DdG',
            'DlA',
            'GrG',
            'GcG',
            'GiG',
            'CrC',
            'CtD',
            'CpD',
            'CuG',
            'CbG',
            'CdG'
        ]

        info = {
            'A': 'Anatomy',
            'D': 'Disease',
            'G': 'Gene',
            'C': 'Compound',
            'u': 'upregulates',
            'e': 'expresses',
            'd': 'downregulates',
            'a': 'associates',
            'l': 'localizes',
            'r': 'resembles',
            'c': 'covaries',
            'i': 'interacts',
            't': 'treats',
            'p': 'palliates'
        }

    def query_db(self, query, compound):
        A = 'Anatomy'
        D = 'Disease'
        G = 'Gene'
        C = 'Compound'
        u = 'upregulates'
        e = 'expresses'
        d = 'downregulates'
        a = 'associates'
        l = 'localizes'
        r = 'resembles'
        c = 'covaries'
        i = 'interacts'
        t = 'treats'
        p = 'palliates'

        if compound == '':
            query = '''
                    MATCH (a:Compound)-[:upregulates]-(:Gene)-[:downregulates]-(b:Disease)
                    WHERE NOT (a)-[:treats]->(b)
                    RETURN DISTINCT a, b
                    '''
        else:
            query = f'''
                    MATCH (a:Compound)-[:downregulates]-(:Gene)-[:upregulates]-(b:Disease)
                    WHERE NOT (a)-[:treats]->(b)
                    RETURN DISTINCT a, b
                    '''

        result = self.graph.run(query)

        if not result:
            print('None')
        else:
            for results in result:
                print(f'Compound {results["a"]} matches Disease {results["b"]}')
