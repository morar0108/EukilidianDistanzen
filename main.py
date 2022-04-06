import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance
import random

# In the world of mathematics, the shortest distance between two points in any dimension is termed the Euclidean
# distance. It is the square root of the sum of squares of the difference between two points.

points = []
listDistance = []
for i in range(100):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    # We can also directly implement the mathematical formula using the numpy module. For this method, we will use
    # the numpy.sum() function, which returns the sum of elements, and the numpy.square() function will return the
    # square of the elements.
    dist = np.sqrt(np.sum(np.square(x - y)))
    print("Euklidische Distanz zwischen ", x, " und ", y, " = ", dist)
    plt.scatter(x, y)
    point = [x, y]
    points.append(point)
    for j in range(i):
        # Use the distance.euclidean() Function to Find the Euclidean Distance Between Two Points
        distanz = distance.euclidean(points[j], points[i])
        listDistance.append(distanz)
print(listDistance)
plt.show()
