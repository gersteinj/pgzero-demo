WIDTH = 600
HEIGHT = 400

rocket = Actor('rocketpurple')

def draw():
    screen.fill((20, 0, 50))
    rocket.draw()

def on_mouse_move(pos):
    # Each time the mouse moves, assign the
    # mouse's position to be the new rocket position
    rocket.pos = pos  
