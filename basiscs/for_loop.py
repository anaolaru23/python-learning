"""
Countdown example using a for loop and time.sleep.
Demonstrates range with a negative step.
"""

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print("Happy New Year!")
