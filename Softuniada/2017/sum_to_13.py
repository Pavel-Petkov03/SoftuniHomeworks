# operations = 0
# dup = None
#
#
# def duplicates(word):
#     while True:
#         is_continue = False
#         for i in range(len(word) - 1):
#             if word[i] == word[i+1]:
#                 word = word[:i] + word[i + 2:]
#                 global operations
#                 operations += 1
#                 is_continue = True
#                 break
#         if is_continue:
#             continue
#
#         break
#     if not word:
#         return 'Empty String'
#     return word
#
# print(duplicates(input()))
# print(f'{operations} operations ')
def create_cube(n):
    cube = []
    for _ in range(n):
        cube.append([list(l) for l in input().split(' | ')])
    return cube


class MoveTheSnake:
    def __init__(self):
        self.cube_size = int(input())
        self.cube = create_cube(self.cube_size)
        self.initial_task = input()
        self.points = 0
        self.initial_pos = self.entry_pos()

    def down(self, steps):
        self.initial_pos[1] += steps

    def up(self, steps):
        self.initial_pos[2] -= steps

    def left(self, steps):
        self.initial_pos[2] -= steps

    def right(self, steps):
        self.initial_pos[2] += steps

    def forward(self, steps):
        self.initial_pos[0] -= steps

    def backward(self, steps):
        self.initial_pos[0] += steps

    def entry_pos(self):
        for matrix in range(len(self.cube)):
            for row in range(len(self.cube[matrix])):
                for col in range(len(self.cube[matrix][row])):
                    if self.cube[matrix][row][col] == 's':
                        return [matrix, row, col]

    def check_if_state_to_eat(self):
        m = self.initial_pos[0]
        r = self.initial_pos[1]
        c = self.initial_pos[2]
        if self.cube[m][r][c] == 'a':
            self.points += 1

    def __validate(self, pos):
        if 0 <= self.find_dimension(pos) < self.cube_size:
            return False
        return True

    def find_dimension(self, pos):
        if pos in ['forward', 'backward']:
            return self.initial_pos[0]
        elif pos in ['right', 'left']:
            return self.initial_pos[2]
        else:
            return self.initial_pos[1]

    def make_main_logic(self):
        while self.initial_task != 'end':
            pos, _, steps, _ = input().split()
            steps = int(steps)
            self.movement_wrapper(self.initial_task, steps)
            if not self.__validate(self.initial_task):
                return f'Points collected: {self.points}\nThe snake dies.'
            self.check_if_state_to_eat()
            self.initial_task = pos

        return f'Points collected: {self.points}'

    def movement_wrapper(self, pos, steps):
        if pos == 'forward':
            self.forward(steps)
        elif pos == 'backward':
            self.backward(steps)
        elif pos == 'up':
            self.up(steps)
        elif pos == 'down':
            self.down(steps),
        elif pos == 'left':
            self.left(steps),
        elif pos == 'right':
            self.right(steps)


m = MoveTheSnake()
print(f'{m.make_main_logic()}')


