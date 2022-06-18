#
# ------------------------------

import pygame as pg
from model_3d import *


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0]) #WCS
        self.forward = np.array([0,0,1,1]) # Z
        self.up = np.array([0,1,0,1]) # Y
        self.right = np.array([1,0,0,1]) # X
        # Parameter for Camera FOV | Horizontal = Landscape | Vertical = Portrait
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.height / render.width)
        # Parameter for  Clipping Planes
        self.near_plane = 0.1
        self.far_plane = 100
        
    def translate_matrix(self):
        x, y, z, w = self.position
        return np.array([
            [1,0,0,0], # X 
            [0,1,0,1], # Y 
            [0,0,1,0], # Z 
            [-x,-y,-z,1] # WCS
        ])
        
    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0,0,0,1]
        ])
    
    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
