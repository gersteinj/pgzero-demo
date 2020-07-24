WIDTH = 600
HEIGHT = 400

stage = 0

donkey = Actor('donkey')
donkey.bottomright = (WIDTH, HEIGHT)
ship = Actor('rocketwhite')
button = Actor('rocketpurple')

def draw():
    screen.fill( (20,0,50))
    button.draw()
    if stage == 0:
        donkey.draw()
    else:
        ship.draw()

def update():
    if stage == 0:
        donkey.x -= 1
        if donkey.right < 0:
            donkey.left = WIDTH
    else:
        ship.x -= 1
        if ship.right < 0:
            ship.left = WIDTH

def on_mouse_down(pos):
    global stage
    if button.collidepoint(pos) and stage == 0:
        stage = 1
        ship.center = donkey.center