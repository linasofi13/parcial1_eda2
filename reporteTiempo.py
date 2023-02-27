from triageClasificacion import *

cantidadMedicos = [200, 170, 185, 75, 100, 160, 90]

porcentajesXDia = [[0.65, 0.15, 0.20], [0.70, 0.20, 0.10], [0.40, 0.25, 0.35], [0.30, 0.30, 0.40], [0.80, 0.10, 0.10], [0.50, 0.25, 0.25], [0.60, 0.05, 0.35] ]

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

def asignacionPaciente(paciente):
    triage = 0
    condicion = 0
    sobrepeso = 0
    if paciente.enfermedad in triage1:
        triage = 1
    elif paciente.enfermedad in triage2:
        triage = 2
    elif paciente.enfermedad in triage3:
        triage = 3
    elif paciente.enfermedad in triage4:
        triage = 4
    elif paciente.enfermedad in triage5:
        triage = 5
        
    if paciente.condicionPrioritaria != "Ninguna":
        condicion = 1
    else:
        condicion = 0
            
    if paciente.peso >= 140:
            sobrepeso = 1
    else: 
        sobrepeso = 0
            
    return triage, condicion, sobrepeso

def calcularMedicosEtapa(cantidadMedicos, porcentajesXDia):
    cantidadMedPred = int(((porcentajesXDia[0]*100) * cantidadMedicos)/100)
    cantidadMedLab = int(((porcentajesXDia[1]*100) * cantidadMedicos)/100)
    cantidadMedTrat = int(((porcentajesXDia[2]*100) * cantidadMedicos)/100)
    
    return cantidadMedPred, cantidadMedLab, cantidadMedTrat
        
def generarCantidadMedicosXEtapa(cantidadMedicos, cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia, triage, condicion, sobrepeso, cantidadBacteriologos):
    cantidadMedPred, cantidadMedLab, cantidadMedTrat = calcularMedicosEtapa(cantidadMedicos, porcentajesXDia)
    # tiempoPre = random.randint(600, 1200) # un medico podria demorarse entre 10 y 20 minutos en generar el diagnóstico
    # tiempoLab = random.randint(600, 1800) # un medico podria demorarse entre 10 y 30 minutos haciendo un examen de laboratoio
    return tiempoEtapaPrediagnostico(cantidadMedPred, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso), tiempoEtapaLab(cantidadMedLab, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso, cantidadBacteriologos), tiempoEtapaTratamiento(cantidadMedTrat, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso)# el tiempo del tratamiento depende de la enfermedad

def reporteDia(dia, centroDeUrgencias, cantidadPacientes, pacientesLista, triage, condicion, sobrepeso):
    if centroDeUrgencias == "clinica_del_norte":
        if dia == 1: # lunes, cuenta con 200 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[0], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[0], triage, condicion, sobrepeso, 20) # el ultimo significa cantidad de bacteriólogos
        if dia == 2: # martes, cuenta con 170 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[1], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[1], triage, condicion, sobrepeso, 10) # TODO cambiar dias jsjs
        if dia == 3: # miercoles, cuenta con 185 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[2], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[2], triage, condicion, sobrepeso, 5)
        if dia == 4: # jueves, cuenta con 75 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[3], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[3], triage, condicion, sobrepeso, 40)
        if dia == 5: # viernes, cuenta con 100 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[4], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[4], triage, condicion, sobrepeso, 30)
        if dia == 6: # sabado, cuenta con 160 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[5], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[5], triage, condicion, sobrepeso, 18)
        if dia == 7: # domingo, cuenta con 90 medicos
            generarCantidadMedicosXEtapa(cantidadMedicos[6], cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajesXDia[6], triage, condicion, sobrepeso, 30)
    
