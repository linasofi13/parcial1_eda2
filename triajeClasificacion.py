from keras.models import Sequential
from keras.layers import Dense 
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

def tiempoEtapaPrediagnostico(cantidadMedPred, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso):
    X=[[120, 90, 1, 1, 1], [50, 140, 2, 0, 0], [75, 50, 4, 0, 0], [10, 100, 3, 0, 1], [80, 30, 5, 0, 0]] # ejemplo 20 niveles de contaminacion, modelo 2014 y 4 llantas
    Y=[0,                     1,            0,             1,                  1] # 1 puede salir, 0 no puede salir
    modelo.fit(X, Y, epochs=10, batch_size=10, verbose=True) # conjunto de modelos verdades, 150 iteraciones, verbose -> presición
# evaluar
    medicion = modelo.evaluate(X,Y)
    print(f"Medicion: {medicion[1]*100}%")
    item = [cantidadMedPred, cantidadPacientes, triage, condicion, sobrepeso]
    resultado = modelo.predict([item])
    
    if condicion == 1:
        condicion == "Si"
    else:
        condicion =="No"
    
    if sobrepeso == 1:
        sobrepeso == "Si"
    else:
        sobrepeso == "No"
    print(f"Para un prediagnostico con {cantidadMedPred} medicos, {cantidadPacientes} pacientes, {triage} de triage, Condicion -> {condicion} , Sobrepeso -> {sobrepeso} , la prediccion es: {resultado}")
    resultadoNativo = resultado[0][0]
    resultadoNativo = resultadoNativo.item()
    tiemposPred.append(resultadoNativo)
    return resultado
    
def tiempoEtapaLab(cantidadMedPred, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso, cantidadBacteriologos):
    X=[[30, 30, 1, 1, 1], [15, 85, 2, 0, 0], [10, 100, 4, 0, 0], [45, 65, 3, 0, 1], [20, 20, 1, 0, 1]] # ejemplo 20 niveles de contaminacion, modelo 2014 y 4 llantas
    Y=[0,                     1,            1,             1,                  0] # 1 puede salir, 0 no puede salir
    modelo.fit(X, Y, epochs=10, batch_size=10, verbose=True) # conjunto de modelos verdades, 150 iteraciones, verbose -> presición
# evaluar
    medicion = modelo.evaluate(X,Y)
    print(f"Medicion: {medicion[1]*100}%")
    item = [cantidadBacteriologos, cantidadPacientes, cantidadPacientes, triage, condicion]
    resultado = modelo.predict([item])
    print(f"Para un examen de laboratorio con {cantidadBacteriologos} bacteriologos, {cantidadPacientes} pacientes, {triage} de triage, {condicion} -> Condicion, la prediccion es: {resultado}")
    resultadoNativo = resultado[0][0]
    resultadoNativo = resultadoNativo.item()
    tiemposLab.append(resultadoNativo)
    return resultado

def tiempoEtapaTratamiento(cantidadMedPred, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso):
    X=[[140, 100, 1, 1, 1], [60, 15, 2, 0, 0], [55, 77, 4, 0, 0], [77, 90, 3, 0, 1], [70, 10, 5, 0, 0]] # ejemplo 20 niveles de contaminacion, modelo 2014 y 4 llantas
    Y=[1,                     0,            1,             0,                  0] # 1 puede salir, 0 no puede salir
    modelo.fit(X, Y, epochs=10, batch_size=10, verbose=True) # conjunto de modelos verdades, 150 iteraciones, verbose -> presición
# evaluar
    medicion = modelo.evaluate(X,Y)
    print(f"Medicion: {medicion[1]*100}%")
    item = [cantidadMedPred, cantidadPacientes, triage, condicion, sobrepeso]
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

    print(f"Para un prediagnostico con {cantidadMedPred} medicos, {cantidadPacientes} pacientes, {triage} de triaje, Condicion -> {condicion} , Sobrepeso -> {sobrepeso} , la prediccion es: {resultado}")
    return resultado
