import numpy as np
import matplotlib.pyplot as plt 
import ipywidgets as widget
from ipywidgets import interact, Layout

#definition des parametres du modele
N = 1000  # Population totale
beta = 0.3  # Taux de transmission
alpha = 0.1  # Taux de guérison
gamma = 0.05  # Taux de mortalité
eta = 0.02  # Taux de transition de T vers R
delta = 0.1  # Paramètre supplémentaire

# Conditions initiales
S0 = N - 1
I0 = 1
T0 = 0
R0 = 0

# Pas de temps et nombre d'itérations
h = 0.1
Nb_iterations = 1000

def system(S,I,R,T) : 
    dS = -beta / N * (I + delta * T) * S
    dI = beta / N * (S * (I + delta * T)) - (alpha + gamma) * I
    dT = alpha * I - eta * T
    dR = gamma * I + eta * T
    return dS, dI, dT, dR

def euler_implicite(S,I,R,T,h) : 
    dS, dI, dR, dT = system(S,I,R,T) 
    Sn= S / (1 + beta * h * (I + delta * T) / N)
    In = I + h * (beta * S * (I + delta * T) / N - (alpha + gamma) * I)
    Tn = T + h * (alpha * I - eta * T)
    Rn = R + h * (gamma * I + eta * T)
    
    return Sn, In, Tn, Rn 

def res_system(method) : 
    S_res = [S0]
    I_res = [I0]
    T_res = [T0]
    R_res = [R0]
    S, I, T, R = S0, I0, T0, R0
    k = 0
    while (k < Nb_iterations) :
        S, I, T, R = method(S, I, T, R, h)
        S_res.append(S)
        I_res.append(I)
        T_res.append(T)
        R_res.append(R)
        k+=1
    
    return S_res, I_res, T_res, R_res

S_euler, I_euler, T_euler, R_euler = res_system(euler_implicite)
plt.figure(figsize=(10, 6))
plt.plot(range(Nb_iterations + 1), S_euler, label='S (Euler implicite)', color='blue')
plt.show()
    