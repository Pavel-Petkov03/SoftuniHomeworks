times = int(input())
import math


class Circle:
    def __init__(self, *args):
        self.x, self.y, self.r = args


class Triangle:
    def __init__(self, *args):
        self.ax, self.ay, self.bx, self.by, self.cx, self.cy = args


def check_condition(state):
    if all(state):
        return 'The circle is circumscribed and the center is inside.'
    elif state[0] is True and state[1] is False:
        return 'The circle is circumscribed and the center is outside.'
    elif state[0] is False and state[1] is True:
        return 'The circle is not circumscribed and the center is inside.'
    else:
        return 'The circle is not circumscribed and the center is outside.'


def make_main_logic(t: Triangle, c: Circle):
    final = [False, False]
    ax_expression = max(c.x, t.ax) - min(c.x, t.ax)
    ay_expression = max(c.y, t.ax) - min(c.y, t.ay)
    bx_expression = max(c.x, t.bx) - min(c.x, t.bx)
    by_expression = max(c.y, t.by) - min(c.y, t.by)
    cx_expression = max(c.x, t.cx) - min(c.x, t.cx)
    cy_expression = max(c.y, t.cy) - min(c.y, t.cy)
    first_direction = str(math.sqrt(ax_expression ** 2 + ay_expression ** 2))
    second_direction = str(math.sqrt(bx_expression ** 2 + by_expression ** 2))
    third_direction = str(math.sqrt(cx_expression ** 2 + cy_expression ** 2))
    if first_direction[:first_direction.index('.') + 2] == second_direction[
                                                           :second_direction.index('.') + 2] == third_direction[
                                                                                                :third_direction.index(
                                                                                                    '.') + 2]:
        final[0] = True
    if str(c.r) == first_direction[:first_direction.index('.') + 2] == second_direction[:second_direction.index(
            '.') + 2] == third_direction[:third_direction.index('.') + 2]:
        final[1] = True
    return final


for _ in range(times):
    circle = Circle(*list(map(float, ''.join(input().split('circle ')).split(', '))))
    triangle = Triangle(*list(map(float, ''.join(input().split('triangle ')).split(', '))))
    state = make_main_logic(triangle, circle)
    result = check_condition(state)
    print(result)

# по - голям (вадим)
