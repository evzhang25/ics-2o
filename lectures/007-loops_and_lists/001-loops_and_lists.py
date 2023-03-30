"""
LOOPS AND LISTS

Use loops and lists to draw things at specific points.
- row of trees
- bunch of clouds
- grid of windows
- lasers
- group of enemies
"""

import random

x_pos = []
y_pos = []

for x in range(50, 600, 100):
    y = random.randrange(300, 400)
    x_pos.append(x)
    y_pos.append(y)
print(x_pos)
print(y_pos)

for i in range(len(x_pos)):
    print(x_pos[i], y_pos[i])