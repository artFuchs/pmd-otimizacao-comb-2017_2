from group import *
from vertex import *
from problem import *

def readInstance(filename, alpha):
    vertices = []
    groups = []

    with open(filename) as instanceFile:
        # vertices and groups numbers
        line = instanceFile.readline()
        [vertexNum, groupNum] = line.split(' ')
        [vertexNum, groupNum] = [int(vertexNum), int(groupNum)]

        # vertices:

        for i in range(0, vertexNum):
            line = instanceFile.readline()
            [value, x, y] = line.split(' ')
            [value, x, y] = [float(value), float(x), float(y)]
            vertex = Vertex(i, x, y, value)
            vertices.append(vertex)

        for i in range(0, groupNum):
            line = instanceFile.readline()
            targetWeight = float(line)
            group = Group(i, targetWeight)
            groups.append(group)



    problem = Problem(vertices, groups, alpha)

    return problem
