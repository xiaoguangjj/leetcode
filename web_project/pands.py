
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
right =  pd.DataFrame({'key':['foo','foo'],'rval':[4,5]})

df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])

# print left
# print right

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
p = ts.cumsum().plot()