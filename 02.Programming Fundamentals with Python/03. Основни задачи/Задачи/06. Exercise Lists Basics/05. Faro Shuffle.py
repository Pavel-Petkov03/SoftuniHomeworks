# A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then
# the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the
# bottom and the original top card is still on top.
# For example, faro shuffling the list
# ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives
# a number of faro shuffles that have to be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number
cards = input().split()
times_of_shuffle = int(input())
half = len(cards) // 2
for times in range(times_of_shuffle):
    right_list = []
    left_list = []
    left_symbol = cards[0]
    right_symbol = cards[-1]
    shuffle_list = []
    for index in range( 1, half ):
        left_list.append( cards[index] )
    for index in range( half, len( cards ) - 1 ):
        right_list.append( cards[index] )
    for index in range( len( right_list ) ):
        shuffle_list.append(right_list[index] )
        shuffle_list.append(left_list[index] )
    cards = shuffle_list.copy()
    cards.append( right_symbol )
    cards.insert(0, left_symbol)
print(cards)



