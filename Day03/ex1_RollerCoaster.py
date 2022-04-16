print("Welcome to the RollerCoaster ! \n")
height = int(input("What is your height in cm? "))

if height >= 120 :
    print("You can ride the rollerCoaster !")
    age = int(input("what is your age ? "))
    if (age >= 18) :
        print("You should pay 12$.")
    elif age>=12 and age <= 18:
        print("you should pay 7$.")
    else :
        print("You should pay 5$.")
else :
    print("Sorry you have to grow taller before you van ride !")