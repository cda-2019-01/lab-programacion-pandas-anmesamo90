##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##%matplotlib inline
##df = pd.read_csv("tbl1.tsv", sep="\t")
##df[['_c0','_c4']].sort_values('_c4',ascending = True).groupby('_c0')[('_c4')].apply(list)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
df = pd.read_csv("tbl1.tsv", sep="\t")
df['_c4']=df['_c4'].apply(str)
df2=df.sort_values('_c4',ascending = True).groupby('_c0')['_c4'].apply(lambda x: ','.join(x))
df3=pd.DataFrame({'_c0':df2.index, 'lista':df2.values})
print (df3)