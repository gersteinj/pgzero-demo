WIDTH = 1200
HEIGHT = 800

black = Actor('rocketblack', (50, 50))
blue = Actor('rocketblue', (100, 20))
white = Actor('rocketwhite', (300, 150))
purple = Actor('rocketpurple', (400, 80))
donkey = Actor('donkey', (375, 60))

# now it's a list of dictinonaries
all_images = [
    {'img': black, 'xvel': 1, 'yvel': -1},
    {'img': blue, 'xvel': 0, 'yvel': 0},
    {'img': white, 'xvel': 2, 'yvel': 1},
    {'img': purple, 'xvel': -1, 'yvel': 2},
    {'img': donkey, 'xvel': 1, 'yvel': 1},
]

def draw():
    screen.fill((100,100,100))
    # use a for loop to repeat for all the items
    for img_dict in all_images:
        img_dict['img'].draw()

def update():
    # use a for loop to repeat for each item
    for img_dict in all_images:
        img_dict['img'].x += img_dict['xvel']
        img_dict['img'].y += img_dict['yvel']
