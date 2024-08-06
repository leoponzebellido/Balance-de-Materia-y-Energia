import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros de la ecuación
K = 1.26e-6
C0 = 200
alpha = 1.28
F = 5

# Definimos una función que represente la ecuación diferencial
def dX_dV(V, X):
    return - (K * C0**alpha * (1 - X)**alpha) / (F * C0)

# Valores iniciales
X0 = 0  
V_span = (0, 1000)

# Resolvemos la EDO
sol = solve_ivp(dX_dV, V_span, [X0], t_eval=np.linspace(V_span[0], V_span[1], 500))

# Graficamos la solución
plt.plot(sol.t, sol.y[0])
plt.xlabel('V')
plt.ylabel('X')
plt.title('Solución de la Ecuación Diferencial')
plt.grid()
plt.show()
