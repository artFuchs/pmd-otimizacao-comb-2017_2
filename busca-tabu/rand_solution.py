#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rand_solution.py

import math
import random
from solution import Solution


# O objetivo do algorítmo abaixo é criar uma solução aleatória para o PMD.
# Pensei e testei para apenas um caso. Pode ser que não funcione para outros casos.
# Ass. Arthur

# randomize_solution(percentage, vp, M, a):
# S = n*[0];
# Para cada vertice i:
# 	Para cada grupo j:
#       se a RCL tiver espaço,
#    	        adicinar j na RCL
#       senao, se o peso atual do grupo j + i satisfizer a restrição de M[j],
#           se algum grupo k na RCL não satisfaz a restricao,
#               substituir o grupo k com valor mais distante da M[k] pelo grupo j;
#       senao,
#           se o grupo j estiver mais necessitado de peso do que algum grupo k na RCL, substituir o grupo k com o valor
#           mais proximo de M[k]
#   S[i] := RCL(Random index)
# return S


def randomize_solution(percentage, vp, M, a):
    S = Solution(0, len(vp))
    g = len(M)
    max_rcl_size = math.floor((percentage / 100) * g)
    groupValue = g * [0]


    # para cada vertice i:
    for i in range(len(vp)):
        # para cada grupo
        rcl = []
        for j in range(g):
            newValue = groupValue[j] + vp[i]

            if (1-a)*M[j] <= newValue <= (1+a)*M[j]:
                if len(rcl) < max_rcl_size:
                    rcl.append(j)
                else:
                    c = {}
                    for k in rcl:
                        val = groupValue[k] + vp[i]
                        if not (1 - a) * M[k] <= val <= (1 + a) * M[k]:
                            c[k] = abs(M[k] - val)
                    if (c):
                        worse = max(c, key=c.get)
                        rcl[worse] = j

            else:
                if len(rcl) < max_rcl_size:
                    rcl.append(j)
                else:
                    c = {}
                    for k in rcl:
                        val = groupValue[k] + vp[i]
                        if not (1-a)*M[k] <= val <= (1+a)*M[k] and (abs(M[k] - val) < abs(M[j] - newValue)):
                            c[k] = abs(M[k] - val)
                    if (c):
                        worse = min(c, key=c.get)
                        rcl[worse] = j


        s = None
        if len(rcl) > 1:
            s = random.randint(0, len(rcl)-1)
        elif len(rcl) > 0:
            s = rcl[0]

        S.assignGroup(i, s)
        groupValue[s] += vp[i]


    return S


def teste_randomizar():
    random.seed(0)
    s = randomize_solution(50, [1, 2, 3, 4, 5], [4, 6, 5], 0.05)
    print(s)


if __name__ == '__main__':
    import sys
    sys.exit(teste_randomizar())
