# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water",
# "Fish", and "Sun" appear (case insensitive).
word = input().lower()
times = 0
if 'water' in word:
    times += word.count("water")
if 'fish' in word:
    times += word.count("fish")
if "sand" in word:
    times += word.count( "sand" )
if "sun" in word:
    times += word.count( "sun" )
print(times)