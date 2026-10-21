Glosario = {
    "DEFENESTRAR": "Arrojar o tirar una persona o una cosa por una ventana", 
    "LOL": "una respuesta a algo gracioso", 
    "CRINGE": "algo raro o embarazoso", 
    "ROFL": "una respuesta a una broma", 
    "SHEESH": "ligera desaprobación", 
    "CREEPY": "aterrador, siniestro", 
    "AGGRO": "ponerse agresivo/enojado",
    "RAQUÍTICO": "Dicho de una cosa: Muy pequeña o escasa."
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in Glosario.keys():
    print("El significado de", word, "es:", Glosario[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("No se encontro esa palabra")

    # ¿Qué hacer si no se encuentra la palabra?
