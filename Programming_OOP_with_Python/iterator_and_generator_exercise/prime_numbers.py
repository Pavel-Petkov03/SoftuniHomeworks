def gen(all_nums):
    for num in all_nums:
        is_prime = True
        for check in range(2, num):
            if num % check == 0:
                is_prime = False
        if is_prime and num != 0:
            yield num


def get_primes(all_nums):
    return (x for x in all_nums if len([x for d in range(2, x) if x % d == 0]) == 0 and x != 0)


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
