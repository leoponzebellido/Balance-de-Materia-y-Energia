Vi_vs = 0.008
Ve_vs = df_final.at[1, 'Volumen']
Mi_vs = round((Vi_vs / Ve_vs), 9)

# Mostrar el resultado
print(f"Resultado: {Mi_vs} lbm")
