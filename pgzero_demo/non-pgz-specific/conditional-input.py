response = input("What do you choose? > ")

# branching lots of directions
if response.lower() == 'tent':
    print("Great, you survive")
elif response.lower() == 'sleep':
    print("Sorry, a bear ate you")
elif response.lower() == 'berries':
    print('Sorry, the berries were poisonous')
else:
    print("You were too indecisive and a bear ate you while you were making up your mind")