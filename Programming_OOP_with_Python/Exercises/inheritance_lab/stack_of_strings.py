class Stack:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f'[{", ".join([str(c) for c in reversed(self.data)])}]'

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

