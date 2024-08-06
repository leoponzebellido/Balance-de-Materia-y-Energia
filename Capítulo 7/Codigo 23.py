import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
    
# 1. Definir valores
k1 = 0.933
V = 10
CI = 0.1
F = 1
Cf = 0.1
    
# 2. Definir la función a solucionar (EDO)
def f(t, CA):
    return (F/V) * (Cf-CA) -k1 * (CA ** 2) # <------ Escribir aqui la EDO
    
# 3. Condiciones iniciales (Modificar valores en el código)
t0 = 0
CA0 = CI
    
# 4. Definir periodos de tiempo
t_span = (t0, 500)  # desde t0 hasta t=500
    
# 5. Resolver la EDO
sol = solve_ivp(f, t_span, [CA0])
    
# 6. Graficar
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.title('Concentración vs Tiempo')
plt.grid(True)
plt.show()
