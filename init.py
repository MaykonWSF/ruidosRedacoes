import pandas as pd
import os

def read_corpus():
    path = 'project\\splits\\testing.csv'
    return pd.read_csv(path, converters={'essay': eval, 'competence': eval})

print(read_corpus().head())