import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([0, 1, 2, 3, 4, 5, 5.5, 7])
y = np.array([0, 0.36, 0.48, 0.56, 0.62, 0.59, 0.6838, 0.7129])

pendiente, intercepto, r_value, p_value, std_err = stats.linregress(x, y)

plt.figure(figsize=(10, 6))
plt.grid(True)

plt.scatter(x, y, label="Puntos")

plt.plot(x, y, linestyle="-", marker="o")

plt.plot(
    x, pendiente * x + intercepto, color="red", linestyle="--", label="Regresión lineal"
)

plt.plot(
    np.ones(10) * 1, np.linspace(0, 1, 10), color="black", linestyle="-", label="x=1"
)
plt.plot(
    np.linspace(0, 10, 10),
    0.2 * np.linspace(0, 10, 10) + 0.16,
    color="purple",
    linestyle="-",
    label="y=0.2x+0.16",
)
plt.plot(
    np.linspace(0, 10, 10),
    0.16 * np.ones(10),
    color="black",
    linestyle="-",
    label="y=0.16",
)

plt.xlabel("Tiempo, h")
plt.ylabel("Conversión mol/mol")

plt.xlim(0, 10)
plt.ylim(0, 1.2)

plt.show()
