# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  pilha =util.Stack()
  visitado = []
  start_state = (problem.getStartState(), [])
  pilha.push(start_state)

  while not pilha.isEmpty():
    remover = pilha.pop()
    posicao = remover[0]
    caminho = remover [1]

    if posicao not in visitado:
      visitado.append(posicao)

      if problem.isGoalState(posicao):
        return caminho

      sucessores = problem.getSuccessors(posicao)

      for sucessor in list (sucessores):
        if sucessor[0] not in visitado:
          pilha.push((sucessor[0], caminho + [sucessor[1]]))
          
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"

  fila = util.Queue()
  visitado = []
  start_state = (problem.getStartState(), [])
  fila.push(start_state)

  while not fila.isEmpty():
    remover = fila.pop()
    posicao = remover[0]
    caminho = remover [1]

    if posicao not in visitado:
      visitado.append(posicao)

      if problem.isGoalState(posicao):
        return caminho
  
      sucessores = problem.getSuccessors(posicao)

      for sucessor in list (sucessores):
        if sucessor[0] not in visitado:
          fila.push((successor[0], caminho + [sucessor[1]]))
          
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  prioridade = util.PriorityQueue()
  visitado = {}
  start_state = (problem.getStartState())
  acoes = []
  cost = 0
  prioridade.push((tart_state, acoes, custo), custo)

  while not prioridade.isEmpty():
    remover = prioridade.pop()

    if problem.isGoalState(removed [0]):
      return remover [1]

    if remover[0] not in visitado:
      visitado[remover[0]] = True

      for sucessor, novo, prox in problem.getSuccesors(remover[0])
        if sucessor and sucessor not in visitado:
          prioridade.push((sucessor, remover[1]+[novo], remover[2] + prox),remover[2]+prox)
  
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
