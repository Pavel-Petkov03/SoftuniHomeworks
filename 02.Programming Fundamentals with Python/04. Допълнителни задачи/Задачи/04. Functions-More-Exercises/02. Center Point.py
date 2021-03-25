# You are given the coordinates of two points on a Cartesian coordinate system
# - X1, Y1, X2 and Y2. Create a method that prints the point that is
# closest to the center of the coordinate system (0, 0) in the format
# (X, Y). If the points are on a same distance from the center, print
# only the first one. The resulting coordinates must be formated to the lowest integer

def cord(x1 , y1 , x2 , y2):
    first_sum = abs(x1) + abs(y1)
    second_sum = abs(x2) + abs(y2)
    if first_sum >= second_sum:
        return f"({int(x2)}, {int(y2)})"
    else:
        return f"({int(x1)}, {int(y1)})"

our_x1 = float(input())
our_y1 = float(input())
our_x2 = float(input())
our_y2 = float(input())
print(cord(our_x1 , our_y1 , our_x2 , our_y2))

