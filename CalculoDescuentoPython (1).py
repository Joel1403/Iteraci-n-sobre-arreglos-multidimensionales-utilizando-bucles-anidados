# CalculoDescuentoPython.py
# Programa para calcular el descuento en compras
# Autor: [Tu Nombre]
# Fecha: [Coloca la fecha de entrega]
# Descripción:
# Este programa utiliza una función para calcular el descuento en base
# al monto total de la compra y un porcentaje de descuento (por defecto 10%).

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a aplicar en una compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento (por defecto 10%).

    Retorna:
    float: El valor del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100.0)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada: usando el porcentaje de descuento por defecto
    compra1 = 200.0
    descuento1 = calcular_descuento(compra1)
    total1 = compra1 - descuento1
    print("Compra 1:")
    print("Monto total: $%.2f" % compra1)
    print("Descuento aplicado: $%.2f" % descuento1)
    print("Monto final a pagar: $%.2f\n" % total1)

    # Segunda llamada: usando un porcentaje de descuento personalizado
    compra2 = 350.0
    descuento2 = calcular_descuento(compra2, 15)  # 15% de descuento
    total2 = compra2 - descuento2
    print("Compra 2:")
    print("Monto total: $%.2f" % compra2)
    print("Descuento aplicado: $%.2f" % descuento2)
    print("Monto final a pagar: $%.2f" % total2)
