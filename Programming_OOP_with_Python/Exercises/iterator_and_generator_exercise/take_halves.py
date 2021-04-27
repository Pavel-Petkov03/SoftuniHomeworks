def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        new_list = []
        times = 0
        for v in seq:
            new_list.append(v)
            if times == n - 1:
                break
            times += 1

        return new_list

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
