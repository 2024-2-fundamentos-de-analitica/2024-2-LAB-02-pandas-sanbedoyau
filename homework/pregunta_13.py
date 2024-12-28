import pandas as pd

def pregunta_13():
    '''
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`
    R/=
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    '''
    tbl0 = pd.read_csv('files/input/tbl0.tsv',
                       sep = '\t')
    tbl2 = pd.read_csv('files/input/tbl2.tsv',
                       sep = '\t')
    R = tbl2.copy()
    R = R.join(tbl0, on = 'c0', lsuffix='_tbl2', rsuffix='_tbl0')[['c1','c5b']]
    return R.groupby('c1')['c5b'].sum()