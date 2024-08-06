h_ev = df_final.at[1, 'Entalpía']
Q_lat = Mi_vs * h_ev

# Mostrar el calor latente
print(f'Q latente: {round(Q_lat, 9)} BTU')
