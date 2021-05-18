import sys #importamos la libreria que trabaja con exepciones

try: #es vital identar sino no funciona y muestra error
    numero1 = int(input("Ingrese el primero numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
except ValueError:#si se genera este tipo de error entonces ejecuta
    print("Error. Valor no valido")
    sys.exit(1)

try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error no se puede dividir por cero")
    sys.exit(1)
else:
    print("Resultado exitoso")

print(f"El resultado de la divsisión de {numero1} dividido {numero2} es = {resultado}")#La F lo que permite es mesclar texto que sale impreso con variables
