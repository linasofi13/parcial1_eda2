from datosHospital import * # importamos los datos dummis
import random # libreria random, escoger nombres al azar

class Paciente(): # creamos Pacientes con diferentes atributos
    def __init__(self): # nos encontramos dentro del objeto
        self.nombre = darNombre()
        self.peso = darPeso(40.0, 180.0)
        self.estatura = darEstatura(1.45, 2.10) 
        self.enfermedad = darEnfermedad(self)
        self.genero = darGenero(self)
        self.edad = darEdad(0, 95)
        self.condicionPrioritaria = darCondicionPrioritaria(self)
        self.tiempo1 = darTiempo1(300, 2400) # tiempo en segundos
        self.tiempo2 = darTiempo2(600, 1200)
        self.tiempo3 = darTiempo3(30, 90)
        
    def __str__(self): # sobreescribimos el método
        return f'Paciente: [{self.nombre} | {self.genero} | {self.edad} anios  | {self.estatura:.2f} m | {self.peso:.2f} kg | Enfermedad o Motivo de Consulta: {self.enfermedad} | Condicion Prioritaria: {self.condicionPrioritaria}]'
    
    # metodos de comparacion para utilizar el ordenamiento de los datos
    
    def __gt__(self, otroObj): # great than, mayor que -> el operador que nos compara entre los objetos
        return self.edad > otroObj.edad # boolean
    
    def __lt__(self, otroObj): # less than , mas metodos que comparan entre atributos de objetos
        return self.edad < otroObj.edad 
    
    def __eq__(self, otroObj): #  iguales
        return self.edad == otroObj.edad
    
def darGenero(self): # para asignarle a una mujer un embarazo
    nombreReverse = str(self.nombre[::-1])
    k = " "
    n = 2
    nombreSubstring = nombreReverse.split(k, n)[-1]
    nombreReverse = nombreSubstring[::-1] # para tener solo el string del nombre con el self 
    if nombreReverse in listaNombresMujeres:
        return "Mujer"
    else:
        return "Hombre"
    
def darNombre():
    pick1 = random.choice(listaNombresHombres)
    pick2 = random.choice(listaNombresMujeres)
    finalPick = [pick1, pick2]
    nombre = random.choice(finalPick) # escoge nombre random entre hombres y mujeres
    apellido1 = random.choice(listaApellidos)
    apellido2 = random.choice(listaApellidos)
    return f'{nombre} {apellido1} {apellido2}'

    
def darCondicionPrioritaria(self):
    numAleatorio = random.randint(1, 100) # inclusivo
    if self.edad >= 60:
        return "Adulto Mayor" # segun minsalud
    if self.genero == "Mujer":
        if ((numAleatorio%10 == 0) or (numAleatorio%7 == 0)): # probabilidad del 23%
            return "Embarazada"
    if ((numAleatorio%10 == 0) or (numAleatorio%7 == 0) or (numAleatorio%8 == 0)): # probabilidad del 35%
        return "Discapacitado"
    else:
        return "Ninguna"
# damos limites reales a los datos  

def darEdad(limiteInf, limiteSup):
    return random.randint(limiteInf, limiteSup)
 
def darPeso(limiteInf, limiteSup):
    return random.uniform(limiteInf, limiteSup) 

def darEstatura(limiteInf, limiteSup):
    return random.uniform(limiteInf, limiteSup)    

def darTiempo1(limiteInf, limiteSup): 
    return random.randint(limiteInf, limiteSup)
        
def darTiempo2(limiteInf, limiteSup):
    return random.uniform(limiteInf, limiteSup)

def darTiempo3(limiteInf, limiteSup):
    return random.uniform(limiteInf, limiteSup)   


def darEnfermedad(self):
    enfermedad = random.choice(listaEnfermedades)
    return f'{enfermedad}'

def crearDatos(cantidad):
    try:
        if cantidad > 0:
            lista = []
            for item in range(cantidad):
                lista.append((Paciente()))
            return lista
    except:
        return None

#main

if __name__ == '__main__':

    obj1 = Paciente()
    obj2 = Paciente()
    if obj1 > obj2:
        print("obj1 > obj2") # podemos usar operadores directamente al haber definido los metodos
    elif obj1 < obj2:
        print("obj2 > obj1") # estamos comparando edades de las personas
    else:
        print("obj1 = obj2")
    print(f'Obj1 ->  {obj1}')
    print(f'Obj2 -> {obj2}')
