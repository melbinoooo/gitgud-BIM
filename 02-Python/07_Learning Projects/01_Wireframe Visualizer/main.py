# .self = "This"

# --------------------------------------
import pygame as pg
from model import *
from camera import *
from projection import *
#
from constants import *


# READ MODEL FILE FROM:
import os
os.chdir(r'02-Python\07_Learning Projects\01_Wireframe Visualizer')



class WireframeVisualizer:
    def __init__(self):
        pg.init()
        # LAUNCH APPLICATION
        # SET SCREEN RESOLUTION
        self.screen = pg.display.set_mode(RES)
        # SET FPS
        self.FPS = FPS
        # SET RUNTIME
        self.clock = pg.time.Clock()
        # INITIATE MODEL
        self.create_models()

    def build_UI(self):
        # BUILD UI
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()

    def create_models(self):
        # 1 INITIATE THE POV
        self.camera = Camera(self, [-5, 6, -55])
        # 2 LOAD THE MODEL VERTICES
        self.object = self.get_object_from_file('models/cat.obj')
        # 3 SET THE MODEL COORDINATE
        self.projection = Projection(self)
        # 4 THE MODEL VIEW ANGLE
        self.object.rotate_y(-math.pi / 4)
        
        


    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as file:
            for line in file:
                # .OBJ PARSER
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)



    def run(self):
        while True:
            self.build_UI()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = WireframeVisualizer()
    app.run()