print(" welcome to the love calculator !")
name1 = input("What is your name ? \t")
name2 = input("What is their name ? \t")

name3 = name1 + name2
name3 = name3.lower()

print("how many time each letter of true love appeared in both names combined ?\n")
t = name3.count('t')
r = name3.count('r')
u = name3.count('u')
e = name3.count('e')

true = t + r + u + e

l = name3.count('l')
o = name3.count('o')
v = name3.count('v')
e = name3.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print("Your score is {love_score}")
   