print('\nMasas en Kg (Operación 3):')
df.at['Masa, Kg', 3] = round((df.at['Masa, Kg', 2] * 0.08), 0)
df.at['Almidón, Kg', 3] = (df.at['Masa, Kg', 3] * df.at['Almidón, %', 3])/100
df.at['Agua, Kg', 3] = (df.at['Masa, Kg', 3] * df.at['Agua, %', 3])/100
df.at['Sólidos, Kg', 3] = (df.at['Masa, Kg', 3] * df.at['Sólidos, %', 3])/100
print(df)