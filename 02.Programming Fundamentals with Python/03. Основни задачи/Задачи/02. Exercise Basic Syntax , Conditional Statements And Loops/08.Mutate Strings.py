first_string = input()
second_string = input()
previous_word = first_string
for index in range( 0, len( first_string ) ):
    new_word = ''
    for i in range( 0, index + 1 ):
        new_word += second_string[i]
    for j in range( index + 1, len( first_string ) ):
        new_word += first_string[j]
    if new_word != previous_word:
        print( new_word )
        previous_word = new_word
