import pandas as pd

def pregunta_02():
    '''
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?
    R/= 4
    '''
    df = pd.read_csv('files/input/tbl0.tsv',
                     sep = '\t')
    return df.shape[1]