# -*- encoding: utf-8 -*-
__author__ = 'fredy'

def Cruzar(nuevos):
    poblacion=[]
    c=0
    while len(nuevos)!=0:
        try:
            x=nuevos[0]
            y=nuevos[1]
            mitad1 = x[0:(len(x)/2)]
            mitad2 = x[len(x)/2:]
            mitad3 =  y[0:(len(y)/2)]
            mitad4 = y[len(y)/2:]
            nuevo1 = mitad1+mitad4
            nuevo2=mitad3+mitad2
            poblacion.append(nuevo1)
            poblacion.append(nuevo2)
            del nuevos[0]
            del nuevos[0]
            c=c+1
        except IndexError,e:
            poblacion.append(nuevos[0])
            del nuevos[0]
            c=c+1
    return poblacion