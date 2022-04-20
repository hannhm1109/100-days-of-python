import random

names_string = input("Give me everybody's name seperated by a comma. \n")

names =  names_string.split(", ")

lenght = len(names)

random_name = random.randint(0,lenght - 1)
who_will_pay = names[random_name]

print(f"{who_will_pay} is going to buy the meal today.")