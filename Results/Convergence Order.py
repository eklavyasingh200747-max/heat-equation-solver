import numpy as np
import pandas as pd
df=pd.read_csv('Result.csv')
E=df['Error']
dx=df['dx']
ans=[]
for i in range(5):
    order=np.log(E[i]/E[i+1])/np.log(dx[i]/dx[i+1])
    ans.append(order)
df1=pd.DataFrame(ans,columns=['Convergence Order'])
df1.to_csv('Convergence Order.csv',index=False)

