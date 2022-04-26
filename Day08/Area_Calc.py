import math

def paint_calc(height, width , cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You will need {number_of_cans} cans of paint.")



test_h = int(input("Height of Wall : \n"))
test_w = int(input("Width of Wall : \n"))
coverage = 5

paint_calc(height = test_h, width= test_w , cover = coverage)