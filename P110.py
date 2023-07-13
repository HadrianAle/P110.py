import random
min_value=1
max_value=6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the die")
    print("The value is:")
    value=random.randint(min_value, max_value)
    print(value)
    roll_again = input("Input 'y' or 'yes' to roll the die again, press 'n' or 'no' to stop")
roll_stop = "no"
while roll_stop == "no" or roll_stop == "n":
    break
print("you have exited")
