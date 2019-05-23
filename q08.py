##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
df = pd.read_csv("tbl0.tsv", sep="\t")
df['ano'] = df['_c3'].str.slice(0,4)
df