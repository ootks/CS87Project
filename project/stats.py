import matplotlib.pyplot as plt
import numpy as np
import math

with open("data/scores/top_1000_posts.txt") as g:
    scores = [int(line.split("")[1]) for line in g]

scores = [math.log(score) for score in scores if score > 0]
scores = [math.log(score) for score in scores if score > 0]


plt.hist(scores, bins = 50)
plt.ylabel('scores')

plt.show()
