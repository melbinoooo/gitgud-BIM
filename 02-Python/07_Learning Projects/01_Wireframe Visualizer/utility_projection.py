import math
import numpy as np
from constants import *


class Projection:
    def __init__(self, render):
        NEAR = render.camera.near_plane
        FAR = render.camera.far_plane
        RIGHT = math.tan(render.camera.h_fov / 2)
        LEFT = -RIGHT
        TOP = math.tan(render.camera.v_fov / 2)
        BOTTOM = -TOP


        mt0 = 2 / (RIGHT - LEFT)
        mt1 = 2 / (TOP - BOTTOM)
        mt2 = (FAR + NEAR) / (FAR - NEAR)
        mt3 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [mt0, 0, 0, 0],
            [0, mt1, 0, 0],
            [0, 0, mt2, 1],
            [0, 0, mt3, 0]
        ])


        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])