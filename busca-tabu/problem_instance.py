
# Represents an instance of a problem.
# Used for calculating the objective value of a solution and checking if
# a solution is feasible.
class ProblemInstance:

    def __init__(self, objectiveFunction, restrictions):
        self._objectiveFunction = objectiveFunction
        self._restrictions = restrictions

    def isSolutionFeasible(self, solution):
        for restriction in self._restrictions:
            if not restriction(solution):
                return False

        return True

    def calculateObjectiveValue(self, solution):
        if self.isSolutionFeasible(solution):
            return self._objectiveFunction(solution)
        return None
