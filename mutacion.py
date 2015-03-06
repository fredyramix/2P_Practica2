# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random

def Mutar(cruzados,num):

    x=random.randrange(0,int(num)-1)
    mu=cruzados[x]
    print mu
    y= random.randint(0,len(mu)-1)
    print y
    if mu[y]==1:
        mu[y]=0
    else:
        mu[y]=1
    return cruzados