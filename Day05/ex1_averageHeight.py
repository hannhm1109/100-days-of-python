sum = 0
students_heights = input("input a list of student heights ").split()


for n in range(0, len(students_heights)) :
  students_heights[n] = int(students_heights[n])
  sum = sum + students_heights[n]
print(students_heights)
print(sum)

average = round(sum / len(students_heights))

print(average)