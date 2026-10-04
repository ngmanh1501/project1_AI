# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack() # su dung stack de luu cac trang thai can duyet
    visited = set() # su dung set de luu cac trang thai da duyet
    startState = problem.getStartState() # lay state ban dau 
    frontier.push((startState,[])) # push state ban dau va path rong vao frontier

    while not frontier.isEmpty():
        state, path = frontier.pop() # lay state va path tu frontier

        # neu state da duyet thi bo qua
        if state in visited:
            continue

        visited.add(state) # them state da duyet vao visited

        # neu state la goal thi tra ve path
        if problem.isGoalState(state):
            return path

        # lay cac successor cua state va push vao frontier neu chua duyet
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                newPath = path + [action] # tao path moi tu path hien tai va action moi
                frontier.push((successor, newPath)) 

    return [] # tra ve list rong neu khong tim thay goal 

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue() 
    visited = set()
    startState = problem.getStartState()
    frontier.push((startState,[]))

    while not frontier.isEmpty():
        state, path = frontier.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                newPath = path + [action]
                frontier.push((successor, newPath))

    return []
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    visited = set()
    startState = problem.getStartState()
    frontier.push((startState, [], 0), 0) # push state ban dau gom trang thai va chi phi ban dau bang 0

    while not frontier.isEmpty():
        state, path, cost = frontier.pop() # lay state, path va chi phi tu frontier

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                newPath = path + [action]
                newCost = cost + stepCost # tinh chi phi moi
                frontier.push((successor, newPath, newCost), newCost) # push state moi vao frontier voi chi phi moi

    return []
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    visited = set()
    startState = problem.getStartState()
    frontier.push((startState, [], 0), heuristic(startState, problem)) # push state ban dau vao frontier voi chi phi heuristic

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                newPath = path + [action]
                newCost = cost + stepCost
                priority = newCost + heuristic(successor, problem) # tinh priority moi tu chi phi va heuristic
                frontier.push((successor, newPath, newCost), priority) # push state moi vao frontier voi priority moi

    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
