print("You go to the beach, and you see lots of trash on the shoreline.")

response = input("What do you do?")

if response.lower() == 'pick it up':
    print("You're a good person and you understand that the environment smiles down on you.")

    # scenario b
    response = input("Do you save the baby bird? ")

    if response.lower() == 'of course':
      print("thank you")
    else:
      print("You're mean")
    

if response.lower() == 'kick it':
    print("I am at a loss for words. Do you realize you have an opportunity to save an animal's life?")

    response = input("Why? ")

    if response.lower() == "it was a mistake":
      print("oh, okay")
    else:
      print("That's not good a reason")

