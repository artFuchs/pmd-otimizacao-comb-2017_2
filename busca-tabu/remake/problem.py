from solution import *
import math
import random

class Problem:

    def __init__(self, vertices, groups, alpha):
        self._alpha = alpha
        self._vertices = vertices
        self._groups = groups

    def __repr__(self):
        string = "Vertices:\n"

        for vertex in self._vertices:
            string += "\t" + str(vertex) + "\n"

        string += "\nGroups:\n"
        for group in self._groups:
            string += "\t" + str(group) + "\n"

        return string


    def getVertices(self):
        return self._vertices

    def getGroups(self):
        return self._groups

    def getSolutionValue(self, solution):
        minDistance = None

        if self.isSolutionFeasible(solution):
            for groupId in solution.getGroupIds():
                vertexIds = solution.getGroupVertexIds(groupId)
                for vertexIdIndex in range(0, len(vertexIds)):
                    for otherVertexIdIndex in range(vertexIdIndex + 1, len(vertexIds)):
                        v1 = self.getVertices()[vertexIdIndex]
                        v2 = self.getVertices()[otherVertexIdIndex]

                        distance = self.calculateDistance(v1, v2)
                        if minDistance == None or distance < minDistance:
                            minDistance = distance
        return minDistance



    def isSolutionFeasible(self, solution):
        for groupId in solution.getGroupIds():
            groupBalance = self.getGroupBalance(solution, groupId)
            if groupBalance != None:
                return False

        return True

    def calculateGroupWeight(self, solution, groupId):
        weightSum = 0
        group = self._groups[groupId]

        vertexIds = solution.getGroupVertexIds(groupId)

        for vertexId in vertexIds:
            vertex = self._vertices[vertexId]
            weightSum += vertex.getValue()

        return weightSum

    def getGroupBalance(self, solution, groupId):
        weightSum = self.calculateGroupWeight(solution, groupId)
        group = self._groups[groupId]
        groupTargetWeight = group.getTargetWeight()

        if weightSum < (1 - self._alpha) * groupTargetWeight:
            return False
        elif weightSum > (1 + self._alpha) * groupTargetWeight:
            return True
        else:
            return None


    def calculateDistance(self, vertex1, vertex2):
        dx = vertex1.getXPos() - vertex2.getXPos()
        dy = vertex1.getYPos() - vertex2.getYPos()

        return math.sqrt((dx * dx) + (dy * dy))



    def getNeighbours(self, solution):
        neighbours = []
        groupIds = solution.getGroupIds()

        for groupId in groupIds:
            for otherGroupId in groupIds:
                if groupId != otherGroupId:

                    groupVertexIds = solution.getGroupVertexIds(groupId)


                    if len(groupVertexIds) != 0:
                        vertexId = random.choice(groupVertexIds)

                        neighbour = Solution(solution.getId(), solution.getGroupAssignment())
                        neighbour.deassignVertex(vertexId, groupId)
                        neighbour.assignVertex(vertexId, otherGroupId)

                        neighbours.append(neighbour)


        return neighbours
