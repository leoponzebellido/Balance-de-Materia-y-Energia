print('\nMasas en Kg (Operación 2):')
df.at['Masa, Kg', 2] = df.at['Masa, Kg', 1] - df.at['Masa, Kg', 1] * 0.08
df.at['Almidón, Kg', 2] = (df.at['Masa, Kg', 2] * df.at['Almidón, %', 2])/100
df.at['Agua, Kg', 2] = (df.at['Masa, Kg', 2] * df.at['Agua, %', 2])/100
df.at['Sólidos, Kg', 2] = (df.at['Masa, Kg', 2] * df.at['Sólidos, %', 2])/100
print(df)