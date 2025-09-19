import random
playing = True
number = str(random.randint(1,20))
print("the dice of death will roll soon if it lands on the number of your choosing you may survive temporarily")
print("the dice has 20 sides and the game nevere ends...")
while playing:
    guess = int(input("enter your number and fate will choose if you survive: \n"))
    if number == guess:
        print("you survive for now....")
        print("the number was ", number)
        break
    else:
        print("ok get in the torture pit time to die...")