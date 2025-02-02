import pandas as pd
import os

def read_corpus() -> pd.DataFrame:
    path = 'corpus'
    return pd.read_csv(os.path.join(path, 'testing.csv'), converters={'essay': eval, 'competence': eval})

print(read_corpus().head())