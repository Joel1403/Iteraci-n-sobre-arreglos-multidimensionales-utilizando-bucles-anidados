
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a aplicar en una compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento (por defecto 10%).

    Retorna:
    float: El valor del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada: usando el porcentaje de descuento por defecto
    compra1 = 200.0
    descuento1 = calcular_descuento(compra1)
    total1 = compra1 - descuento1
    print("Compra 1:")
    print(f"Monto total: ${compra1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${total1:.2f}\n")

    # Segunda llamada: usando un porcentaje de descuento personalizado
    compra2 = 350.0
    descuento2 = calcular_descuento(compra2, 15)  # 15% de descuento
    total2 = compra2 - descuento2
    print("Compra 2:")
    print(f"Monto total: ${compra2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${total2:.2f}")
