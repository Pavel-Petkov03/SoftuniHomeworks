from collections import deque


class First:
    def __init__(self):
        self.males = list(map(int, input().split()))
        self.females = deque(map(int, input().split()))
        self.matches = 0

    def main(self):
        while self.males and self.females:
            if self.males[-1] <= 0:
                self.pop_male()
                continue
            if self.females[0] <= 0:
                self.pop_female()
                continue
            if self.remove_next_from_same_gender((self.males[-1], self.females[-1])) is None:
                continue
            if self.males[-1] == self.females[0]:
                self.matches += 1
                self.pop_male()
                self.pop_female()
            else:
                self.pop_female()
                self.males[-1] -= 2

    def pop_male(self):
        self.males.pop()

    def pop_female(self):
        self.females.popleft()

    def remove_next_from_same_gender(self, person):
        if person[0] % 25 == 0:
            self.pop_male()
            if self.males:
                self.pop_male()
                return
        if person[1] % 25 == 0:
            self.pop_female()
            if self.females:
                self.pop_female()
                return
        return True

    def print_result(self):
        result = [
            f"Matches: {self.matches}",
            f"Males left: {', '.join([str(male) for male in reversed(self.males)])}" if self.males else "Males left: none",
            f"Females left: {', '.join([str(female) for female in self.females])}" if self.females else "Females left: none",
        ]
        return '\n'.join(result)


f = First()
f.main()
print(f.print_result())