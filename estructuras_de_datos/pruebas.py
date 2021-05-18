"""ejemploSet = {"Amarillo", "Naranja", "Negro"}
ejemploList = ["Azul", "Verde", "Rojo"]

ejemploSet.update(ejemploList )

print(ejemploSet)
conjunto1 = {10, 20, 30, 40, 50}
conjunto2 = {30, 40, 50, 60, 70}
print(conjunto1.intersection(conjunto2))

conjunto1 = {10, 20, 30}
conjunto2 = {20, 40, 50}
conjunto1.difference_update(conjunto2)
print(conjunto1)

ejemploDiccionario = { 
   "clase":{ 
      "estudiante":{ 
         "nombre":"Marcos",
         "examenes":{ 
            "matematica":70,
            "geografia":80
         }
      }
   }
}
print(ejemploDiccionario['clase']['estudiante']['examenes']['matematica'])
"""
import datetime

# 2020-03-22 10:00:00
fecha_dada = datetime(2020, 3, 22, 10, 00, 00)
fecha_limite = fecha_dada + timedelta(days=7, hours=12)