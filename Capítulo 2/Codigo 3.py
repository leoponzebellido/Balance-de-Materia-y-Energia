import pandas as pd

Nro_Op = 7  # <---- Aquí puede cambiar el número de operaciones de su sistema
Almidon_P = []
Agua_P = []
Solidos_P = []
Masa = [0 for i in range(Nro_Op)]
Almidon = [0 for i in range(Nro_Op)]
Agua = [0 for i in range(Nro_Op)]
Solidos = [0 for i in range(Nro_Op)]
print("A continuación, ingrese al programa el porcentaje de almidón,")
print("agua y sólidos según el número de operación. Si la operación ")
print("en cuestión posee una entrada vacía, ingrese el número 0.")

# Ingresar el porcentaje de almidón correspondiente a la operación
print("\nIngrese el porcentaje de almidón correspondiente a la operación:")
for A_Op in range(Nro_Op):
    Almidon_P.append(float(input(f"Operación {A_Op + 1}: ")))

# Ingresar el porcentaje de agua correspondiente a la operación
print("\nIngrese el porcentaje de agua correspondiente a la operación:")
for W_Op in range(Nro_Op):
    Agua_P.append(float(input(f"Operación {W_Op + 1}: ")))

# Ingresar el porcentaje de sólidos correspondientes a la operación
print("\nIngrese el porcentaje de sólidos correspondientes a la operación:")
for S_Op in range(Nro_Op):
    Solidos_P.append(float(input(f"Operación {S_Op + 1}: ")))

Masa[0] = float(input("\nIngrese su masa inicial: "))  # <---- Masa inicial

# Crear la tabla
data = {
    "Masa, Kg": Masa, "Almidón, Kg": Almidon,
    "Agua, Kg": Agua, "Sólidos, Kg": Solidos,
    "Almidón, %": Almidon_P, "Agua, %": Agua_P,
    "Sólidos, %": Solidos_P,
}
df = pd.DataFrame(data)
df = df.transpose()
df.columns = [i + 1 for i in range(Nro_Op)]
print("\nTabla resultante:")
print(df)