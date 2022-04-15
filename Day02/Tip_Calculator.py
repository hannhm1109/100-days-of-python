#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. 

print("welcome to the tip calculator !\n")
bill =float(input("what was the total bill ? $"))
tip = int(input("what pourcentage tip would you like to give ? 10, 12 or 15 ?\n"))
people = int(input("how many people to split the bill ?"))
sum = ((bill * ((tip / 100)))) / (people)
roundd = round(sum,2)
print("Each person should pay : \n")
print(roundd)