import pandas as pd

def pregunta_11():
     '''
     Construya una tabla que contenga `c0` y una lista separada por ',' de
     los valores de la columna `c4` del archivo `tbl1.tsv`
     R/=
          c0       c4
     0     0    b,f,g
     1     1    a,c,f
     2     2  a,c,e,f
     3     3      a,b
     ...
     37   37  a,c,e,f
     38   38      d,e
     39   39    a,d,f
     '''
     df = pd.read_csv('files/input/tbl1.tsv',
                         sep = '\t')
     R = df.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(x)))
     R = R.reset_index()
     return R