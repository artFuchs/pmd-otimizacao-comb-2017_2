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
        return "Vertex " + str(self.vertexId) + ": (" + str(self.x) + ", " + str(self.y) + "), weight: " + str(self.weight)
        
    def __repr__(self):
        return "<<Vertex " + str(self.vertexId) + ">>"
        
    def calcDist(self, anotherVertex):
        dx = self.x-anotherVertex.x
        dy = self.x-anotherVertex.x
        return math.sqrt(dx*dx+dy*dy)
