class State():
    def __init__(self,state:str):
        """Constructor of class State, can be modified to suit the problem.

        Args:
            state:str
        Returns:
            None
        """
        self.state = state

    @staticmethod
    def isEqual(stateA, stateB)->bool:
        """Static method, receives two states and check if they´re same. Can be modified to suit the problem.

        Args:
            stateA:State
            stateB:State
        Returns:
            bool
        """
        return stateA.state == stateB.state

class Node():
    def __init__(self,state:State,father=None):
        """Node, stores the statem and recive a father Node parameter(none if it´s root) 

        Args:
            stateA:State
            stateB:State
        Returns:
            None
        """
        self.state = state
        self.father = father

    def __str__(self)->str:
        return "Nodo "+self.state.state+" "

class Problem():
    def __init__(self,actions:dict,state_i:State,state_f:State):
        """Receives a dict of actions, a initial state and a final state.

        Args:
            actions:dict
            state_i:State
            state_f:State
        Returns:
            None
        """
        self.actions = actions
        self.state_i = state_i
        self.state_f = state_f
    
    def isGoal(self,state:State)->bool:
        """Receives a state and check if it´s the final state.

        Args:
            state: State
        Returns:
            bool
        """
        return State.isEqual(state,self.state_f)
