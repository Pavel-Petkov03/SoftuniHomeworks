# You are given the coordinates of four points in the 2D plane.
# The first and the second pair of points form two different lines.
# Print the longer line in format "(X1, Y1)(X2, Y2)" starting with the point that is closer
# to the center of the coordinate system (0, 0) (You can reuse the method that you wrote for
# the previous problem). If the lines are of equal length, print only the first one.
# The resulting coordinates must be formated to the lowest integer.
def cordinates(first_x1 , first_y1 , first_x2, first_y2 , second_x1 , second_y1 ,second_x2 ,second_y2 ):
    first_result = (abs(first_x1) + abs(first_x2)) ** 2 + abs((first_y1 - first_y2)**2)
    second_result = (abs(second_x1) + abs(second_x2)) ** 2 + abs((second_y1 - second_y2)**2)
    if first_result >= second_result:
        x1 = our_first_x1
        x2 = our_first_x2
        y1 = our_first_y1
        y2 = our_first_y2

    else:
        x1 = our_second_x1
        x2 = our_second_x2
        y1 = our_second_y1
        y2 = our_second_y2
    first_sum = abs(x1) + abs(y1)
    second_sum = abs(x2) + abs(y2)
    if first_sum > second_sum:
        return f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})"
    else:
        return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"


our_first_x1 = float(input())
our_first_y1 = float(input())
our_first_x2 = float(input())
our_first_y2 = float(input())
our_second_x1 = float(input())
our_second_y1 = float(input())
our_second_x2 = float(input())
our_second_y2 = float(input())
print(cordinates(our_first_x1 , our_first_y1 , our_first_x2, our_first_y2 , our_second_x1 , our_second_y1 , our_second_x2 , our_second_y2))

















































































































































































































































































































