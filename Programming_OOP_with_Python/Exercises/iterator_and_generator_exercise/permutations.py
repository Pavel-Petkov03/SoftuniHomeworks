from itertools import permutations as permutes


def possible_permutations(array):
    return (list(perm) for perm in permutes(array))


[print(n) for n in possible_permutations([1, 2, 3, 4])]
