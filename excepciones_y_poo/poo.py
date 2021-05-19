
#Para definir una clase
class Perro:
    #para definir atributos de clases que son las comunes a todos los objetos
    especie = "Canis Lupus Familiaris" #De esta forma defino que todos los objetos que cree van a ser del tipo caniche

    #constructor, define el estado inicial, y le asigna las propiedades a un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #metodos son compartidos todas las instancias
    """def descricion(self):
        return f"{self.nombre} tiene {self.edad} años"
    """
    
    def ladrar (self, sonido):
        return f"{self.nombre} hace este sonido: {sonido}"

    #STR el metodo str lo que hace es hacer mas descriptiva la clase
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

#herencia
class DogoArgentino(Perro):#De esta forma la clase DogoArgentino hereda todo lo que esta definido en la clase perro en la clase DogoArgenitno ahora
    raza = "Dogo Argentino" #Esta es una propiedad de esta clase que es disitnta a las que ya hereda de perro

class Alumno:
    pass

"""class Vehiculo:
    def __init__(self, nombre, velocidad_maxima, kilometraje):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Colectivo(Vehiculo):
    pass

Colectivo_escolar = Colectivo("Mercedez Benz 1114 Escolar", 12, 50)

print(isinstance(Colectivo_escolar, Vehiculo))"""