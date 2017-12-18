from readInstance import *
from solution import *
from tabooList import *
import random
from rand_solution import *

def tabuSearch(problem, initialSolution, maxIterations, tabuListSize):

    iteration = 0
    currentSolution = initialSolution
    tabooList = TabooList(tabuListSize)

    bestSolution = None
    bestSolutionValue = None
    nextSolution = None
    if problem.isSolutionFeasible(currentSolution):
        bestSolutionValue = problem.getSolutionValue(currentSolution)

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

            if bestSolution == None or solutionValue > bestSolutionValue:
                bestSolution = nextSolution
                bestSolutionValue = solutionValue


        currentSolution = nextSolution
        print("Iteration " + str(iteration) + ", Current solution value: " + str(problem.getSolutionValue(currentSolution)))
        printSolutionInfo(problem, currentSolution)
        tabooList.addMovement(currentSolution)

        iteration += 1

    print("best value: " + str(bestSolutionValue))
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
                        else:
                            bestNeighbour = getBestSolution(problem, bestNeighbour, neighbour)


            # If current solution is feasible:
            else:
                # If neighbour is feasible, calculate its solution value.
                isNeighbourFeasible = problem.isSolutionFeasible(neighbour)
                if isNeighbourFeasible:
                    neighbourValue = problem.getSolutionValue(neighbour)

                    # If its value is better than the best value so far, store it.
                    if bestNeighbour == None or neighbourValue > bestValue:
                        bestNeighbour = neighbour
                        bestValue = neighbourValue

            if bestNeighbour == None:
                bestNeighbour = neighbour


        else:
            print("TABOO NEIGHBOUR")

    return bestNeighbour



def getNumOfFeasibleGroups(problem, solution):
    num = 0

    for groupId in solution.getGroupIds():
        if problem.getGroupBalance(solution, groupId) == None:
            num += 1


    return num

def printSolutionInfo(problem, solution):
    groupIds = solution.getGroupIds()
    groups = problem.getGroups()

    for groupId in groupIds:
        lowerBound = groups[groupId].getTargetWeight() * (1 - problem.getAlpha())
        upperBound = groups[groupId].getTargetWeight() * (1 + problem.getAlpha())
        weightString = str(lowerBound) + " <= " + str(problem.calculateGroupWeight(solution, groupId)) + " <= " + str(upperBound)
        print(str(groups[groupId]) + ", Weight Info: " + weightString + ", Balance: " + str(problem.getGroupBalance(solution, groupId)))
    print("")


def getBestSolution(problem, solution, otherSolution):

    groups = problem.getGroups()
    groupIds = solution.getGroupIds()
    solutionGoodGroups = 0
    otherSolutionGoodGroups = 0

    for groupId in groupIds:

        group = groups[groupId]

        groupWeight = problem.calculateGroupWeight(solution, groupId)
        otherSolutionGroupWeight = problem.calculateGroupWeight(otherSolution, groupId)

        groupDiff = math.fabs(group.getTargetWeight() - groupWeight)
        otherGroupDiff = math.fabs(group.getTargetWeight() - otherSolutionGroupWeight)

        if groupDiff <= otherGroupDiff:
            solutionGoodGroups += 1
        else:
            otherSolutionGoodGroups += 1

    if solutionGoodGroups >= otherSolutionGoodGroups:
        return solution
    else:
        return otherSolution

def display_help():
    print(u'Uso: tabuSearch [OPÇÃO] | [ARQUIVO] [NUMERO DE ITERAÇÕES] [TAMANHO DA LISTA TABU] (OPT)[ALPHA]')
    print(u'procura soluções para o problema da PARTIÇÃO MAIS DISTANTE utilizando Busca Tabu')
    print("\n Se ARQUIVO, NUMERO DE ITERAÇÕES e TAMANHO DA LISTA TABU não fore especificados, mostra essa ajuda e finaliza")
    print("-h, --help: mostra essa ajuda e finaliza")


#linha de comando: tabuSearch [nome do arquivo] [numero de iterações] [tamanho da lista tabu] (OPT)[alpha]
if __name__ == '__main__':
    import sys
    import time
    
    start_time = time.time()
    
    if len(sys.argv) < 4 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        display_help()
        sys.exit()
    
    random.seed(0)
	
    alpha = 0.05
    if len(sys.argv) > 4:
        alpha = sys.argv[4]
    problem = readInstance(sys.argv[1], float(alpha))
    
    #problem = readInstance("teste")
    initialSolution = Solution(0, {})

    #groups = problem.getGroups()
	#
    #for group in groups:
    #    initialSolution.addGroup(group.getId())
    #    if group.getId() == 0:
    #        for vertex in problem.getVertices():
    #            initialSolution.assignVertex(vertex.getId(), groups[0].getId())
    
    initialSolution = randomize_solution(33, problem)
    
    solution = tabuSearch(problem, initialSolution, int(sys.argv[2]), int(sys.argv[3]))
	
    print("initial: " + str(problem.getSolutionValue(initialSolution)))
    
    print("------ %s seconds ----------"%(time.time()-start_time))
	
    sys.exit()
