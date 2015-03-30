def CalculaDeltaR(R,alfa,Cr):
    return R*(alfa-Cr)
def CalculaDeltaV(V,R,Rc2,beta):
    return beta*V*(1 - (R/Rc2))
R = [0]*21
R[0] = 40000000
alfa = 0.08
Rc2 = 30000000
Cr = 21*[0]
Cr[0] = 0.02
V = 21*[0]
V[0] = 100000000
beta = 0.15
T = [0]*21
T[0] = 1
for i in range(0,20):
    delta_V = CalculaDeltaV(V[i],R[i],Rc2,beta)
    delta_R = CalculaDeltaR(R[i],alfa,Cr[i])
    Cr[i+1] = Cr[i] + 0.015
    R[i+1] = int(R[i] + delta_R)
    V[i+1] = int(V[i] + delta_V)
    T[i+1] = i+1
    print("População de vieiras:",V[i])
    print("População de raias:",R[i])
    
import matplotlib.pyplot as plt

plt.plot (T,V)
plt.axis([T[0],T[20],40000000,100000000])
plt.ylabel("V [Vieiras]")
plt.xlabel ("T [tempo em anos]")
plt.title ("V em função do tempo")
plt.show()