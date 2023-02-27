from generadorPacientes import *
from ordenamientos import *


def crearDummis(cantidad):
    try:
        if cantidad > 0:
            lista = []
            for item in range(cantidad):
                lista.append((Paciente()))
            return lista
    except:
        return None

def verLista(lista):
    i = 1
    for item in lista:
        print(f'({i}) {item}')
        i += 1
        
if __name__ == '__main__':
    datos = crearDummis(int(input('Cuantos datos? ')))
    verLista(datos)
    print("="*20)
    datosOrd = quickSort(datos)
    verLista(datosOrd)
