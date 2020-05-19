# Building a CMD DIce SImulator Program - 5/19/2020
import random

print("This is a Dice Rolling Simulator!")

user_roll = "y"
#checking program's logic
while user_roll == "y":
    random_number = random.randint(1,52)
    if random_number == 1:
        print("{----------------}")
        print("{|      0      | }")
        print("{|             | }")
        print("{----------------}")

    if random_number == 2:
        print("{----------------}")
        print("{       00       }")
        print("{                }")
        print("{----------------}")

    if random_number == 3:
        print("{----------------}")
        print("{       0 0       }")
        print("{        0       }")
        print("{----------------}")

    if random_number == 4:
        print("{----------------}")
        print("{       0 0      }")
        print("{       0 0      }")
        print("{----------------}")

    if random_number == 5:
        print("{----------------}")
        print("{       0 0      }")
        print("{       0 0      }")
        print("{        0       }")
        print("{----------------}")

    if random_number == 6:
        print("{----------------}")
        print("{       0 0 0    }")
        print("{       0 0 0    }")
        print("{                }")
        print("{----------------}")
    user_roll = input("Press y to roll and any other number to end the program: ")