import pygame
import os


class Tileset:
    def draw(self, surface, pos, tile):
        surface.blit(self.tileset, pos, (tile[0]*self.size[0],tile[1]*self.size[1],self.size[0],self.size[1]))

class Dungeon:
    tileset = pygame.image.load(os.path.join("assets","Dungeon_Tileset.png"))
    size = (16, 16)

