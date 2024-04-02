# Calcular la masa del almidón
print('\nMasa de Almidón, Agua y Sólidos en Kg (Operación 1):')
df.at['Almidón, Kg', 1] = (df.at['Masa, Kg', 1] * df.at['Almidón, %', 1])/100

# Calcular la masa de los sólidos
df.at['Sólidos, Kg', 1] = (df.at['Masa, Kg', 1] * df.at['Sólidos, %', 1])/100

# Calcular la masa de agua
df.at['Agua, Kg', 1] = (df.at['Masa, Kg', 1] * df.at['Agua, %', 1])/100
print(df)