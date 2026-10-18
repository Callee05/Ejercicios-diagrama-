def calcular_gastos_envio(importe, peso):
    # 1. Evaluamos si el importe es de 50 euros o más
    if importe >= 50:
        envio = 0.0
    # 2. Si no es gratis, evaluamos el peso
    elif peso > 5:
        envio = 9.95
    # 3. En caso contrario (pesa 5 kg o menos)
    else:
        envio = 4.95
        
    # 4. Cálculo que se hace siempre
    total_pagar = importe + envio
    
    # Devolvemos los dos resultados de salida
    return envio, total_pagar

gastos, total = calcular_gastos_envio(50, 1)

print(f"Gastos de envío: {gastos} €")
print(f"Total a pagar: {total} €")
