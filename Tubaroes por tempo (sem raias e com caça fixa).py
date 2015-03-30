def CalculaDeltaT(Tu,gama,Ct):
    return Tu*(gama - Ct)
Tu = [0]*21
Tu[0] = 1000000
gama= 0.18
Ct = 0.6
T = [0]*21
T[0] = 0

for i in range(0,20):
    delta_Tu = CalculaDeltaT(Tu[i],gama,Ct)
    Tu [i+1] = int(Tu[i] + delta_Tu)
    T[i+1] = i+1
    print(Tu[i])

import matplotlib.pyplot as plt
    
plt.plot (T,Tu)
plt.axis([0,20,0,Tu[0],0])
plt.ylabel("Tu [Tubarões]")
plt.xlabel ("T [tempo em anos]")
plt.title ("Tu em função do tempo")
plt.show()