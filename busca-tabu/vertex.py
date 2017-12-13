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
        dy = self.x-anotherVertex.x
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
        return "Group " + str(self.groupId) + "- weight: " + str(self.weight) + "/" + str(self.maxweigth)
        
    def __repr__(self):
        return "<<Group " + str(self.groupId) + ">>"
		
    def addVertex(self, vertex):
        if not type(vertex) is Vertex:
            raise ValueError("object passed is not an Vertex");
            
        if vertex.weight + self.weight > self.maxweight*(1+alpha):
            self.Balance = True
        elif vertex.weight + self.weight < self.maxweight*(1-alpha):
            self.Balance = False
        else:
            self.Balance = None
            
        if len(self.vertexes) > 0:
            for v in self.vertexes:
                d = vertex.calcDist(v)
                if (self.minDist is None) or (d < minDist):
                    self.minDist=d
                    
        self.vertexes.append(vertex)
        
    def getBalance(self):
        return self.Balance
		
	
		
