# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time, the time it needs to process a product. When a robot is free
# it should take a product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each
# second (so the first product should appear at [start time + 1 second]). If a product passes the line and
# there is not a free robot to take it, it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.
# Input
# •	On the first line, you will get the names of the robots and their processing times in format
# "robotName-processTime;robotName-processTime;robotName-processTime"
# •	On the second line, you will get the starting time in format "hh:mm:ss"
# •	Next, until the "End" command, you will get a product on each line.


from collections import deque
from datetime import datetime, timedelta
data = input().split(";")
robots = {sub.split("-")[0]: int(sub.split("-")[1]) for sub in data}
available_robots = {k: 0 for k in robots}
tasks = deque()
timed = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=1)
command = input()
while command != "End":
    tasks.append(command)
    command = input()

while tasks:
    available = [k for k, v in available_robots.items() if v <= 0]
    if available:
        print(f"{available[0]} - {tasks.popleft()} [{timed.strftime( '%H:%M:%S' )}]")
        available_robots[available[0]] = robots[available[0]]
        timed += timedelta(seconds=1)
        available_robots = {k: v - 1 for k, v in available_robots.items()}
    else:
        while not available:
            tasks.append(tasks.popleft())
            available_robots = {k: v - 1 for k, v in available_robots.items()}
            timed += timedelta(seconds=1)
            available = [k for k, v in available_robots.items() if v <= 0]