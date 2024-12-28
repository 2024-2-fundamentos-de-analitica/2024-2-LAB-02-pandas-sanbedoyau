import pandas as pd

def pregunta_01():
    '''
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?
    R/= 40
    '''
    df: pd.DataFrame = pd.read_csv('files/input/tbl0.tsv',
                     sep = '\t',
                     index_col = 'c0'
                     )
    return df.shape[0]