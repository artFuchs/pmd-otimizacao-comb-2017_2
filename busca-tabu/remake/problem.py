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

    def getAlpha(self):
        return self._alpha

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
        numChanges = 5
        neighbours = []
        groupIds = solution.getGroupIds()

        for groupIdIndex in range(0, len(groupIds)):
            for otherGroupIdIndex in range(groupIdIndex + 1, len(groupIds)):
                groupId = groupIds[groupIdIndex]
                otherGroupId = groupIds[otherGroupIdIndex]
                chosenVertices = []

                [originGroupId, destGroupId] = self.getOriginAndDest(solution, groupId, otherGroupId)

                vertexMovements = []
                for i in range(0, numChanges):
                    vertexId = self.pickVertex(solution, originGroupId, destGroupId, vertexMovements)
                    if vertexId != None:
                        vertexMovements.append(vertexId)

                for vertexId in vertexMovements:
                    neighbour = Solution(solution.getId(), solution.getGroupAssignment())

                    neighbour.deassignVertex(vertexId, originGroupId)
                    neighbour.assignVertex(vertexId, destGroupId)

                    neighbours.append(neighbour)

        return neighbours




    def getOriginAndDest(self, solution, groupId, otherGroupId):
        groupBalance = self.getGroupBalance(solution, groupId)
        otherGroupBalance = self.getGroupBalance(solution, otherGroupId)

        originGroupId = groupId
        destGroupId = otherGroupId

        if groupBalance == True and (otherGroupBalance == False or otherGroupBalance == None):
            originGroupId = groupId
            destGroupId = otherGroupId
        elif otherGroupBalance == True and (groupBalance == False or groupBalance == None):
            originGroupId = otherGroupId
            destGroupId = groupId
        else:
            groups = self.getGroups()
            group = groups[groupId]
            otherGroup = groups[otherGroupId]

            groupWeight = self.calculateGroupWeight(solution, groupId)
            otherGroupWeight = self.calculateGroupWeight(solution, otherGroupId)

            groupDiff = math.fabs(group.getTargetWeight() - groupWeight)
            otherGroupDiff = math.fabs(otherGroup.getTargetWeight() - otherGroupWeight)

            if groupDiff >= otherGroupDiff:
                originGroupId = otherGroupId
                destGroupId = groupId
            else:
                originGroupId = groupId
                destGroupId = otherGroupId

        return [originGroupId, destGroupId]


    def pickVertex(self, solution, originGroupId, destGroupId, pickedVertices):

        originVertexIds = solution.getGroupVertexIds(originGroupId)

        if len(originVertexIds) > len(pickedVertices):

            vertexId = random.choice(originVertexIds)

            while vertexId in pickedVertices:
                vertexId = random.choice(originVertexIds)

            return vertexId

        else:
            return None
