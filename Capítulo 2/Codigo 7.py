print('\nMasas en Kg (Operación 4):')
df.at['Masa, Kg', 4] = df.at['Masa, Kg', 2]
df.at['Almidón, Kg', 4] = (df.at['Masa, Kg', 4] * df.at['Almidón, %', 4])/100
df.at['Agua, Kg', 4] = (df.at['Masa, Kg', 4] * df.at['Agua, %', 4])/100
df.at['Sólidos, Kg', 4] = (df.at['Masa, Kg', 4] * df.at['Sólidos, %', 4])/100