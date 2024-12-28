import pandas as pd

def pregunta_10():
    '''
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`
    R/=
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    '''
    df = pd.read_csv('files/input/tbl0.tsv',
                     sep = '\t',
                     index_col = 'c0')
    R = df.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).to_frame()
    return R