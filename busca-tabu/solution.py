class Solution:

    def __init__(self, solutionId, numberVertices, numGroups):
        self._solutionId = solutionId
        self._groupAssignment = numberVertices * [None]
        self._numVertices = numberVertices
        self._numGroups = numGroups

    def __str__(self):

        string = "Solution " + str(self._solutionId) + ":\n"

        for i in range(0, self._numVertices):
            string += "Vertex " + str(i) + ": " + "Group " + str(self._groupAssignment[i]) + ".\n"

        return string

    def assignVertex(self, vertexNum, groupNum):
        self._groupAssignment[vertexNum] = groupNum

    def desasignGroupAll(self, maxVertexNumber, group):
        for i in range(maxVertexNumber):
            if self._groupAssignment[i] == group:
                self._groupAssignment[i] = None;

    def getVertexGroup(self, vertexNumber):
        return self._groupAssignment[vertexNumber];

    def getGroups(self):
        return range(0, numGroups)

    def getVerticesInGroup(self, groupNum):
        group = []

        for i in range(0, self._numVertices):
            if self._groupAssignment[i] == groupNumber:
                group.append(i)

        return group
