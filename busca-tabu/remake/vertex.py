class Vertex:

    def __init__(self, id, xPos, yPos, value):
        self._id = id
        self._xPos = xPos
        self._yPos = yPos
        self._value = value

    def __repr__(self):
        return "Vertex " + str(self._id) + ", \tx: " + str(self._xPos)+ " \ty: " + str(self._yPos)+ " \tValue: " + str(self._value)

    def getId(self):
        return self._id

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def getValue(self):
        return self._value
