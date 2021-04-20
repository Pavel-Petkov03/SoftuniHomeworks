def vowel_filter(func):
    vowels = set('aeouyi' + 'aeouyi'.upper())

    def wrapper():

        return [x for x in func() if x in vowels]

    return wrapper
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())


