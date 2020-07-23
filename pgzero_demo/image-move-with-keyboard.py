WIDTH = 600
HEIGHT = 400

# Load a sprite containing an image and assign it to a variable so we can access it later
rocket = Actor('rocketwhite')

def draw():
    screen.fill( (0, 128, 255) )
	# It's later. We'll call .draw() on rocket
    rocket.draw()

def on_key_down(key):
  if key == keys.W:
    rocket.y -= 1
  elif key == keys.S:
    rocket.y += 1
  elif key == keys.A:
    rocket.x -= 1
  elif key == keys.D:
    rocket.x += 1
