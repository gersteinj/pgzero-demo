WIDTH = 600
HEIGHT = 400

# Load a sprite containing an image and assign it to a variable so we can access it later
rocket = Actor('rocketwhite')
rocket.pos = WIDTH/2, HEIGHT/2

def draw():
    screen.fill( (0, 128, 255) )
    rocket.draw()

def on_mouse_down(pos):
    if rocket.collidepoint(pos):
        print("You touched the rocket!")
        set_grey_rocket()
        clock.schedule_unique(set_white_rocket, 1.5)
        rocket.angle += 15
    else:
        print(f"Sorry, {pos} wasn't the right location")

def set_white_rocket():
    rocket.image = 'rocketwhite'

def set_grey_rocket():
    rocket.image = 'rocketgrey'

def update():
    rocket.x += 3
    
    if rocket.left >= WIDTH:
        rocket.right = 0
