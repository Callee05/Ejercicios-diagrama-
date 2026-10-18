stock = int(input("Introduce el stock inicial: "))
pedidos = 0

# 2. Bucle para los 7 días de la semana (del 1 al 7)
for dia in range(1, 8):
    ventas_dia = int(input(f"Introduce las ventas del día {dia}: "))
    
    # Restamos las ventas del día al stock actual
    stock = stock - ventas_dia
    print(f"Stock restante después del día {dia}: {stock} unidades")
    # Decisión: ¿Quedan menos de 10 unidades?
    if stock < 10:
        print(f"Reponer - Día {dia}")
        stock = stock + 50
        pedidos = pedidos + 1

# 3. Resultados finales al terminar la semana (fuera del bucle)
print("--- RESUMEN SEMANAL ---")
print(f"Stock final: {stock} unidades")
print(f"Total de pedidos realizados: {pedidos}")