from triajeClasificacion import *

def asignacionPaciente(paciente):
    triaje = 0
    condicion = 0
    sobrepeso = 0
    if paciente.enfermedad in triaje1:
        triaje = 1
    elif paciente.enfermedad in triaje2:
        triaje = 2
    elif paciente.enfermedad in triaje3:
        triaje = 3
    elif paciente.enfermedad in triaje4:
        triaje = 4
    elif paciente.enfermedad in triaje5:
        triaje = 5
        
    if paciente.condicionPrioritaria != "Ninguna":
        condicion = 1
    else:
        condicion = 0
            
    if paciente.peso >= 140:
            sobrepeso = 1
    else: 
        sobrepeso = 0
            
    return triaje, condicion, sobrepeso
            
        
def generarCantidadMedicosXEtapa(cantidadMedicos, cantidadPacientes, pacientesLista, centroDeUrgencias, porcentajeMedPred, porcentajeMedLab, porcentajeTratamiento, triaje, condicion, sobrepeso, cantidadBacteriologos):
    cantidadMedPred = int(((porcentajeMedPred*100) * cantidadMedicos)/100)
    cantidadMedLab = int(((porcentajeMedLab*100) * cantidadMedicos)/100)
    cantidadMedTrat = int(((porcentajeTratamiento*100) * cantidadMedicos)/100)

    # tiempoPre = random.randint(600, 1200) # un medico podria demorarse entre 10 y 20 minutos en generar el diagnóstico
    # tiempoLab = random.randint(600, 1800) # un medico podria demorarse entre 10 y 30 minutos haciendo un examen de laboratoio
    return tiempoEtapaPrediagnostico(cantidadMedPred, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso), tiempoEtapaLab(cantidadMedLab, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso, cantidadBacteriologos), tiempoEtapaTratamiento(cantidadMedTrat, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso)# el tiempo del tratamiento depende de la enfermedad

def reporteDia(dia, centroDeUrgencias, cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso):
    if centroDeUrgencias == "clinica_del_norte":
        if dia == 1: # lunes, cuenta con 200 medicos
            generarCantidadMedicosXEtapa(200, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.65, 0.15, 0.20, triaje, condicion, sobrepeso, 20) # el ultimo significa cantidad de bacteriólogos
        if dia == 2: # martes, cuenta con 170 medicos
            generarCantidadMedicosXEtapa(170, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.70, 0.20, 0.10, triaje, condicion, sobrepeso, 10) # TODO cambiar dias jsjs
        if dia == 3: # miercoles, cuenta con 185 medicos
            generarCantidadMedicosXEtapa(185, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.40, 0.25, 0.35, triaje, condicion, sobrepeso, 5)
        if dia == 4: # jueves, cuenta con 75 medicos
            generarCantidadMedicosXEtapa(75, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.30, 0.30, 0.40, triaje, condicion, sobrepeso, 40)
        if dia == 5: # viernes, cuenta con 100 medicos
            generarCantidadMedicosXEtapa(100, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.80, 0.10, 0.10, triaje, condicion, sobrepeso, 30)
        if dia == 6: # sabado, cuenta con 160 medicos
            generarCantidadMedicosXEtapa(160, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.50, 0.25, 0.25, triaje, condicion, sobrepeso, 18)
        if dia == 7: # domingo, cuenta con 90 medicos
            generarCantidadMedicosXEtapa(90, cantidadPacientes, pacientesLista, centroDeUrgencias, 0.60, 0.05, 0.35, triaje, condicion, sobrepeso, 30)
    
