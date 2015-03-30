"""
Simulação da interação entre raias,tubarões e vieiras em um periodo de 100 anos.

O modelo conta com a alteração das taxas de caça relativas aos tubarões e às raias,
sendo que a cada ano a taxa das raias sobe (mais raias caçadas) e a dos tubarões desce (menos tubarões caçados).
O objetivo é ver como essas alterações afetam a população das vieiras a longo prazo.

Espera-se que a população das vieiras decresça por um tempo e depois, com o decrescimo da população de raias,
a população suba rapidamente.

"""





def CalculaDeltaT(Tu,R,Rc1,gama,Ct):
    return gama*Tu*((R/Rc1) - 1) - Ct*Tu
def CalculaDeltaR(Tu,R,Tuc,alfa,Cr):
    return alfa*Tu*(1-(Tu/Tuc)) - Cr*R
def CalculaDeltaV(V,R,Rc2,beta):
    return beta*V*(1 - (R/Rc2))

Tu = 101*[0]
Tu[0] = 1500000                    #um milhão e quinhetos mil (pop inicial de tubarões)
V = 101*[0]
V[0] = 100000000                  #cem milhões (pop inicial de vieiras)
R = 101*[0]
R[0] = 40000000                   #quarenta milhões (pop inicial de raias)

gama = 0.18                       #crescimento vegetativo de tubarões
alfa = 0.08                       #crescimento vegetativo de raias
beta = 0.15                       #crescimento vegetativo de vieiras

Tuc = 500000                       #quinhentos mil (número crítico de tubarões)
Rc1 = 10000000                    #dez milhões (número crítico de raias para tubarões)
Rc2 = 30000000                     #trinta milhões (número crítico de raias para vieiras)

Ct = [0]*101
Ct[0] = 0.6                       #taxa de caça inicial de tubarões
Cr = [0]*101
Cr[0] = 0.02                      #taxa de caça inicial de raias 

T = [0]*101
T[0] = 0

for i in range(0,100):
    delta_Tu = CalculaDeltaT(Tu[i],R[i],Rc1,gama,Ct[i])
    delta_R = CalculaDeltaR(Tu[i],R[i],Tuc,alfa,Cr[i])
    delta_V = CalculaDeltaV(V[i],R[i],Rc2,beta)
    Cr[i+1] = Cr[i] + 0.00005
    Ct[i+1] = Ct[i] - 0.010
    V[i+1] = int(V[i] + delta_V)
    R[i+1] = int(R[i] + delta_R)
    Tu [i+1] = int(Tu[i] + delta_Tu)
    T[i+1] = i+1
print("População de vieiras inicial:",V[0])
print("População de vieiras final:",V[100])
print("População de raias inicial:",R[0])
print("População de raias final",R[100])
print("População de tubarões inicial",Tu[0])
print("População de tubarões final",Tu[100])
    
import matplotlib.pyplot as plt
    
plt.plot(T,R, 'blue')
plt.axis([0,100,0,50000000])
plt.ylabel("R [Raias]")
plt.xlabel ("T [tempo em anos]")
plt.title ("R em função do tempo")
plt.show()

plt.plot(T,Tu, 'green')
plt.axis([0,100,0,2000000])
plt.ylabel("Tu [Tubarões]")
plt.xlabel ("T [tempo em anos]")
plt.title ("Tu em função do tempo")
plt.show()

plt.plot(T,V,'red')
plt.axis([0,40,0,200000000])
plt.ylabel("V [Vieiras]")
plt.xlabel ("T [tempo em anos]")
plt.title ("V em função do tempo")
plt.show()

plt.plot(T,V,'red')
plt.axis([30,100,0,80000000000])
plt.ylabel("V [Vieiras]")
plt.xlabel ("T [tempo em anos]")
plt.title ("V em função do tempo")
plt.show()