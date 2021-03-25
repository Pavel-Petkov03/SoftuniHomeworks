# Вие сте режисьор на филма "Програмирането е забавно", като имате определено време за снимки. От вас се иска да напишете програма, с която ще разберете дали снимачният ден ще ви стигне да заснемете филма. Снимачният ден започва с подготовка на терен, което е 15 процента от времето за снимки! Филмът има определен брой сцени, които се заснемат за определено време.
# Вход
# От конзолата се четат 3 реда:
# 1.	Време за снимки – цяло число в диапазона [0… 1440]
# 2.	Брой сцени  – цяло число в диапазона [5… 25]
# 3.	Времетраене на сцена – цяло число в диапазона [20… 90]
# Изход
# На конзолата да се отпечата един ред:
# •	Ако времето за заснемане на филма ви стигне:
#   "You managed to finish the movie on time! You have {останало време} minutes left!"
# •	Ако времето НЕ ВИ стигне:
#   "Time is up! To complete the movie you need {нужно време} minutes."
# Останалото време да се закръгли до най-близкото цяло число.
from math import ceil
time_for_photo = int(input())
count_Of_scenes = int(input())
all_on_scene = int(input())
prapeiring_time = 0.15 * time_for_photo
time_we_need =  time_for_photo
time_we_have = count_Of_scenes * all_on_scene + prapeiring_time
if time_we_need >= time_we_have:
    print(f"You managed to finish the movie on time! You have {ceil(abs(time_we_have - time_we_need))} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {ceil(abs(time_we_have - time_we_need))} minutes.")

