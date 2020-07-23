WIDTH = 800
HEIGHT = 600

yes = Actor('rocketpurple')
no = Actor('rocketwhite')

answer = ''
stage = 0

yes.bottomleft = 0, HEIGHT
no.bottomright = WIDTH, HEIGHT

def draw():
    global answer
    global stage
    screen.fill( (100, 100, 100))
    if stage == 0:
        screen.draw.text("Did you know that when wolves were brought\nback to Yellowstone, the overall environment improved?", (10, 10))
        if answer == 'yes':
            print("Print additional information to the console")
        if answer == 'no':
            print("Print other additional information to the console")
        if answer != '':
            answer = ''
            stage = 1
    if stage == 1:
        print("Welcome to stage 1!")
        # do something similar to stage 0
    yes.draw()
    no.draw()


def on_mouse_down(pos):
    global answer
    if yes.collidepoint(pos):
        print("Yes was chosen")
        answer = 'yes'
    if no.collidepoint(pos):
        print("No was chosen")
        answer = 'no'