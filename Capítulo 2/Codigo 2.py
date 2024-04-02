# Definir Variables:
AHE = float(input("¿Cuántos moles de AHE se desean obtener?: "))
P_W_AHE = float(input("Ingrese el porcentaje de Vapor de agua: "))
P_Ox_AHE = float(input("Ingrese el porcentaje de Oxígeno: "))

# Operamos:
W = (P_W_AHE * AHE) / 100
Ox = (P_Ox_AHE - (AHE - W) * 0.21) / 0.79
AS = (P_Ox_AHE - Ox) / 0.21

# Resultados:
print(f"\nPara obtener {round(AHE, 2)} moles de AHE con {round(P_W_AHE, 2)}% de vapor de agua ")
print(f"y {round(P_Ox_AHE, 2)}% de oxígeno,")
print(f"se necesitan {round(AS, 2)} moles de aire seco y {round(Ox, 2)} moles de oxígeno. ")