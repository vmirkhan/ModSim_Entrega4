def CalculaDeltaT(Tu,R,Rc1,gama,Ct):
    return gama*Tu*((R/Rc1) - 1) - Ct*Tu
def CalculaDeltaR(Tu,R,Tuc,alfa,Cr):
    return alfa*Tu*(1-(Tu/Tuc)) - Cr*R
Tu = [0]*21
Tu[0] = 1000000
gama= 0.18
Ct = [0]*21
Ct[0] = 0.6
R = [0]*21
R[0] = 40000000
alfa = 0.08
Cr = [0]*21
Cr[0] = 0
T = [0]*21
T[0] = 0
Tuc = 500000
Rc1 = 10000000

for i in range(0,20):
    delta_Tu = CalculaDeltaT(Tu[i],R[i],Rc1,gama,Ct[i])
    delta_R = CalculaDeltaR(Tu[i],R[i],Tuc,alfa,Cr[i])
    Cr[i+1] = Cr[i] + 0.015
    Ct[i+1] = Ct[i] - 0.035
    R[i+1] = int(R[i] + delta_R)
    Tu [i+1] = int(Tu[i] + delta_Tu)
    T[i+1] = i+1
    print("População de tubarão:",Tu[i])
    print("População de raias",R[i])

import matplotlib.pyplot as plt
    
plt.plot(T,R)
plt.axis([0,20,0,50000000])
plt.ylabel("R [Raias]")
plt.xlabel ("T [tempo em anos]")
plt.title ("R em função do tempo")
plt.show()

plt.plot(T,Tu)
plt.axis([0,20,0,2000000])
plt.ylabel("Tu [Tubarões]")
plt.xlabel ("T [tempo em anos]")
plt.title ("Tu em função do tempo")
plt.show()