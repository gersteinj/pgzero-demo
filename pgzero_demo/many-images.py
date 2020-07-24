WIDTH = 1200
HEIGHT = 800

black = Actor('rocketblack', (50, 50))
blue = Actor('rocketblue', (100, 20))
white = Actor('rocketwhite', (300, 150))
purple = Actor('rocketpurple', (400, 80))
donkey = Actor('donkey', (375, 60))

all_images = [black, blue, white, purple, donkey]

# alternate way of creating the list
# all_images = [
#     Actor('rocketblack', (50, 50)),
#     Actor('rocketblue', (100, 20)),
#     Actor('rocketwhite', (300, 150)),
#     Actor('rocketpurple', (400, 80)),
#     Actor('donkey', (375, 60))
# ]

def draw():
    screen.fill((100,100,100))
    # use a for loop to repeat for all the items
    for img in all_images:
        img.draw()
