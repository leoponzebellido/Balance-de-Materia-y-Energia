print('\nMasas en Kg (Operación 7):')
df.at['Agua, Kg', 7] = round((df.at['Agua, Kg', 5] - df.at['Agua, Kg', 6]), 2)
df.at['Masa, Kg', 7] = df.at['Agua, Kg', 7]
print(df)