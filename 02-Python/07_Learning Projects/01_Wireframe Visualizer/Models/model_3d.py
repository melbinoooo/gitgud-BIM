#
# ------------------------------

import pygame as pg
from ..Utilities.matrix_helper import *

class Model3D:
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([
            (0,0,0,1), # 0 Vertex Sitting on the WCS | # 0 Index
            (0,1,0,1), # 1 Vertex | # 1 Index
            (1,1,0,1), # 2 Vertex | # 2 Index
            (1,0,0,1), # 3 Vertex | # 3 Index
            (0,0,1,1), # 4 Vertex | # 4 Index
            (0,1,1,1), # 5 Vertex | # 5 Index
            (1,1,1,1),# 6 Vertex | # 6 Index
            (1,0,1,1) # 7 Vertex | # 7 Index
        ])
        
        # Get face's vertixes using above's indexing
        # [0, -> Index 0 and embedded with it's coordinates
        #  1, -> Index 1 and embedded with it's coordinates
        #  2, -> Index 2 and embedded with it's coordinates
        #  3] -> Index 3 and embedded with it's coordinates
        self.faces = np.array([
            # Connecting the edges from each indexes's coordinates
            (0,1,2,3), 
            (4,5,6,7),
            (3,2,6,7),
            (0,1,5,4),
            (0,4,7,3),
            (1,5,2,6)
        ])
    
    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)
    
    def scale(self, scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)
    
    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ rotate_x(angle)
        
    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ rotate_y(angle)
        
    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ rotate_z(angle)
        
    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1,1)
        vertexes[(vertexes > 1) | (vertexes < -1)] = 0
