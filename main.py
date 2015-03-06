# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import *
from Cruzar import *

from funciones import *
from mutacion import *

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
    best=[0, 1, 0, 0, 1, 0, 1, 1, 1, 1,1000, 1000,1000,0]
    while c!=int(num_rep):
        #1.-Evaluar la función.
        funcion_evaluada=EvaluarFX(primeros,all)
        print "Funcion Evaluada : Costo , Importancia"
        for i in funcion_evaluada:
            print i

        print "Siguiente Paso Penalizar"

        funcion_penalizada=Penalizar(funcion_evaluada,caja_peso_max)
        print "Funcion Evaluada : Costo , Importancia, Penalizacion"
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
        print "Los hijos son:"
        for x in hijos:
            print x
        #comprobar el mejor.
        best=SelectBest(hijos,best)
        print "El mejor hasta el momento es:"
        print best
        #Proces de cruzamiento
        nuevos=[]
        for x in hijos:
            nuevos.append(x[0:(len(all))])
        print nuevos
        cruzados=Cruzar(nuevos)
        print "Proceso de mutacion"
        primeros=Mutar(cruzados,num)
        c=c+1 #fin de ciclo.
    print "Acabo en numero de generacion= " + str(c)
    print("El resultado final es: \n")
    print "N°  \tPeso   \tImportancia"
    for x in range(0,len(best)):
        if best[x]==1:
            articulo=all[x+1]
            pes=articulo[0]
            impo = articulo[1]
            print ""+str(x+1)+"\t\t"+str(pes)+"\t\t\t"+str(impo)
        else:
            pass
    print "\t\tPeso Total  \tImportancia total"
    print "\t\t   "+str(best[-4]) +"\t\t\t\t"+str(best[-3])

main()