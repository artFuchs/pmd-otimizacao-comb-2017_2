#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rand_solution.py

import math
import random
from readVertex import *
from vertex import *
from solution import Solution
from operator import attrgetter


# O objetivo do algorítmo abaixo é criar uma solução aleatória para o PMD.
# Pensei e testei para apenas um caso. Pode ser que não funcione para outros casos.
# Ass. Arthur

# randomize_solution(porcentagem, vertices, grupos):
# S = n*[0];
# ordenar os grupos por maior para menor
# ordenar os vertices por mais pesado para menos pesado
#
# Para cada vertice i:
# 	Para cada grupo j:
#       RCL <= []
#       se i cabe em j:
#           se a RCL tiver espaço:
#               colocar j na RCL
#           senão:
#               PIOR <= None
#               se existe algum grupo k na RCL que não esteja vazio e cuja distância mínima com o 
#               vertice i seja menor que a distância mínima de j com o vertice i:
#                      se a distância mínima do grupo k com o vértice i for a menor,
#                           pior <= k
#               RCL[pior] <= j
#
#   se RCL == []:
#       para cada grupo j:
#           se o grupo j estiver no peso adequado, adicionar j a RCL
#
#   se ainda a RCL == []:
#       adicionar todos grupos na RCL
#       
#   s <= RCL(Random index)
#   S[id do vertex i] <= s
#   grupo[s] += vertice[i] 
# return S


def randomize_solution(percentage, vertexes, groups):
    n = len(vertexes)
    g = len(groups)
    S = Solution(0, n, g)
    max_rcl_size = math.floor((percentage / 100) * g)
    lv = sorted(vertexes, key=attrgetter('weight'), reverse = True)
    lg = sorted(groups, key=attrgetter('maxweight'), reverse = True)
    
    for i in range(n):
        rcl = []
        min_dist = []
        groupValue = g*[None]
        for j in range(g):
            groupValue[j] = lg[j].getMinDistance(lv[i])
            if lg[j].getHipoteticalBalance(lv[i]) != True:
                if len(rcl) < max_rcl_size:
                    rcl.append(j)
                else:
                    pior = None
                    minD = None;
                    for k in range(len(rcl)):
                        if groupValue[j] is None and groupValue[rcl[k]] is not None:
                            if minD is None or groupValue[rcl[k]] < minD:
                                pior = k
                                minD = groupValue[rcl[k]]
                        elif groupValue[rcl[k]] is not None and groupValue[rcl[k]] < groupValue[j]:
                            if minD is None or groupValue[rcl[k]] < minD:
                                pior = k
                                minD = groupValue[rcl[k]]
                    if pior is not None:
                        rcl[pior] = j
        
        if len(rcl) == 0:
            for j in range(g):
                if lg[j].getBalance() != True:
                    rcl.append(j)
        
        if len(rcl) == 0:
            for j in range(g):
                rcl.append(j)
        
        s = rcl[random.randint(0, len(rcl) - 1)]
        S.assignVertex(lv[i].vertexId, lg[s].groupId)
        lg[s].addVertex(lv[i]) 
    return S


def teste_randomizar(list_vert):
    random.seed(0)
    s = randomize_solution(67, list_vert[0], list_vert[1])
    print(s)
    print('------------Vertexes')
    for v in list_vert[0]:
        print(v)
    print('------------Groups')
    for g in list_vert[1]:
        print(g)


if __name__ == '__main__':
    import sys
    l = readVertex("teste3")
    sys.exit(teste_randomizar(l))
