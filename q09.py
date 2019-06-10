##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 


##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##%matplotlib inline
##df = pd.read_csv("tbl0.tsv", sep="\t")
##df[['_c1','_c2']].sort_values('_c2',ascending = True).groupby('_c1')[('_c2')].apply(list)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
df = pd.read_csv("tbl0.tsv", sep="\t")
df['_c2']=df['_c2'].apply(str)
df2=df.sort_values('_c2',ascending = True).groupby('_c1')['_c2'].apply(lambda x: ':'.join(x))

df3=pd.DataFrame({'_c0':df2.index, 'lista':df2.values})
print (df3)