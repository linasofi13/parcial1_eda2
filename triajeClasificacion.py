from keras.models import Sequential
from keras.layers import Dense # usamos from para no tener que especificar en cada método el keras.algo
from dummisPacientes import *
from generadorPacientes import Paciente
from tensorflow import *
import numpy as np

tiemposPred = []
tiemposLab = []
tiemposTratamiento = []

modelo = Sequential()
modelo.add(Dense(12, input_dim=5, activation='relu')) # 12 es la cantidad de nodos internos
modelo.add(Dense(1, activation='sigmoid'))
modelo.add(Dense(1, activation='sigmoid'))
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

def tiempoEtapaPrediagnostico(cantidadMedPred, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso):
    X=[[120, 300, 1, 1, 1], [50, 140, 2, 0, 0], [75, 1000, 4, 0, 0], [10, 500, 3, 0, 1], [80, 200, 5, 0, 0]] # ejemplo 20 niveles de contaminacion, modelo 2014 y 4 llantas
    Y=[0,                     1,            0,             1,                  1] # 1 puede salir, 0 no puede salir
    modelo.fit(X, Y, epochs=30, batch_size=10, verbose=True) # conjunto de modelos verdades, 150 iteraciones, verbose -> presición
# evaluar
    medicion = modelo.evaluate(X,Y)
    print(f"Medicion: {medicion[1]*100}%")
    item = [cantidadMedPred, cantidadPacientes, triaje, condicion, sobrepeso]
    resultado = modelo.predict([item])
    
    if condicion == 1:
        condicion == "Si"
    else:
        condicion =="No"
    
    if sobrepeso == 1:
        sobrepeso == "Si"
    else:
        sobrepeso == "No"
    print(f"Para un prediagnostico con {cantidadMedPred} medicos, {cantidadPacientes} pacientes, {triaje} de triaje, Condicion -> {condicion} , Sobrepeso -> {sobrepeso} , la prediccion es: {resultado}")
    resultadoNativo = resultado[0][0]
    resultadoNativo = resultadoNativo.item()
    tiemposPred.append(resultadoNativo)
    return resultado
    
def tiempoEtapaLab(cantidadMedPred, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso, cantidadBacteriologos):
    X=[[30, 250, 1, 1, 1], [15, 600, 2, 0, 0], [10, 450, 4, 0, 0], [45, 100, 3, 0, 1], [20, 150, 1, 0, 1]] # ejemplo 20 niveles de contaminacion, modelo 2014 y 4 llantas
    Y=[0,                     1,            1,             1,                  0] # 1 puede salir, 0 no puede salir
    modelo.fit(X, Y, epochs=30, batch_size=10, verbose=True) # conjunto de modelos verdades, 150 iteraciones, verbose -> presición
# evaluar
    medicion = modelo.evaluate(X,Y)
    print(f"Medicion: {medicion[1]*100}%")
    item = [cantidadBacteriologos, cantidadPacientes, cantidadPacientes, triaje, condicion]
    resultado = modelo.predict([item])
    print(f"Para un examen de laboratorio con {cantidadBacteriologos} bacteriologos, {cantidadPacientes} pacientes, {triaje} de triaje, {condicion} -> Condicion, la prediccion es: {resultado}")
    resultadoNativo = resultado[0][0]
    resultadoNativo = resultadoNativo.item()
    tiemposLab.append(resultadoNativo)
    return resultado

def tiempoEtapaTratamiento(cantidadMedPred, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso):
    X=[[140, 200, 1, 1, 1], [60, 130, 2, 0, 0], [55, 900, 4, 0, 0], [77, 555, 3, 0, 1], [70, 300, 5, 0, 0]] # ejemplo 20 niveles de contaminacion, modelo 2014 y 4 llantas
    Y=[1,                     0,            1,             0,                  0] # 1 puede salir, 0 no puede salir
    modelo.fit(X, Y, epochs=30, batch_size=10, verbose=True) # conjunto de modelos verdades, 150 iteraciones, verbose -> presición
# evaluar
    medicion = modelo.evaluate(X,Y)
    print(f"Medicion: {medicion[1]*100}%")
    item = [cantidadMedPred, cantidadPacientes, triaje, condicion, sobrepeso]
    resultado = modelo.predict([item])
    
    if condicion == 1:
        condicion = "Si"
    else:
        condicion ="No"
    
    if sobrepeso == 1:
        sobrepeso = "Si"
    else:
        sobrepeso = "No"
    resultadoNativo = resultado[0][0]
    resultadoNativo = resultadoNativo.item()
    tiemposTratamiento.append(resultadoNativo)
    print(type(resultadoNativo))

    print(f"Para un prediagnostico con {cantidadMedPred} medicos, {cantidadPacientes} pacientes, {triaje} de triaje, Condicion -> {condicion} , Sobrepeso -> {sobrepeso} , la prediccion es: {resultado}")
    return resultado

