WIDTH = 600
HEIGHT = 400

breathe_text = "Breathe in"

def text_change():
    global breathe_text

    if breathe_text == "Breathe in":
        breathe_text = "Exhale"
    else:
        breathe_text = "Breathe in"
    
clock.schedule_interval(text_change, 3)

def draw():
    screen.fill( (100, 200, 255))
    screen.draw.text(breathe_text, (50, 100))

# def on_mouse_down():
#     text_change()




