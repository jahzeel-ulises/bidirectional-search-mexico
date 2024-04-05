from bidirectional_class import BidirectionalSearch
from graph import Problem
from graph import State
import pygame
import time
from tkinter import messagebox
import json

def motion(initial:str,final:str)->None:
    """Display the animation of the searching algorithm.

    Args:
        initial:str
        final:str
    Returns:
        None
    """
    #------------------Define Functions-----------------------------------
    def drawVertices():
        """Draw the graph´s vertices.

        Args:
            None
        Returns:
            None
        """
        for i in position.keys():
            pygame.draw.rect(screen,color[i],(position[i][0],position[i][1],10,10))
            myfont = pygame.font.SysFont("monospace", 10)
            label = myfont.render(i,1,(0,0,1))
            screen.blit(label,(position[i][0],position[i][1]-10))
        
    def drawEdges():
        """Draw graph's edges.

        Args:
            None
        Returns:
            None
        """
        for i in actions.keys():
            for j in actions[i]:
                pygame.draw.line(screen,(0,0,0),position[i],position[j])

    def changeColor(db:BidirectionalSearch):
        """Change the graph's nodes´s colors.

        Args:
            None
        Returns:
            None
        """
        for i in db.frontier_i:
            color[i.state.state]=(0,255,0)
        
        for i in db.explored_i:
            color[i.state.state]=(0,0,255)
        
        for i in db.frontier_f:
            color[i.state.state]=(0,255,0)
        
        for i in db.explored_f:
            color[i.state.state]=(0,0,255)

    def paintSolution(node):
        """Change the color of both´s trees intersection.

        Args:
            None
        Returns:
            None
        """
        color[node.state.state] = (0,0,0)

    def reset():
        """Reset the color of the graph.

        Args:
            None
        Returns:
            None
        """
        for i in color.keys():
            color[i] = (255,0,0)

    #------------Load Data----------------
    with open('data\data.json','r') as file:
        data = json.load(file)
    color = data["color"]
    position = data["positions"]
    actions = data["actions"]

    state_i = State(initial)
    state_f = State(final)

    problem = Problem(actions,state_i,state_f)

    bd = BidirectionalSearch(actions,state_i,state_f)
    solution = list()

    if bd.initialize():
        pass

    pygame.init()
    size = (1250,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Simulador')

    framerate = 1
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        result = bd.step()

        screen.fill((255,255,255))
        drawEdges()
        drawVertices()

        if type(result) == bool:
            if not result:
                messagebox.showerror("Warning","No hay solucion")
                pygame.quit()
                return
            changeColor(bd)
        else:
            solution = bd.buildSolution(result)
            paintSolution(result[0])
            break

            
        clock.tick(framerate)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255,255,255))
        drawEdges()
        drawVertices()
            
        clock.tick(framerate)
        pygame.display.update()
        time.sleep(3)
        break

    reset()

    i = 0
    lenn = len(solution)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if i == lenn:
            continue
        paintSolution(solution[i])
        i+=1
        screen.fill((255,255,255))
        drawEdges()
        drawVertices()
            
        clock.tick(framerate)
        pygame.display.update()