class Solution:

    def __init__(self, solutionId, numberVertices):
        self._solutionId = solutionId
        self._groupAssignment = numberVertices * [None]
        self._numberVertices = numberVertices

    def __str__(self):
        
        string = "Solution " + str(self._solutionId) + ":\n"

        for i in range(0, self._numberVertices):
            string += "Vertex " + str(i) + ": " + "Group " + str(self._groupAssignment[i]) + ".\n"

        return string
    
    def assignGroup(self, vertexNumber, group):
        self._groupAssignment[vertexNumber] = group

    def desasignGroupAll(self, maxVertexNumber, group):
        for i in range(maxVertexNumber):
            if self._groupAssignment[i] == group:
                self._groupAssignment[i] = None;

    def getVertexGroup(self, vertexNumber):
        return self._groupAssignment;