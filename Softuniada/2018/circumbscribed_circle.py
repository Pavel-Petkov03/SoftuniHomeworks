times = int(input())
import math


class Circle:
    def __init__(self, *args):
        self.x, self.y, self.r = args


class Triangle:
    def __init__(self, *args):
        self.ax, self.ay, self.bx, self.by, self.cx, self.cy = args


def check_circumscribed(t: Triangle, c: Circle):
    ax_expression = max(c.x, t.ax) - min(c.x, t.ax)
    ay_expression = max(c.y, t.ax) - min(c.y, t.ay)
    bx_expression = max(c.x, t.bx) - min(c.x, t.bx)
    by_expression = max(c.y, t.by) - min(c.y, t.by)
    cx_expression = max(c.x, t.cx) - min(c.x, t.cx)
    cy_expression = max(c.y, t.cy) - min(c.y, t.cy)
    first_direction = math.sqrt(ax_expression ** 2 + ay_expression ** 2)
    second_direction = math.sqrt(bx_expression ** 2 + by_expression ** 2)
    third_direction = math.sqrt(cx_expression ** 2 + cy_expression ** 2)
    if f'{first_direction:.2f}' == f'{second_direction:.2f}' == f'{third_direction:.2f}':
        return True
    return False


for _ in range(times):
    circle = Circle(*list(map(float, ''.join(input().split('circle ')).split(', '))))
    triangle = Triangle(*list(map(float, ''.join(input().split('triangle ')).split(', '))))
    is_circumscribed = check_circumscribed(triangle, circle)
    print(is_circumscribed)


# по - голям (вадим)