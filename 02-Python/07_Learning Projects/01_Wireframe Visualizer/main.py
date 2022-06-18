# Import pygame and numpy library using
# pip install pygame numpy 
# ------------------------------
import sys
sys.path.append("..")
import pygame as pg
from Models.model_3d import * # Import from Models folder the model_3d.py
from Utilities.camera_helper import * # Import from Utilities folder the camera_helper.py
from Utilities.projection_helper import * # Import from Utilities folder the projection_helper.py


# Create Class for WireframeVisualizer ("The app")

class WireframeVisualizer:
    # Define APP display resolutions
    width = 960
    height = 600
    fps = 60

    def __init__(self):
        pg.init() # Initialize pygame
        self.res = self.width, self.height 
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.create_models() # Call the imported create_model instance.
        
    # Object for UI
    def draw(self):
        # Set App Name // show fps
        # pg.display.set_caption('WIREFRAME VISUALIZER')
        pg.display.set_caption(str(self.clock.get_fps()))
        # Define APP background color
        self.screen.fill(pg.Color(61, 61, 61))
        # Display a portion of the screen to be updated only.
        pg.display.flip()
        # Runtime
        self.clock.tick(self.fps)
        # Call the model instance
        self.model.draw()

    # Object for Runner
    def run(self):
        running = True
        while running:
            # Display UI
            self.draw()
            # Run while loop to check if the app is running.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
    
    # Create an instance for the Model3D
    def create_models(self):
        # Import the camera utility and Add a starting coordinate
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        # Import model
        self.model = Model3D(self)
        # Set model view / angle
        self.model.translate([0.2,0.4,0.2])
        self.model.rotate_y(math.pi / 6)


# Main
if __name__ == '__main__':
    app = WireframeVisualizer()
    app.run()

