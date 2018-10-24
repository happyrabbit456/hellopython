import pandas as pd
import numpy as np

s1=np.array([1,2,3,4])
s2=np.array([5,6,7,8])
df=pd.DataFrame([s1,s2])
print(df)
s3=s1+s2
print(s3)