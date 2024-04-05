from src.graph import Node
from src.graph import Problem
from src.graph import State

class BidirectionalSearch():
    def __init__(self,actions,state_i:State,state_f:State)->None:
        """Constructor of class BidirectionalSearch.

        Args:
            actions:dict
            state_i:State
            state_f:State
        Returns:
            None
        
        actions must be of the form

        {
            element:[neightbor1,neightbour2...],
            element2:[neightbor1,neightbour2,..],

            ...
        }
        """
        self.problem = Problem(actions,state_i,state_f)

        self.frontier_i = list()
        self.frontier_f = list()

        self.explored_i = list()
        self.explored_f = list()
        pass

    def initialize(self) -> tuple[Node,None] | None:
        """Check if the initial state is not equal to the final.

        Args:
            None
        Returns:
            tuple[Node,None] | None
        """
        root_i = Node(self.problem.state_i)
        root_f = Node(self.problem.state_f) 
    
        if self.problem.isGoal(root_i.state): #Revisa que la condicion inicial no sea la misma que la final
            return (root_i,None)
    
        self.frontier_i.append(root_i) #Creamos las estructuras fifo para las busquedas
        self.frontier_f.append(root_f)

        return None
    
    def step(self) -> tuple[Node,None] | tuple[None,Node] | tuple[Node,Node] | bool:
        """Makes an iteration of the Bidirectional Search Algorithm, returns True if we can continue, False if there isn´t a solution, a tuple with the intersection of both searching trees.

        Args:
            None
        Returns:
            tuple[Node,None] | tuple[None,Node] | tuple[Node,Node] | bool
        """
        if self.frontier_i and self.frontier_f:
            node_i = self.frontier_i.pop(0) #Extraemos los nodos que visitaremos
            self.explored_i.append(node_i)
            solution_i = expand_frontier(self.problem,node_i,self.frontier_i,self.explored_i,self.frontier_f) #Expande la frontera del arbol inicial
            if solution_i:
                if type(solution_i) == Node:
                    return(solution_i,None)
                else:
                    return intersection(self.frontier_i,self.frontier_f)

            node_f = self.frontier_f.pop(0)
            self.explored_f.append(node_f)
            solution_f = expand_frontier(self.problem,node_f,self.frontier_f,self.explored_f,self.frontier_i)#Expande la frontera del nodo final
            if solution_f:
                if type(solution_f) == Node:
                    return(None,solution_f)
                else:
                    return intersection(self.frontier_i,self.frontier_f)
            return True
        else:
            return False

    def buildSolution(self,solution:tuple[Node,None] | tuple[None,Node] | tuple[Node,Node] | None)->list:
        """Receives tuple[Node,None] | tuple[None,Node] | tuple[Node,Node] | None and return an ordered list with the solution or None.

        Args:
            solution: tuple[Node,None] | tuple[None,Node] | tuple[Node,Node] | None
        Returns:
            list
        """
        if not solution: 
            return None
        node = solution[0]
        camino = []
        while node:     #Se realiza backtraking mediante la lista enlaza generada la ingresar los elementos a frontier
            camino.insert(0,node)
            node = node.father
        node = solution[1]
        if node: node = solution[1].father
        while node:
            camino.append(node)
            node = node.father
        return camino

def intersection(setI:list,setF:list)->tuple[Node,Node] | tuple[None,None]:
    """Receives a couple of states lists and return and element that is in intesection of both. 

    Args:
        setI:list
        setF:list
    Returns:
        tuple[Node,Node]
        tuple[None,None]
    """
    for node in setI:
        if isIn(setF,node):
            for i in setF:
                if State.isEqual(node.state,i.state):
                    return(node,i)

    return (None,None)

def expand_frontier(problem:Problem,actualNode:Node,frontier:list,explored:list,frontier_o:list):
    """Expand the frontier of a node

    Args:
        problem:Problem
        actualNode:Node
        frontier:list
        explored:list
        frontier_o:list
    Returns:
        Literal[True] | None
    """
    for action in problem.actions[actualNode.state.state]:
        child = Node(State(action),actualNode)
        if not isIn(frontier,child) and not isIn(explored,child):
            frontier.append(child)
                # if State.isEqual(child.state,goal.state):
                #     return child
            if isIn(frontier_o,child):
                    return True
    return None

def isIn(set:list,node:Node)->bool:
    """Return True if the node is in set and False if not.

    Args:
        set:list
        node:Node
    Returns:
        bool
    """
    for nodes in set:
        if State.isEqual(node.state,nodes.state):
            return True
    return False