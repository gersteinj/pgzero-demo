response = input("What do you choose? > ")

if response.lower() == 'yes':
    print("Great, you survive")
elif response.lower() == 'no':
    print("Sorry, a bear ate you")
else:
    print("You were too indecisive and a bear ate you while you were making up your mind")