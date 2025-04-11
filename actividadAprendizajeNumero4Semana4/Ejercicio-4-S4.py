# Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el
# nombre del producto y precio final luego de aplicar el descuento.

iniciador = 1
iniciador2 = 1

print(" ")
nombre_producto = str(input(f"Introduzca el nombre del producto \n-> "))
precio_producto = float(input(f"Introduzca el precio del producto \n-> "))
descuento = float(input(f"Introduzca el porcentaje de descuento a aplicar \n-> "))

precio_final = (descuento/100) * precio_producto

print(" ")    
print(f"El total a pagar de {nombre_producto} con el descuento aplicado es de C${precio_final:,.2f}")
print(" ")
