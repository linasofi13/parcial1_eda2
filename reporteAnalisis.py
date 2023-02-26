from triajeClasificacion import *
import random

def convertirAFormato(segundos):
    segundos = segundos % (24 * 3600) #tiempo total en segundos
    horas = segundos // 3600
    segundos  %= 3600
    minutos = segundos // 60
    segundos %= 60   
    
    return "%d:%02d:%02d" % (horas, minutos, segundos) # -- segundos
    

def tiempoPromedioPrediagnostico():
    acumulador = 0
    for tiempo in tiemposPred:
        acumulador += tiempo
    promedio = acumulador/len(tiemposPred)
    promedio = (600*promedio) + 600
    
    return promedio
    
def tiempoPromedioLab():
    acumulador = 0
    for tiempo in tiemposLab:
        acumulador += tiempo
    promedio = acumulador/len(tiemposLab)
    promedio = (1200*promedio) + 600
    return promedio

def tiempoPromedioTratamiento():
    acumulador = 0
    for tiempo in tiemposTratamiento:
        acumulador += tiempo
    promedio = acumulador/len(tiemposTratamiento)
    promedio = (1800*promedio) + 600
    return promedio
    
def tiempoTotalPorPaciente(paciente, triaje, listaPacientes):
    tiempoIngresoATriaje = random.randint(60, 120) # (s) del ingreso del paciente a urgencias al triaje de clasificacion esta entre 1 a 2 minutos
    tiempoTriajeAPrediagnostico = 0
    if triaje == 1:
        tiempoTriajeAPrediagnostico = 0 # atencion inmediata
    if triaje == 2:
        tiempoTriajeAPrediagnostico = random.randint(600, 900) # 10-15 min (en segundos)
    if triaje == 3:
        tiempoTriajeAPrediagnostico = random.randint(1800, 3600) #30-60 min
    if triaje == 4:
        tiempoTriajeAPrediagnostico = random.randint(3600, 7200) #60-120 min}
    else:
        tiempoTriajeAPrediagnostico = random.randint(7200, 14400) # 2 a 4 horas
        
    tiempoPrediagnostico = tiemposPred[listaPacientes.index(paciente)] # 10 a 20 min
    tiempoLaboratorio = tiemposLab[listaPacientes.index(paciente)] # 10 a 30 min
    tiempoTratamiento = tiemposTratamiento[listaPacientes.index(paciente)] #10 a 40 min
    
    segundosPred = (600*tiempoPrediagnostico) + 600
    segundosLab = (1200*tiempoLaboratorio) + 600
    segundosTratamiento = (1800*tiempoTratamiento) + 600
    
    tiempoTotal = tiempoIngresoATriaje + tiempoTriajeAPrediagnostico + segundosPred + segundosLab + segundosTratamiento
    return tiempoTotal


    
