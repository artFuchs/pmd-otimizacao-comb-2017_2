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