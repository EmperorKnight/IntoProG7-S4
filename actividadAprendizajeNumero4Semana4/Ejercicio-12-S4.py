# El dueño de una tienda compra un artículo a un precio determinado. Obtener el precio
# en que lo debe vender para obtener una ganancia del 30%.

precio_articulo = float(input(f" \nIntroduzca el precio del articulo comprado \n-> "))

precio_venta = precio_articulo + (precio_articulo * 0.3)

print(f" \nEl precio a vender el articulo comprado es de C${precio_venta:,}\n ")