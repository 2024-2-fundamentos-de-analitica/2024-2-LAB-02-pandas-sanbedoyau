import pandas as pd

def pregunta_06():
    '''
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente
    R/= ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    '''
    df = pd.read_csv('files/input/tbl1.tsv',
                     sep = '\t')
    return sorted(list(map(lambda x: x.upper(), df['c4'].unique())))