##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("tbl1.tsv", sep="\t")
df['_c4'].sort_values().apply(lambda x: x.upper()).unique()
