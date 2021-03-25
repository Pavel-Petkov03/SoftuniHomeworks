# Create a function called get_magic_triangle which will receive a single parameter
# (integer n) and it should create a magic triangle which follows those rules:
# •	We start with this simple triangle [[1], [1, 1]]
# •	We generate the next rows until we reach n amount of rows
# •	Each number in each row is equal to the sum of the two numbers right above it in the triangle
# •	If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5

def get_magic_triangle(n, a=[[1]]):
    if n == 1:
        return a

    current = a[-1]
    helper = []
    for adding in range(len(a[-1]) + 1):
        if adding in range(len(current)) and adding - 1 in range(len(current)):
            add_sum = current[adding] + current[adding - 1]
            helper.append(add_sum)
        else:
            helper.append(1)
    a.append(helper)
    return get_magic_triangle(n - 1, a)


print(get_magic_triangle(5))
