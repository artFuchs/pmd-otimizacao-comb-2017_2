#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vertex import *
from operator import attrgetter


alpha = 0.05

# readVertex(filepath) - filepath: string
# Lê um arquivo de instância do pmd e retorna uma lista contendo: uma lista de vértices e uma lista
# de grupos
def readVertex(filename):
    counter = 0
    l = []
    with open(filename) as f:
		# read first line;
        s = f.readline()
        [n, g] = s.split(' ')
        n = int(n)
        g = int(g)
		
        lv = []
        for i in range(n):
            s = f.readline()
            [w, x, y] = s.split(' ')
            [w, x, y] = [int(w), int(x), int(y)]
            v = Vertex(i, w, x, y)
            lv.append(v)
        l.append(lv)
        
        lg = []
        for i in range(g):
            s = f.readline()
            g = Group(i, int(s), alpha)
            lg.append(g)
        l.append(lg)
    return l
    
def readTest(filename):
	[lv, lg] = readVertex(filename)
	#teste de ordenação
	lv = sorted(lv, key=attrgetter('weight'), reverse = True)
	lg = sorted(lg, key=attrgetter('maxweight'), reverse = True)
	print(lv)
	print(lg)
	
    
if __name__ == '__main__':
    import sys
    filename = "teste"
    sys.exit(readTest(filename))
