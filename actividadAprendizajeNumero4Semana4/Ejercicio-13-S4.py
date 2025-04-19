# Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra
# los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer
# la ruta en una semana cualquiera.

print(f" \nIntroduzca el tiempo obtenido en segundos, durante la semana")
tiempo_lunes = int(input(f"Lunes -> "))
tiempo_miercoles = int(input(f"Miercoles -> "))
tiempo_viernes = int(input(f"Viernes -> "))

tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes)/3

tiempo_promedio_horas = tiempo_promedio // 3600
tiempo_promedio_restante = tiempo_promedio - (tiempo_promedio_horas * 3600)
tiempo_promedio_minutos = tiempo_promedio_restante // 60
tiempo_promedio_segundos = tiempo_promedio_restante - (tiempo_promedio_minutos * 60)

print(f" \nEl tiempo promedio que recorre la ruta durante la semana es de {tiempo_promedio_horas:.0f} horas, {tiempo_promedio_minutos:.0f} minutos, {tiempo_promedio_segundos:.0f} segundos\n ")