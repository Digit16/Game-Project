import pygame
import os

import tiles


class Game:

    def __init__(self):
        self.size = self.width, self.height = (864, 576)  
        self.trueSize = (288, 192)
        

        self.win = pygame.display.set_mode((self.width, self.height))
        


        self.dungeonTileset = pygame.image.load(os.path.join("assets","Dungeon_Tileset.png"))
        self.map = []

    def run(self):
        run = True

        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            self.draw()

        pygame.quit()

    def draw(self):
        BLACK = pygame.Color(0,0,0)
        #self.win.fill(BLACK)

        #self.drawGrid(48)

        sur = pygame.Surface(self.trueSize)

        for x in range(10):
            for y in range(10):
                tiles.Tileset.draw(tiles.Dungeon, sur, (x*16,y*16), (x,y))

        self.win.blit(pygame.transform.scale(sur, self.size), (0, 0))

        pygame.display.update()


    def drawGrid(self, size = 16):
        for x in range(1, self.width // size+1):
            pygame.draw.line(self.win, [255]*3, (x*size, 0), (x*size, self.height), 1)
        for y in range(1, self.height // size+1):
            pygame.draw.line(self.win, [255]*3, (0, y*size), (self.width, y*size), 1)
        
g = Game()
g.run()

