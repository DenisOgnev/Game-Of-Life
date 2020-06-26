import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALIVE = 0
DEAD = 1

class Grid:
    def __init__(self, width, height, cellSize):
        self.Cells = list()
        self.width = width
        self.height = height
        self.cellSize = cellSize
        for i in range(int(self.width / self.cellSize)):
            self.Cells.append(list())
            for j in range(int(self.height / self.cellSize)):
                self.Cells[i].append(Cell(DEAD))

    def randomInit(self):
        for i in range(int(self.width / self.cellSize)):
            for j in range(int(self.height / self.cellSize)):
                if(random.random() > 0.8):
                    self.Cells[i][j].state = ALIVE
    
    def clear(self):
        for i in range(int(self.width / self.cellSize)):
            for j in range(int(self.height / self.cellSize)):
                    self.Cells[i][j].state = DEAD


    def draw(self, sc):
        #for i in range(int(self.width / self.cellSize) + 1):
        #    for j in range(int(self.height / self.cellSize) + 1):
        #        pygame.draw.line(sc, WHITE, (0, j * self.cellSize), (self.width, j * self.cellSize))
        #        pygame.draw.line(sc, WHITE, (i * self.cellSize, 0), (i * self.cellSize, self.height))

        for i, cells in enumerate(self.Cells):
            for j, cell in enumerate(cells):
                if cell.state == ALIVE:
                    pygame.draw.rect(sc, WHITE, (i * self.cellSize + 2, j * self.cellSize + 2, self.cellSize - 3, self.cellSize - 3))

    def change(self):
        radius = 1
        newStates = list()
        for i in range(int(self.width / self.cellSize)):
            newStates.append(list())
            for j in range(int(self.height / self.cellSize)):
                newStates[i].append(Cell(DEAD))
        for i in range(1, int(self.width / self.cellSize) - 1):
            for j in range(1, int(self.height / self.cellSize) - 1):
                count = 0
                for k in range(-radius, radius + 1):
                    for l in range(-radius, radius + 1):
                        if k == 0 and l == 0:
                            if self.Cells[i][j].state == ALIVE:
                                newStates[i][j].state = ALIVE
                            continue
                        if self.Cells[i + k][j + l].state == ALIVE:
                            count += 1
                if self.Cells[i][j].state == DEAD:
                    if count == 3:
                        newStates[i][j].state = ALIVE
                else:
                    if count > 3 or count < 2:
                        newStates[i][j].state = DEAD
        self.Cells = newStates

    def createClick(self, pos):
        x = pos[0] // self.cellSize
        y = pos[1] // self.cellSize
        if self.Cells[x][y].state == DEAD:
            self.Cells[x][y].state = ALIVE

    def deleteClick(self, pos):
        x = pos[0] // self.cellSize
        y = pos[1] // self.cellSize
        if self.Cells[x][y].state == ALIVE:
            self.Cells[x][y].state = DEAD

                

class Cell:
    def __init__(self, state):
        self.state = state
