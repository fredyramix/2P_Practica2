# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from random import randrange
import random

def LeerArticulos():
    dic={}
    archi=open('articulos.txt','r')
    linea="a"
    c=1
    while linea!="":
        try:
            linea=archi.readline()
            listita=[]
            a=linea.split(',')
            b=a[1]
            d=b[:-1]
            listita.append(str(a[0]))
            listita.append(str(d))
            dic[c]=listita
            c=c+1
        except IndexError,e:
            pass #encontro un salto de linea.
    archi.close()
    return dic

def GenerarAleatoria(all,num):
    tam=len(all)
    pob=[]
    for i in range(0,num):
        cromosoma=[]
        for x in range(0,tam):
            n=randrange(0,2) #para los bits del croma
            cromosoma.append(n)
        pob.append(cromosoma)
    return pob

def EvaluarFX(poblacion,articulos):
    fun_evaluada=[]
    print articulos
    tam=len(poblacion)
    p=[]
    for i in poblacion:
        c=1
        Wt=0
        It=0
        for j in i:
            if j==1:
                articulo = articulos[c]
                w=articulo[0] #peso
                I=articulo[1] #importancia
                Wt=Wt+int(w) #peso total por cromosoma
                It=It+int(I) #Importancia total por cromosoma
            c=c+1
        i.append(Wt)
        i.append(It)
        p.append(i)
    return p

def Penalizar(funcion_evaluada,peso_maximo):
    a=int(peso_maximo)
    # la unica forma de penalizacion es que el peso exeda el tamaño de la caja
    for i in funcion_evaluada:
        pena=0
        if int(i[-2])>a:
            #Esta inclumpliendo el peso accion: Penalizar
            pena=i[-2] + 1000
        else:
            pena = i [-2]
        i.append(pena)
    return funcion_evaluada

def SumatoriaFX(lista):
    suma=0
    for x in lista:
        suma=suma+abs(int(x[-1]))
    return suma

def Probabilidad(funciones_penalizadas,suma):
    for x in funciones_penalizadas:
        resta=float(suma)-float(x[-1])
        p=(resta*100)/float(str(suma))
        x.append(int(p))
    return funciones_penalizadas

def Ruleta(lista):
    rul=[]
    for x in lista:
        x.reverse()
        rul.append(x)
    rul.sort()
    new=[]
    for y in rul:
        y.reverse()
        new.append(y)
    return new

def SeleccionParejas(opciones,num_cro):
    count =0
    tabla_hijos=[]
    while count!=num_cro:
        n=random.randrange(0,100)
        for x in opciones:
            if int(x[13]) <= n:
                tabla_hijos.append(x)
                count=count+1
            else:
                pass
    return opciones,tabla_hijos