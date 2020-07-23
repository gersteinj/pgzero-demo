WIDTH = 600
HEIGHT = 400

rocket = Actor('rocketwhite')
rocket.pos = WIDTH/2, HEIGHT/2

game_active = True

def draw():
    # this if statement determines
    # whether to draw a game over screen or the game
    if game_active:
        screen.fill( (0, 128, 255) )
        rocket.draw()
    else:
        screen.fill( (255, 0, 0) )
        screen.draw.text("GAME OVER", (10, 10))

def update():
    rocket.x += 1
    if rocket.left > WIDTH:
        rocket.right = 0

def on_mouse_down(pos, button):
    # editing a global variable, so this is important
    global game_active

    # if mouse is clicked on rocket, change game_active to false
    if rocket.collidepoint(pos):
        game_active = False