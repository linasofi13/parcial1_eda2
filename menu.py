from reporteTiempo import *
from reporteAnalisis import *
import sys

def menu():
    print("Modelo de Gestión de Tiempo y Calidad del Servicio de 2 Centros de Urgencia de la ciudad de Bello")
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
            triaje, condicion, sobrepeso = asignacionPaciente(paciente)
            reporteDia(dia, "clinica_del_norte", cantidadPacientes, pacientesLista, triaje, condicion, sobrepeso)   
        
        print("-"*60)
        print("------------------------ Pacientes ------------------------")
        verLista(pacientesLista)
        seg1 = tiempoPromedioPrediagnostico()
        seg2 = tiempoPromedioLab()
        seg3 = tiempoPromedioTratamiento()
        print(f"El tiempo promedio de {cantidadPacientes} pacientes en el prediagnostico fue de {convertirAFormato(seg1)}")
        print(f"El tiempo promedio de {cantidadPacientes} pacientes en los examenes de laboratorio fue de {convertirAFormato(seg2)}")
        print(f"El tiempo promedio de {cantidadPacientes} pacientes en el tratamiento fue de {convertirAFormato(seg3)}")
        
        print("-"*60)
        print("--------------------- El tiempo total por paciente: ------------------")
        i = 1
        for paciente in pacientesLista:
            print(f'({i}) {paciente}')
            t, c, s = asignacionPaciente(paciente)
            segTotal = tiempoTotalPorPaciente(paciente, t, pacientesLista)
            t1 = (600*tiemposPred[i-1])+600
            t2 = (1200*tiemposLab[i-1])+600
            t3 = (1800*tiemposTratamiento[i-1]+600)
            print(f"Tiempo Prediagnostico: {convertirAFormato(t1)}" )
            print(f"Tiempo Laboratorio: {convertirAFormato(t2)}" )
            print(f"Tiempo Laboratorio: {convertirAFormato(t3)}" )
            print(f"| | Tiempo Total: {convertirAFormato(segTotal)}")
            
            i += 1
        else:
            sys.exit()
            
if __name__ == '__main__':
    menu()
