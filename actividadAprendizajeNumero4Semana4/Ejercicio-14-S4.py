# En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. El presupuesto
# anual del hospital se reparte de la siguiente manera: urgencias (37%), pediatria (42%)
# traumotologia (21%).
# Obtener la cantidad de dinero que recibirá cada área para cualquier monto presupuestal.

presupuesto_anual_hospital = float(input(f" \nIntroduzca el presupuesto anual del hospital\n-> "))

presupuesto_urgencias = presupuesto_anual_hospital * (37/100)
presupuesto_pediatria = presupuesto_anual_hospital * (42/100)
presupuesto_traumatologia = presupuesto_anual_hospital * (21/100)

print(f" \nEl presupuesto para el area de urgencias es de C${presupuesto_urgencias:,}")
print(f"El presupuesto para el area de pediatria es de C${presupuesto_pediatria:,}")
print(f"El presupuesto para el area de traumatologia es de C${presupuesto_traumatologia:,} \n ")
