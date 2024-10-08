# you are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height * wall width)% coverage per can.
# Height = 2, width = 4 and coverage = 5
# number of cans = (2*4)/5  =  1.6
#  But becouse you can't buy 0.6 of can of paint, the result should be rounded up to 2 cans.

import math

def paint_calc(height, width, cover):
    area = height*width
    number_of_cans = math.ceil(area/cover)
    print(f"you will need {number_of_cans} cans of paint.")




test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)