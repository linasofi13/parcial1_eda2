
<h1 align="center">
  Parcial 1 - Estructuras de Datos y Algoritmos II :cherry_blossom:
  <br>
</h1>
  <br>
  </h1>
</p>
</p>



# Desarrollo del Reto :herb:
## Funcionamiento :mushroom:

El código está dividido en 8 archivos:

* [datosHospital.py](datosHospital.py) 	:computer:

  - Se encuentran los datos de los pacientes: nombres, apellidos y enfermedades que estos pueden tener. Además se clasifican las enfermedades con un respectivo nivel de triage de urgencias.

* [generadorPacientes.py](generadorPacientes.py) 	:computer:

  - Generamos los pacientes por medio de objetos, los pacientes tienen nombre, edad, estatura, peso, enfermedad, género, condición prioritaria.
  - (El género es para que una paciente pueda estar embarazada)
  - La condición prioritaria corresponde a personas que deben ser tratadas de inmediato: Adultos mayores, embarazadas y discapacitados
  - Para otorgar la condición o no, se asignan probabilidades

* [dummisPacientes.py ](dummisPacientes.py) 	:computer:

  - Creamos los pacientes de acuerdo a la cantidad indicada por el usuario
  
* [triajeClasificacion.py](triajeClasificacion.py) 	:computer:

  - En este archivo se implementa la red neuronal. Para ello se añaden 2 capas al modelo secuencial y se busca obtener valores entre 0 y 1 con 'sigmoid'
  - La red neuronal calculará los tiempos estimados para cada paciente en las etapas de Prediagóstico, Laboratorio y Tratamiento
  - Se entrena con épocas que indican la cantidad de médicos en esa etapa, la cantidad de pacientes, el número de prioridad de triage, si tiene condición prioritaria o no y si el paciente cuenta con sobrepreso o no. 
  - Siendo 0 el tiempo mínimo entre cierto rango (para la etapa de prediagnóstico son 10 minutos mínimo) y 1 el tiempo máximo entre cierto rango (para la etapa de prediagnóstico son 20 min máximo)
  - En el entrenamiento de la red neuronal para el tiempo de la etapa de tratamiento es importante resaltar que para aquellas personas con triages más urgentes el tiempo será mayor. (el tiempo de tratamiento de una persona con gripa es menor al de alguien que por ejemplo le tengan que hacer maniobras de reanimación)
  
 * [reporteTiempo.py](reporteTiempo.py) 	:computer:

  - En este archivo se realizan varias operaciones. Lo primero es asignar el triage al que corresponde el paciente de acuerdo a la enfermedad o motivo de consulta. Por ejemplo, una persona con un compromiso respiratorio (es crítico) debe ser atendido de inmediato (triage 1). Mientras que una persona con gripe normal no tiene tanta prioridad (triage 4). También se indica por medio de 0 y 1 si el paciente tiene una condición prioritaria y/o sobrepeso.
  - El análisis del tiempo se pensó de acuerdo a los días de la semana: esto quiere decir que, por ejemplo, un lunes pueden haber 200 médicos en el hospital y la distribución por etapas puede ser 100 en prediagnóstico, 70 en laboratorio y 30 en tratamiento. Estos datos son fijos y se simula que son impuestos por el hospital. 
  - Lo anterior significa que el cálculo del tiempo dentro de la red neuronal, como ya se mencionó, tendrá un factor de distribución de los médicos, y para el caso del laboratorio se tienen en cuenta la cantidad de bacteriólogos.
  - La distribución de los médicos se calcula de acuerdo a los porcentajes fijos del hospital.
  
* [reporteAnalisis.py](reporteAnalisis.py) 	:computer:

  - También se realizan varias operaciones: existe una función para convertir el formato de segundos al formato hh:mm:ss
  - Se calculan los tiempos promedios por etapa (el objetivo inicial del análisis).
  - Se convierte el valor de 0 a 1 obtenido por la red neuronal a su equivalencia en segundos. Esto se realiza mediante 3 funciones lineales que realizan la proporcionalidad de x = 0.5 de predicción a y = valor en segundos.
  - Se suman los tiempos y se obtiene el tiempo total por paciente.
  
* [menu.py](menu.py) 	:computer:

  - Es el archivo ejecutable, se encuentra el menú para inicializar el programa. Muestra los pacientes con sus respectivos tiempos por cada etapa y el tiempo promedio por etapa de todos los pacientes. Dentro de las opciones se puede seleccionar la cantidad de pacientes a generar y el día a analizar. 
  
</p>
</p>
<br>
## Output :framed_picture:
</p>
</p>
  <br>
![image](https://user-images.githubusercontent.com/103126242/221451536-1731a717-b1f8-405b-91e9-21a55534f55f.png)

<br>
- Se encuentra otro archivo llamado "ordenamientos.py" el cual puede ser utilizado para ordenar los datos
  <br>
:pushpin: Realizado por: Lina Ballesteros
  <br>
:round_pushpin: Se realizó en base al código de Edison Valencia
