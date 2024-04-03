# Hallar Q(kJ)
Q_kJ = []
Q_kJ.append(((tabla.at['kJ/kg', 'Glu'] * tabla.at['Flujo másico', 'Glu']) + (tabla.at['kJ/kg', 'NH3'] 
* tabla.at['Flujo másico', 'NH3'])) - (tabla.at['Flujo másico', 'Gli'] * tabla.at['kJ/kg', 'Gli']) 
- (tabla.at['Flujo másico', 'EtOH'] * tabla.at['kJ/kg', 'EtOH']) 
- (tabla.at['Flujo másico', 'SC'] * tabla.at['kJ/kg', 'SC']))
print(tabla)
print(f'\nQ(kJ) = {Q_kJ}')
