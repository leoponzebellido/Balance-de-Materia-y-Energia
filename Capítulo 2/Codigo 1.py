# Definir Variables:
print('Definamos nuestras variables:\n')

W = float(input("Ingrese los moles de Agua: W = "))
AS = float(input("Ingrese los moles de Aire Seco: AS = "))
Ox = float(input("Ingrese los moles de Oxígeno Puro: Ox = "))

# Operamos:
AHE = W + AS + Ox
P_W_AHE = (100 * W)/AHE
P_Ox_AHE = 100 * (Ox + 0.21 * AS)/AHE
P_N_AHE = 100 * 0.79 * (AS/AHE)
PM_AS = 0.21 * 32 + 0.79 * 28
PM_AHE = (P_Ox_AHE/100) * 32 + (P_N_AHE/100) * 28 + (P_W_AHE/100) * 18

# Resultados
print(f'\n[2.1] Los moles totales de Aire Húmedo Enriquecido son: {round(AHE, 2)} moles.')
print(f'[2.2] El porcentaje de agua en el Aire Húmedo Enriquecido es de: {round(P_W_AHE, 2)}%.')
print(f'[2.3] El porcentaje de Oxígeno en el Aire Húmedo Enriquecido es de: {round(P_Ox_AHE, 2)}%.')
print(f'[2.4] El porcentaje de Nitrógeno en el Aire Húmedo Enriquecido es de: {round(P_N_AHE, 2)}%.')
print(f'[2.5] El Peso Molecular del Aire Seco es de: {round(PM_AS, 2)} g por cada mol.')
print(f'[2.6] El Peso Molecular del Aire Húmedo Enriquecido es de: {round(PM_AHE, 2)} g por cada mol.')