import pandas as pd

h_esp = [-2805, -382.6, -1655.4, -1366.8, 0]
Masa_m = [180, 14, 92, 46, 0]
kJ_kg = []
flujo_m = [36, 0.4, 7.94, 11.9, 2.81]

# Momento específico para la división
for elem in range(len(h_esp)-1):
  kJ_kg.append(round((h_esp[elem] / Masa_m[elem]), 2))
kJ_kg.append(-21200)

dat = {'Δh (kJ/gmol)': h_esp, 'Masa Molecular': Masa_m, 'kJ/kg': kJ_kg,  'Flujo másico': flujo_m}
tabla = pd.DataFrame(dat)
tabla = tabla.transpose()
tabla.columns = ['Glu', 'NH3', 'Gli', 'EtOH', 'SC']
print(tabla)
