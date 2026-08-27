import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
result=[]
def solve_heat_equation(N,L,alpha,To,t,R):
    x=np.linspace(0,L,N+1)
    T=np.zeros(N+1)
    T[0]=To
    dx=x[1]-x[0]
    dt=R*(dx**2)/alpha
    T_initial=T.copy()
    current_time=0
    # Simulation
    while(current_time<t):
        dt_step=min(dt,t-current_time)
        T_new=T.copy()
        r=alpha*dt_step/(dx**2)
        for i in range(1,len(T)-1):
            T_new[i]=T[i]+r*(T[i-1]+T[i+1]-2*T[i])
        T=T_new
        current_time+=dt_step
    plt.plot(x,T,label='Calculated')
    return (T)


# Theoretical Answer
def analytical_solution(N,L,alpha,To,t,n_terms):
    x=np.linspace(0,L,N+1)
    T_ss=To*(1-(x/L))
    transient=np.zeros_like(x)
    for i in range (1,n_terms+1):
        transient+=(2*To/((np.pi)*i))*np.sin(i*(np.pi)*x/L)*np.exp(-alpha*((i*(np.pi)/L)**2)*t)
    #plt.plot(x,T_ss-transient,label='Analytical')
    return T_ss-transient

#Error
def error():
    dx=L/N
    error=np.max(np.abs(analytical_solution(N,L,alpha,To,t,n_terms)-solve_heat_equation(N,L,alpha,To,t)))
    result.append([N,dx,error])

# Plots
# plt.plot(x,T,label='Calculated')
# plt.plot(x,analytical_solution(x,t,L,alpha,100),label='Analytical')

# Input
L=int(input('Lenght of Rod : '))
To=int(input('Initial temperature of front end : '))
N=int(input('Number of Spacial points : '))
n_terms=int(input('Number of terms in analytical solution : '))
alpha=float(input('Enter value of Alpha : '))
t=int(input('Time : '))
check = [0.4,0.45,0.5,0.525,0.55,0.6,0.7]
for R in check:
    solve_heat_equation(N,L,alpha,To,t,R)
    plt.show()

#Observation
# df=pd.DataFrame(
#     result,
#     columns=['N','dx','Error']
# )
# print(df)
# df.to_csv('Result.csv',index=False)
# plt.loglog(df['dx'], df['Error'], 'o-')
# plt.xlabel('dx')
# plt.ylabel('Maximum Error')
# plt.grid()
# plt.show()
    



