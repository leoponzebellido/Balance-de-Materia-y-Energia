import pandas as pd

Datos_15psi = [15, 212.99, 26.297, 969.47]
Datos_20psi = [20, 227.92, 20.093, 959.93]

df_15psi = pd.DataFrame(
    [Datos_15psi], columns=["Presión", "Temperatura", "Volumen", "Entalpía"]
)
df_20psi = pd.DataFrame(
    [Datos_20psi], columns=["Presión", "Temperatura", "Volumen", "Entalpía"]
)

Nueva_presion = int(input("Ingrese una nueva presión: "))

Datos_Nueva_presion = []
Datos_Nueva_presion.append(Nueva_presion)
for i in range(1, len(Datos_15psi)):  
    dato_interpolado = Datos_20psi[i] - (
        (Datos_20psi[i] - Datos_15psi[i]) / (Datos_20psi[0] - Datos_15psi[0])
    ) * (Datos_20psi[0] - Nueva_presion)
    Datos_Nueva_presion.append(dato_interpolado)

df_interpolado = pd.DataFrame(
    [Datos_Nueva_presion], columns=["Presión", "Temperatura", "Volumen", "Entalpía"]
)
df_final = pd.concat([df_15psi, df_interpolado, df_20psi], ignore_index=True)

print(df_final.to_string(index=False))