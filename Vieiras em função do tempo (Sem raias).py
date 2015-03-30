def CalculaDeltaV(V,beta):
    return V*beta
V = 21*[0]
V[0] = 100000000
beta = 0.15
T = [0]*21
T[0] = 0
for i in range(0,20):
    delta_V = CalculaDeltaV(V[i],beta)
    V[i+1] = int(V[i] + delta_V)
    T[i] = i+1
    print(V[i])
    
import matplotlib.pyplot as plt

plt.plot (T,V)
plt.axis([0,20,V[0],1430000000])
plt.ylabel("V [Vieiras]")
plt.xlabel ("T [tempo em anos]")
plt.title ("V em função do tempo")
plt.show()