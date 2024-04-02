print('\nMasas en Kg (Operación 5):')
df.at['Masa, Kg', 5] = df.at['Masa, Kg', 4]
df.at['Almidón, Kg', 5] = (df.at['Masa, Kg', 5] * df.at['Almidón, %', 5])/100
df.at['Agua, Kg', 5] = (df.at['Masa, Kg', 5] * df.at['Agua, %', 5])/100
df.at['Sólidos, Kg', 5] = (df.at['Masa, Kg', 5] * df.at['Sólidos, %', 5])/100
print(df)