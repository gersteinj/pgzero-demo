WIDTH = 600
HEIGHT = 400

rocket = Actor('rocketpurple')
goal = Actor('donkey', bottomright = (WIDTH, HEIGHT))


def draw():
    screen.fill((20, 0, 50))
    goal.draw()
    rocket.draw()

def on_mouse_move(pos, buttons):
    # Each time the mouse moves, assign the
    # mouse's position to be the new rocket position
    if rocket.collidepoint(pos) and mouse.LEFT in buttons:
        rocket.pos = pos  
        if goal.collidepoint(pos):
            print("YOU WIN!")
