import numpy as np
import matplotlib.pyplot as plt

def C(t):
    return 0.01875 - 0.125 * (2.073 / (10 + 0.3 * t))**(8/3)
t_valores = np.linspace(0, 100, 1000)

C_valores = C(t_valores)

tiempo = float(input("Ingrese el tiempo horas en el que desee saber la concentración: "))
print(f'La concentración en {tiempo} hora(s) es de: {round(C(tiempo), 5)} g/mL')
print("\nAdicionalmente se proporciona un perfil de la función hallada:")
plt.plot(t_valores, C_valores)
plt.xlabel('Tiempo (h)')
plt.ylabel('Concentración (g/mL)')
plt.show()
