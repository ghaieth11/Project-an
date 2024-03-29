from first_attempt import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import ipywidgets as widgets
from ipywidgets import interact, Layout

# Fonction décrivant les équations différentielles du système SIR
def equations_SIR(t, y, beta, alpha, gamma, eta, delta):
    S, I, T, R = y
    dS = -beta / N * (I + delta * T) * S
    dI = beta / N * (S * (I + delta * T)) - (alpha + gamma) * I
    dT = alpha * I - eta * T
    dR = gamma * I + eta * T
    return [dS, dI, dT, dR]

# Fonction pour résoudre le système pour les paramètres donnés
def solve_system(beta, alpha, gamma, eta, delta):
    sol = solve_ivp(equations_SIR, [0, max_time], [S0, I0, T0, R0], args=(beta, alpha, gamma, eta, delta), t_eval=t_values)
    return sol.y

# Fonction de mise à jour du graphique en fonction des paramètres
def update_plot(beta, alpha, gamma, eta, delta):
    S, I, T, R = solve_system(beta, alpha, gamma, eta, delta)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, S, label='S', color='blue')
    plt.plot(t_values, I, label='I', color='red')
    plt.plot(t_values, T, label='T', color='green')
    plt.plot(t_values, R, label='R', color='orange')
    plt.xlabel('Temps')
    plt.ylabel('Population')
    plt.title('Evolution des populations S, I, T et R en fonction du temps')
    plt.legend()
    plt.grid(True)
    plt.show()

# Paramètres du modèle
N = 1000  # Population totale
S0 = N - 1
I0 = 1
T0 = 0
R0 = 0
max_time = 100
t_values = np.linspace(0, max_time, 1000)

# Création des sliders pour chaque paramètre
beta_slider = widgets.FloatSlider(value=0.3, min=0, max=1, step=0.01, description='Beta:', layout=Layout(width='50%'))
alpha_slider = widgets.FloatSlider(value=0.1, min=0, max=1, step=0.01, description='Alpha:', layout=Layout(width='50%'))
gamma_slider = widgets.FloatSlider(value=0.05, min=0, max=1, step=0.01, description='Gamma:', layout=Layout(width='50%'))
eta_slider = widgets.FloatSlider(value=0.02, min=0, max=1, step=0.01, description='Eta:', layout=Layout(width='50%'))
delta_slider = widgets.FloatSlider(value=0.1, min=0, max=1, step=0.01, description='Delta:', layout=Layout(width='50%'))

# Création de l'interface interactive
interact(update_plot, beta=beta_slider, alpha=alpha_slider, gamma=gamma_slider, eta=eta_slider, delta=delta_slider);

