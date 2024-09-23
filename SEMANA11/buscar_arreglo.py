# Se crea la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamar a la función
monto1 = 20000  # Primer monto total de compra
descuento1 = calcular_descuento(monto1)  # valor predeterminado del 10%
print(f"Descuento de la primera compra: {descuento1}")
# segundo descuento
monto2 = 30000  # Segundo monto total de compra
porcentaje_descuento2 = 10  # Porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
print(f"Descuento de la segunda compra: {descuento2}")



