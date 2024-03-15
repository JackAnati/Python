import os
import time
from termcolor import colored
import math

class Canvas:
    def __init__(self,width,height):
        self.x = width
        self.y = height
        self._canvas - [[' ' for y in range(self.y)] for x in range(self.x)]

    def hitsWall(self,point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y


    def setPos(self,pos,mark):
        self._canvas[round(pos[0])][round(pos[1])] - mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

   # def print(self):