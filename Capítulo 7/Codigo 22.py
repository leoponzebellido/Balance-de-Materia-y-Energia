import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definir valores
k1 = 0.1
V = 1.0
CI = 1.0

# 2. Definir la función a solucionar (EDO)
def f(t, CA):
    return -k1 * V * CA # <------ Escribir aqui la EDO

# 3. Condiciones iniciales (Modificar valores en el código)
t0 = 0
CA0 = CI

# 4. Definir periodos de tiempo
t_span = (t0, 100)  # desde t0 hasta t=100

# 5. Resolver la EDO
sol = solve_ivp(f, t_span, [CA0])

# 6. Graficar
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.title('Concentración vs Tiempo')
plt.grid(True)
plt.show()
