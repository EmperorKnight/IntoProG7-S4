# Solicita el precio de 3 productos y muestra:
# Subtotal
# IVA (15%)
# Total a pagar

iniciador = 1
IVA = (15/100)

precio_producto = float(input(f" \nIntroduzca el precio de tres productos \n-> "))

while iniciador < 3:
    precio_producto1 = float(input("-> "))
    precio_producto = precio_producto1 + precio_producto
    iniciador = iniciador + 1

subTotal = precio_producto
total = (subTotal * IVA) + subTotal

print(f" \nEl subtotal es de C${subTotal:,} \nEl IVA aplicado es del 15% \nEl total a pagar es de C${total:,} \n ")
