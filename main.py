# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import *


from funciones import *

#Primer paso leer el archivo de articulos eligir su llave hacia una lista de [W,I]
#dicc={'1':[3,4]}

def main():
    num=raw_input("Ingrese el numero de cromosomas:\n")
    caja_peso_max=raw_input("Peso Maximo de la Caja:\n")
    all=LeerArticulos() #obtener la tabla de articulos
    #obtener el tamaño de toda la lista de articulos. porque de ese tamaño será nuestro cromosoma.
    #cromosoma=[1,0,0,0,0,1,0,1......all]
    #Generar una poblacion aleatoria.
    primeros=GenerarAleatoria(all,int(num))

    #Despues de obtener la primer generacion empieza el ciclo.
    num_rep=raw_input("Ingrese el numero de repeticiones:\n")
    c=1
    while c!=num_rep:
        #1.-Evaluar la función.
        funcion_evaluada=EvaluarFX(primeros,all)
        for i in funcion_evaluada:
            print i

        print "Siguiente Paso Penalizar"
        funcion_penalizada=Penalizar(funcion_evaluada,caja_peso_max)

        for x in funcion_penalizada:
            print x


        suma = SumatoriaFX(funcion_penalizada)
        print "Siguiente Paso Probabilidad de ser elegidos..."
        print "peso, importancia, penalizacion,probabilidad"
        proba=Probabilidad(funcion_penalizada,suma)
        for r in proba:
            print r
        opciones_disponibles=Ruleta(proba)
        print "peso, importancia, penalizacion,probabilidad"
        for h in opciones_disponibles:
            print h
        print "procede a seleccionar al azar algunos sin importar que se repitan."
        padres,hijos=SeleccionParejas(opciones_disponibles,num)
        print padres
        print hijos
        raw_input("Espera")

        c=c+1 #fin de ciclo.



    print len(all)



main()