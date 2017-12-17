#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rand_solution.py

import math


from problem import *
from operator import attrgetter


# O objetivo do algorítmo abaixo é criar uma solução guloso-aleatória para o PMD.
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

def randomize_solution(percentage, problem):
    if (type(problem) is not Problem):
        return -1 ##Aqui enviar um erro
    
    vertexes = problem.getVertices()
    groups = problem.getGroups()
    
    n = len(vertexes)
    g = len(groups)
    max_rcl_size = math.floor((percentage / 100) * g)
    lv = sorted(vertexes, key=attrgetter('_value'), reverse = True)
    lg = sorted(groups, key=attrgetter('_targetWeight'), reverse = True)
    
    S = Solution(0,{})
    for group in lg:
        S.addGroup(group.getId())
    
    for i in range(n):
        vId = lv[i].getId()
        rcl = []
        groupValue = g*[None]
        for j in range(g):
            gId = lg[j].getId()
            Si = copy.deepcopy(S)
            Si.assignVertex(vId, gId)
            
            groupValue[j] = getMinDist(problem, S, gId, vId)
            
            if problem.getGroupBalance(Si, gId) != True:
                #    lg[j].getHipoteticalBalance(lv[i]) != True:
                if len(rcl) < max_rcl_size:
                    rcl.append(j)
                else:
                    pior = None
                    minD = None
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
                if problem.getGroupBalance(S, lg[j].getId()) != True:
                    #  lg[j].getBalance() != True:
                    rcl.append(j)
        
        if len(rcl) == 0:
            for j in range(g):
                rcl.append(j)
        
        s = rcl[random.randint(0, len(rcl) - 1)]
        S.assignVertex(lv[i].getId(), lg[s].getId())
    return S


def getMinDist(problem, solution, groupId, vertexId):
    vertexesIDs = solution.getGroupVertexIds(groupId)
    vertexes = problem.getVertices()
    minD = None
    for vID in vertexesIDs:
        d = problem.calculateDistance(vertexes[vID], vertexes[vertexId])
        if minD is None or d < minD:
            minD = d
    return minD
        
        
    
    


def teste_randomizar(problem):
    s = randomize_solution(67, problem)
    print(s)

if __name__ == '__main__':
    import sys
    import random
    from readInstance import *

    random.seed(0)

    p = readInstance("teste3")
    sys.exit(teste_randomizar(p))
