from readInstance import *
from solution import *
from tabooList import *


def tabuSearch(problem, initialSolution, maxIterations, tabuListSize):

    iteration = 0
    currentSolution = initialSolution
    tabooList = TabooList(tabuListSize)

    bestSolution = None
    bestSolutionValue = None
    nextSolution = None

    while iteration < maxIterations:
        neighbours = problem.getNeighbours(currentSolution)
        nextSolution = pickNeighbour(problem, currentSolution, neighbours, tabooList)

        if len(neighbours) == 0:
            print("Neighbour list is empty.")

        if nextSolution == None:
            print("Could not pick a neighbour.")
            nextSolution = neighbours[0]

        if problem.isSolutionFeasible(nextSolution):
            print("Current solution is feasible.")
            solutionValue = problem.getSolutionValue(nextSolution)

            if bestSolution == None or solutionValue < bestSolutionValue:

                bestSolution = nextSolution
                bestSolutionValue = solutionValue


        print("Current solution value: " + str(problem.getSolutionValue(nextSolution)))
        tabooList.addMovement(currentSolution)
        currentSolution = nextSolution
        iteration += 1

    print(bestSolutionValue)
    return bestSolution


def pickNeighbour(problem, currentSolution, neighbours, tabooList):
    bestNeighbour = None
    isBestNeighbourFeasible = False
    isCurrentSolutionFeasible = problem.isSolutionFeasible(currentSolution)
    bestValue = problem.getSolutionValue(currentSolution)


    for neighbour in neighbours:

        # If neighbour is not taboo:
        if not tabooList.containsMovement(neighbour):

            # If current solution is not feasible:
            if not isCurrentSolutionFeasible:
                if problem.isSolutionFeasible(neighbour):
                    bestNeighbour = neighbour
                    isBestNeighbourFeasible = True
                else:
                    if not isBestNeighbourFeasible:
                        if bestNeighbour == None or getNumOfFeasibleGroups(problem, neighbour) > getNumOfFeasibleGroups(problem, bestNeighbour):
                            bestNeighbour = neighbour

            # If current solution is feasible:
            else:
                # If neighbour is feasible, calculate its solution value.
                isNeighbourFeasible = problem.isSolutionFeasible(neighbour)
                if isNeighbourFeasible:
                    neighbourValue = problem.getSolutionValue(neighbour)

                    # If its value is better than the best value so far, store it.
                    if bestNeighbour == None or neighbourValue < bestValue:
                        bestNeighbour = neighbour
                        bestValue = neighbourValue

            if bestNeighbour == None:
                bestNeighbour = neighbour

    return bestNeighbour



def getNumOfFeasibleGroups(problem, solution):
    num = 0

    for groupId in solution.getGroupIds():
        if problem.getGroupBalance(solution, groupId):
            num += 1


    return num

if __name__ == '__main__':
    import sys

    problem = readInstance("300-5-0.75-1")
    initialSolution = Solution(0, {})

    groups = problem.getGroups()

    for group in groups:
        initialSolution.addGroup(group.getId())
        if group.getId() == 0:
            for vertex in problem.getVertices():
                initialSolution.assignVertex(vertex.getId(), groups[0].getId())


    solution = tabuSearch(problem, initialSolution, 10000, 30)

    sys.exit()
