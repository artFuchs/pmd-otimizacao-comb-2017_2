import copy

class Solution:

    def __init__(self, id, groupAssignment):
        self._id = id
        self._groupAssignment = copy.deepcopy(groupAssignment)

    def __eq__(self, other):
        if other == None:
            return False

        return self._groupAssignment == other.getGroupAssignment()

    def __repr__(self):
        string = ""

        for groupId in self._groupAssignment:
            string += "Group " + str(groupId) + "\n"
            for vertexId in self._groupAssignment[groupId]:
                string += "\tVertex " + str(vertexId) + "\n"
        return string

    def assignVertex(self, vertexId, groupId):
        if not groupId in self._groupAssignment:
            self._groupAssignment[groupId] = []

        self._groupAssignment[groupId].append(vertexId)

    def deassignVertex(self, vertexId, groupId):
        if self._groupAssignment[groupId] != None:
            self._groupAssignment[groupId].remove(vertexId)

    def addGroup(self, groupId):
        self._groupAssignment[groupId] = []

    def getGroupIds(self):
        groupIds = []

        for groupId in self._groupAssignment:
            groupIds.append(groupId)

        return groupIds

    def getGroupVertexIds(self, groupId):
        if groupId in self._groupAssignment:
            return self._groupAssignment[groupId]
        return None

    def getId(self):
        return self._id

    def getGroupAssignment(self):
        return self._groupAssignment
