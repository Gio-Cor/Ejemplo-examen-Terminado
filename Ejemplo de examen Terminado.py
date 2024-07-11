import random
import csv

alumnos = ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Rodríguez', 
           'Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández']

creditos_alumnos={}

def Asignacióndecreditos(): 
    global creditos_alumnos
    creditos_alumnos={alumno :0 for alumno in alumnos}
    for alumno in alumnos:
        creditos=random.randint(50,200)
        creditos_alumnos[alumno]=creditos
    print(creditos_alumnos)
    print('Creditos Asignados')
    print('-'*20)

def Clasificacióndecreditos():
    ''' Clasificación de Créditos:
o Desarrolla una función que clasifique los créditos de los estudiantes 
en los siguientes rangos:
▪ Créditos menores a $100
▪ Créditos entre $100 y $150
▪ Créditos mayores a $150
o Muestra la cantidad de estudiantes en cada rango y sus detalles.
'''
    entre100_150={}
    mayor_150={}
    menorque100={}
    
    print('='*50)
    if len(creditos_alumnos)>0:
        for alumno,credito in creditos_alumnos.items():
            if credito<100:
                menorque100[alumno]=credito
            if credito>=100 and credito<=150:
                entre100_150[alumno]=credito
            if credito>150:
                mayor_150[alumno]=credito
        
        print('Menores a 100',menorque100)
        print('-------------------------------------')
        print('Mayores a 100 hasta 150',entre100_150)
        print('-------------------------------------')
        print('Mayores a 150',mayor_150)
        print('='*20)
        print('Menores que 100',len(menorque100))
        print('-------------------------------------')
        print('Entre 100 y 150',len(entre100_150))
        print('-------------------------------------')
        print('Mayores que 150',len(mayor_150))

        print('-------------------------------------')
    else:
        print('No hay creditos asignados')
    
def CálculodeEstadísticasdeCréditos():
    '''o Implementa una función para calcular las siguientes estadísticas 
    básicas de los créditos de los estudiantes:
    ▪ Máximo crédito
    ▪ Mínimo crédito
    ▪ Promedio de créditos'''
    if len(creditos_alumnos)>0:
        creditos=list(creditos_alumnos.values())
        print('El credito maximo es',max(creditos))
        print('-------------------------------------')
        print('El credito minimo es',min(creditos))
        print('-------------------------------------')
        print('Promedio',sum(creditos)/len(creditos))
        print('-------------------------------------')
        print('-------------------------------------')
    else:
        print('No hay creditos asignados')   

def guardararchivo():
    if len(creditos_alumnos)!=0:
        with open('Archivito.csv','w',newline='') as archivo:
            escritor=csv.writer(archivo,delimiter=',')
            for alumno,credito in creditos_alumnos.items():
                escritor.writerow([alumno,credito])
        print('Archivo creado con exito')
    else:
        print('No hay creditos asignados') 



def menu():
    
    while True:
        print('-----Menú-----')
        print('1.-Asignar Creditos')
        print('2.-Clasificación')
        print('3.-Calculo de estadisticas')
        print('4.-Guardar archivo en csv')
        print('5.-Salir')
        try:
            print('-'*50)
            opc=int(input('Ingresa tu elección'))
            if opc>=1 and opc<=5:
                if opc==1:
                    Asignacióndecreditos()
                if opc==2:
                    Clasificacióndecreditos()
                if opc==3:
                    CálculodeEstadísticasdeCréditos()                 
                if opc==4:
                    guardararchivo()
                if opc==5:
                    break
            else:
                print('Respuesta fuera de rango')
        except:     
            print('Debe ser un numero')
menu()
