from triageClasificacion import *
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
    
def tiempoTotalPorPaciente(paciente, triage, listaPacientes):
    tiempoIngresoATriage = random.randint(60, 120) # (s) del ingreso del paciente a urgencias al triage de clasificacion esta entre 1 a 2 minutos
    # tiempoTriageAPrediagnostico = 0
    
    if ((triage == 1) or ((paciente.condicionPrioritaria == "Discapacitado") or (paciente.condicionPrioritaria == "Embarazada") or (paciente.condicionPrioritaria == "Adulto Mayor"))) :
        tiempoTriageAPrediagnostico = 0 # atencion inmediata
    elif triage == 2:
        tiempoTriageAPrediagnostico = random.randint(600, 900) # 10-15 min (en segundos)
    elif triage == 3:
        tiempoTriageAPrediagnostico = random.randint(1800, 3600) #30-60 min
    elif triage == 4:
        tiempoTriageAPrediagnostico = random.randint(3600, 7200) #60-120 min}
    else:
        tiempoTriageAPrediagnostico = random.randint(7200, 14400) # 2 a 4 horas
        
    tiempoPrediagnostico = tiemposPred[listaPacientes.index(paciente)] # 10 a 20 min
    tiempoLaboratorio = tiemposLab[listaPacientes.index(paciente)] # 10 a 30 min
    tiempoTratamiento = tiemposTratamiento[listaPacientes.index(paciente)] #10 a 40 min
    
    segundosPred = (600*tiempoPrediagnostico) + 600
    segundosLab = (1200*tiempoLaboratorio) + 600
    segundosTratamiento = (1800*tiempoTratamiento) + 600
    
    tiempoTotal = tiempoIngresoATriage + tiempoTriageAPrediagnostico + segundosPred + segundosLab + segundosTratamiento
    return tiempoIngresoATriage, tiempoTriageAPrediagnostico, tiempoTotal

