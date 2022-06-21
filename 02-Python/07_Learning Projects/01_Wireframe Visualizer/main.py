# .self = "This"

# --------------------------------------
import pygame as pg
from model import *
from utility_camera import *
from utility_projection import *
#
from constants import *


# READ MODEL FILE FROM:
import os
os.chdir(r'02-Python\07_Learning Projects\01_Wireframe Visualizer')



class WireframeVisualizer:
    def __init__(self):
        # INITIALIZE PYGAME
        pg.init()
        # APP LAUNCHER
        # SET APP TITLE
        pg.display.set_caption('Wireframe Visualizer')
        # SET APP SCREEN RESOLUTION
        self.screen = pg.display.set_mode(RES)
        # SET APP RUNTIME
        self.clock = pg.time.Clock()
        # INITIATE MODEL
        self.launch_model()


    def get_object_from_file(self, filename):
        vertex, edges = [], []
        with open(filename) as file:
            for line in file:
                # .OBJ PARSER
                # ALL LINE STARTS WITH 'f' DETERMINES VERTICES VALUE
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                # ALL LINE STARTS WITH 'f' DETERMINES FACES VALUE
                elif line.startswith('f'):
                    edges_ = line.split()[1:]
                    edges.append([int(face_.split('/')[0]) - 1 for face_ in edges_])
        return Model3D(self, vertex, edges)


    def launch_model(self):
        # 1 INITIATE THE POV
        self.camera = Camera(self, [-5, 6, -55])
        # 2 LOAD THE MODEL VERTICES
        self.model = self.get_object_from_file('models/cat.obj')
        # 3 SET THE MODEL COORDINATE
        self.projection = Projection(self)
        # 4 THE MODEL VIEW ANGLE
        self.model.rotate_y(-math.pi / 4)
        
        
    def build_UI(self):
        # BUILD UI
        # SET FRAMERATE
        self.clock.tick(FPS)
        # UPDATE ONLY THE DISPLAYING AREA
        pg.display.flip()
        # SET BG COLOR
        self.screen.fill(pg.Color(C_BLACK))
        # GET MODEL AND RUN BUILD EXTENTION FUNCTION
        self.model.build()



# APP RUNNER
    def run(self):
        running = True
        while running:
            # WHILE APP IS RUNNING: BUILD UI
            self.build_UI()
            # WHILE APP IS RUNNING: ENABLE CAMERA CONTROL
            self.camera.control()
            # CHECK IF APP IS RUNNING:
            for event in pg.event.get():
                # IF PRESSED 'CLOSED/EXIT' TERIMINATE APP
                if event.type == pg.QUIT:
                    running = False


if __name__ == '__main__':
    # INITIALIZE THE RUN METHOD TO THE WireframeVisualizer CLASS
    WireframeVisualizer().run()