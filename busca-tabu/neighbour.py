# Defines how the neighbours will be determined.
class NeighbourFunction:

    def __init__(self, problemInstance):
        self._problemInstance = problemInstance

    # getNeightbours(self, solution)
    # neighbours := list of neighbours
    #
    # for every originGroup in solution
    #   for every destGroup in solution with destGroup > originGroup
    #       neighbour = reassignVertexFromSolution(solution, originGroup, destGroup)
    #       add new neighbour to the neighbours list
    # return neighbours
    def getNeighbours(self, solution):
        neighbours = []

        groups = solution.getGroups()
        for originGroup in groups:
            for destGroup in range(originGroup + 1, len(groups))
                neighbour = Solution("unnamed", solution)

                self.changeVertexGroup(neighbour, originGroup, destGroup) # I don't like the name of this function
                neighbours.append(neighbour)

        return neighbours

    # reassignVertex(self, solution, originGroup, destGroup)
    #
    # if solution is not feasible
    #   v = a vertex that when reassigned will make the solution feasible
    #   reassign v
    #   return feasible solution
    # else
    #   v = a vertex that will increase the objective value of the solution
    #       the most
    #   reassign v
    #   return best solution
    # return None
    def reassignVertexFromSolution(self, solution, originGroup, destGroup):
        group = solution.getVerticesInGroup(originGroup)
        isSolutionFeasible = self._problemInstance.isFeasible(solution)

        if not isSolutionFeasible:
            for vertex in group:
                solution.assignVertex(vertex, destGroup)
                if solution.isFeasible():
                    return neighbour
        else:
            bestSolution = None
            bestSolutionValue = None

            for vertex in group:
                currentSolution = Solution("unnamed", solution)
                currentSolution.assignVertex(vertex, destGroup)

                isSolutionFeasible = self._problemInstance.isFeasible(currentSolution)
                if isSolutionFeasible:
                    solutionValue = self._problemInstance.calculateObjectiveValue(currentSolution)
                    if bestSolutionValue == None or solutionValue > bestSolutionValue:
                        bestSolutionValue = solutionValue

            return bestSolution
        return None
