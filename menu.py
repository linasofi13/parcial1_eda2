from reporteTiempo import *
from reporteAnalisis import *
import sys

def menu():
    print("Modelo de Prediccion de 1 Centro de Urgencia de la ciudad de Bello")
    print("Seleccione una opción para continuar:")
    print("1 | Consultar Centro de Urgencia Clinica del Norte")
    print("2 | Salir ")
    opcion_1 = int(input())
    if opcion_1 == 1:
        print("Reporte de Gestión de Tiempo para Clinica del Norte:")
        print("Ingrese la cantidad de Pacientes: ")
        cantidadPacientes = int(input())
        print("Ingrese el dia a analizar: ")
        print(" 1 | Lunes")
        print(" 2 | Martes")
        print(" 3 | Miercoles")
        print(" 4 | Jueves")
        print(" 5 | Viernes")
        print(" 6 | Sabado")
        print(" 7 | Domingo")
        dia = int(input())
        pacientesLista = crearDummis(cantidadPacientes)
        for paciente in pacientesLista:
            triage, condicion, sobrepeso = asignacionPaciente(paciente)
            reporteDia(dia, "clinica_del_norte", cantidadPacientes, pacientesLista, triage, condicion, sobrepeso)   
        
        print("-"*60)
        print("------------------------ Pacientes ------------------------")
        verLista(pacientesLista)
        seg1 = tiempoPromedioPrediagnostico()
        seg2 = tiempoPromedioLab()
        seg3 = tiempoPromedioTratamiento()
        
        print("-"*60)
        print("--------------------- El tiempo total por paciente: ------------------")
        i = 1
        for paciente in pacientesLista:
            print(f'({i}) {paciente}')
            t, c, s = asignacionPaciente(paciente)
            t1_1, t2_2, segTotal = tiempoTotalPorPaciente(paciente, t, pacientesLista)
            t1 = (600*tiemposPred[i-1])+600
            t2 = (1200*tiemposLab[i-1])+600
            t3 = (1800*tiemposTratamiento[i-1]+600)
            print("*"*60)
            print(f"Tiempo Ingreso: {convertirAFormato(t1_1)}" )
            print(f"Tiempo Triaje: {convertirAFormato(t2_2)}" )
            print(f"Tiempo Prediagnostico: {convertirAFormato(t1)}" )
            print(f"Tiempo Laboratorio: {convertirAFormato(t2)}" )
            print(f"Tiempo Tratamiento: {convertirAFormato(t3)}" )
            print(f"| **** | Tiempo Total: {convertirAFormato(segTotal)} | **** | ")
            print("*"*60)
            
            i += 1
        medPred, medLab, MedTrat = calcularMedicosEtapa(cantidadMedicos[dia-1], porcentajesXDia[dia-1])
        print(f"El tiempo promedio de {cantidadPacientes} pacientes, con {cantidadMedicos[dia-1]} medicos en total, con {medPred} medicos la etapa de prediagnostico, en el dia {dias[dia-1]}, fue de {convertirAFormato(seg1)}")
        print(f"El tiempo promedio de {cantidadPacientes} pacientes, con {cantidadMedicos[dia-1]} medicos en total, con {medLab} medicos la etapa de laboratorio, en el dia {dias[dia-1]}, fue de {convertirAFormato(seg2)}")
        print(f"El tiempo promedio de {cantidadPacientes} pacientes, con {cantidadMedicos[dia-1]} medicos en total, con {MedTrat} medicos la etapa de Tratamiento, en el dia {dias[dia-1]}, fue de {convertirAFormato(seg3)}")
        
        registro = []
        registro.append(('Prediagnostico', minutos(seg1))) # registro[i] = [(metodo, nDatos, tiempo), --]
        registro.append(('Laboratorio', minutos(seg2)))
        registro.append(('Tratamiento', minutos(seg3)))
        graficar(registro)
        # print(registro)
    else:
        sys.exit() # [(n, n), (n, n), (n, n)] arreglo[0][0] arreglo [1][0]
            
if __name__ == '__main__':
    menu()
