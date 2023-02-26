# algoritmo merge sort 
# # # archivo opcional
def mergeSort(datos):
    if len(datos) <= 1:
        return datos
    if len(datos) == 2:
        return sorted(datos)

    mitadDatos = len(datos)//2
    return merge(mergeSort(datos[:mitadDatos]), mergeSort(datos[mitadDatos:]))

def merge(datosA, datosB):
    p1 = 0
    p2 = 0
    resultado = []
    
    while(p1 < len(datosA) and p2 < len(datosB)):
        if datosA[p1] < datosB[p2]:
            resultado.append(datosA[p1])
            p1 +=1
        else:
            resultado.append(datosB[p2])
            p2 += 1
            
    resultado += datosA[p1:] + datosB[p2:]
    return resultado

def quickSort(datos):
    if len(datos)<=1:
        return datos
    #buscar pivote
    pivote= datos[len(datos)//2]
    datosMenores=[item for item in datos if item < pivote] # los menores y mayores podrian no estar odenados, los iguales si estan ordenados
    datosIguales=[item for item in datos if item == pivote]
    datosMayores=[item for item in datos if item >pivote]
    return quickSort(datosMenores)+datosIguales+quickSort(datosMayores)

def bubbleSort(datos):
    n = len(datos)
    for i in range(n - 1) :
        flag = 0
        for j in range(n - 1) :     
            if datos[j] > datos[j + 1] : 
                temporal = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = temporal
                flag = 1
        if flag == 0:
            break

    return datos




