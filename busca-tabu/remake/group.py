

class Group:

    def __init__(self, id, targetWeight):
        self._id = id
        self._targetWeight = targetWeight

    def __repr__(self):
        string = "Group " + str(self._id) + ", \tTarget Weight: " + str(self._targetWeight)
        return string

    def getTargetWeight(self):
        return self._targetWeight

    def getId(self):
        return self._id
