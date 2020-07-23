WIDTH = 600
HEIGHT = 400

rocket = Actor('rocketpurple')

def draw():
    screen.fill((20, 0, 50))
    rocket.draw()

def on_mouse_down(pos):
    rocket.pos = pos   # rocket pos is set to mouse position
