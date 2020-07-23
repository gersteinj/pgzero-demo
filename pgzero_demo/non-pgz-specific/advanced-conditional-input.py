
yes_answers = ['yes', 'yep', 'y', 'usually', 'always', 'yeah']
no_answers = ['no', 'nope', 'never', 'rarely']

response = input("Do you recycle? ")

# do you recycle => yes, yep, yeah, y, usually, always, of course
# do you recycle => no, nope, never, rarely

while response.lower() not in yes_answers and response.lower() not in no_answers:
    response = input("I'm sorry, your answer wasn't very clear\nDo you recycle? ")

if response.lower() in yes_answers:
    print("That's great!")
elif response.lower() in no_answers:
    print("Booooooooo")
