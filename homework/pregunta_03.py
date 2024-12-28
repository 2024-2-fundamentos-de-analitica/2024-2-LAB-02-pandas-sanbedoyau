import pandas as pd

def pregunta_03():
    '''
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?
    R/=
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64
    '''
    df = pd.read_csv('files/input/tbl0.tsv',
                     sep = '\t')
    
    return df.groupby('c1').size()