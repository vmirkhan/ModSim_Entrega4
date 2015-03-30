def CalculaDeltaR(R,alfa,Cr):
    return R*(alfa-Cr)
R = [0]*21
R[0] = 40000000
alfa = 0.08
Cr = [0]*21
Cr[0] = 0
T = 21*[0]
T[0] = 0

for i in range(0,20):
     delta_R = CalculaDeltaR(R[i],alfa,Cr[i])
     Cr[i+1] = Cr[i] + 0.01
     R[i+1] = int(R[i] + delta_R)
     T[i+1] = T[i] + 1
     print (R[i+1])  
import matplotlib.pyplot as plt

plt.plot (T,R)
plt.axis([0,T[20],R[20],60000000])
plt.ylabel("R [Raias]")
plt.xlabel ("T [tempo em anos]")
plt.title ("R em função do tempo")
plt.show()