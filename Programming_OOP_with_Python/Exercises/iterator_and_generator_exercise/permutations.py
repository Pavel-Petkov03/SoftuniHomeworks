from itertools import permutations


def possible_permutations(array):
    return (list(perm) for perm in permutations(array))


[print(n) for n in possible_permutations([1, 2, 3])]
