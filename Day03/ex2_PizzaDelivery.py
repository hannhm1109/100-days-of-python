print("welcome to python pizza deliveries !")
size = input("what size of pizza do you want ? S,M,L \n")

bill = 0

if (size == 'S'):
  bill += 15
elif (size == 'M'):
  bill += 20
else:
  bill += 25

add_pepperoni = input("Do you want pepperoni ?")
if (add_pepperoni == 'Y') :
  if (size == 'S'):
    bill += 2
  if (size == 'M' or size == 'L') :
    bill += 3

extra_cheese = input("do you want extra cheese ?")
if (extra_cheese == 'Y') :
  bill += 1

print(f"your total bill is ${bill}")