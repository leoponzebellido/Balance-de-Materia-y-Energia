import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

max_t = 200 # <------ Aquí puede cambiar el rango de tiempo
t = np.linspace(0, max_t, 100)

# Definimos funciones V(t) y T(t)
def V(t):
    return 3 * t + 60

def T(t):
    return 75 - 233998 / ((3 * t + 60)**2)

# Calculamos los valores de V(t) y T(t) para cada punto en el rango de tiempo
v_values = V(t)
t_values = T(t)

# Creamos un DataFrame para visualizar los valores
data = {'t': t, 'T(°C)': t_values, 'V': v_values}
df = pd.DataFrame(data)
print(df)
