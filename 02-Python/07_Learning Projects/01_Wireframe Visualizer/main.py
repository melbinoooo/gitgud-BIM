# Import pygame and numpy library using
# pip install pygame numpy 
# ------------------------------
import pygame as pg


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


# Main
if __name__ == '__main__':
    app = WireframeVisualizer()
    app.run()

