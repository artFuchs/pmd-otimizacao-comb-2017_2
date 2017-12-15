#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Vertex:
    def __init__(self, vertexId, w, posx, posy):
        self.vertexId = vertexId
        self.weight = w
        self.x = posx
        self.y = posy
    
    def __str__(self):
        return "Vertex " + str(self.vertexId) + "- pos:(" + str(self.x) + ", " + str(self.y) + "), weight: " + str(self.weight)
        
    def __repr__(self):
        return "<<Vertex " + str(self.vertexId) + ">>"
        
    def calcDist(self, anotherVertex):
        dx = self.x-anotherVertex.x
        dy = self.y-anotherVertex.y
        return math.sqrt(dx*dx+dy*dy)

class Group:
    def __init__(self, groupId, weight, alpha):
        self.groupId = groupId
        self.maxweight = weight
        self.weight = 0
        self.alpha = alpha
        self.vertexes = []
        self.minDist = None
        self.Balance = False 
        # False = Bellow the balance, 
        # True = Above the balance,
        # None = balanced
		
    def __str__(self):
        return "Group " + str(self.groupId) + "- weight: " + str(self.weight) + "/" + str(self.maxweight)
        
    def __repr__(self):
        return "<<Group " + str(self.groupId) + ">>"
		
    def addVertex(self, vertex):
        if not type(vertex) is Vertex:
            raise ValueError("object passed is not an Vertex");
            
        if vertex.weight + self.weight > self.maxweight*(1+self.alpha):
            self.Balance = True
        elif vertex.weight + self.weight < self.maxweight*(1-self.alpha):
            self.Balance = False
        else:
            self.Balance = None
            
        if len(self.vertexes) > 0:
            for v in self.vertexes:
                d = vertex.calcDist(v)
                if (self.minDist is None) or (d < self.minDist):
                    self.minDist=d
    
        self.vertexes.append(vertex)
        self.weight += vertex.weight
        
    def getBalance(self):
        return self.Balance
    
    def getHipoteticalBalance(self, vertex):
        if vertex.weight + self.weight > self.maxweight*(1+self.alpha):
            return True
        elif vertex.weight + self.weight < self.maxweight*(1-self.alpha):
            return False
        else:
            return None
    
    # calculo da distância mínima dos vértices do grupo, se vertex == None
    # ou calculo da distância mínima de cada vértice do grupo com vertex se type(vertex) is Vertex
    def getMinDistance(self, vertex):
        if len(self.vertexes) == 0:
                return None
        elif vertex == None:
            return self.minDist;
        elif type(vertex) is Vertex:
            minD = None
            for i in range(len(self.vertexes)):
                vi = self.vertexes[i]
                d = vertex.calcDist(vi)
                if (minD is None) or (d < minD):
                    minD = d
            return minD;
        else:
            return None
            
		
	
		
