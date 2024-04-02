print("\nMasas en Kg (Operación 6):")
df.at["Almidón, Kg", 6] = round((df.at["Almidón, Kg", 5]), 2)
df.at["Agua, Kg", 6] = round(
    (
        df.at["Agua, %", 6]
        * (df.at["Almidón, Kg", 5] + df.at["Sólidos, Kg", 5])
        / (100 - df.at["Agua, %", 6])
    ),
    2,
)
df.at["Masa, Kg", 6] = round((df.at["Almidón, Kg", 6] + df.at["Agua, Kg", 6] + df.at["Sólidos, Kg", 6]), 2)
df.at["Sólidos, Kg", 6] = round(((df.at["Masa, Kg", 5] * df.at["Sólidos, %", 5]) / 100), 2)
df.at["Almidón, %", 6] = round(((df.at["Almidón, Kg", 6] / df.at["Masa, Kg", 6]) * 100), 2)
df.at["Sólidos, %", 6] = round(((df.at["Sólidos, Kg", 6] / df.at["Masa, Kg", 6]) * 100), 2)
print(df)