import numpy as np
import matplotlib.pyplot as plt

### Distance from origin
A = np.array([1,2,3,4,5]) # 5D vector
distance = np.linalg.norm(A)
print(distance) # distance of A from origin


### Eucledian Distance
A = np.array([1,2,3,4,5])
B = np.array([6,7,8,9,10])

differnce = A-B
print(differnce)

distance1 = np.linalg.norm(differnce) # type1
print(distance1)

distanceTemp = np.sum((A-B)**2) # type2
distance2 = distanceTemp**0.5
print(distance2)
print(distance1 == distance2) # comparing type1 and type2


### Mean Centering
data = np.random.rand(100, 2) # 100 2D vectors

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], label="Original Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Before Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show(block=False)
plt.pause(1)
plt.close()

data_mean = np.mean(data, axis=0)
print(data_mean)

centered_data = data - data_mean
print(centered_data)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], label="Original Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Before Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(centered_data[:, 0], centered_data[:, 1], label="Centered Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("After Mean Centering")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show(block=False)
plt.pause(1)
plt.close()



### Dot Product
A = np.array([1,2,3])
B = np.array([4,5,6])

print(np.dot(A,B))
print(A@B)
print(np.dot(A,B) == A@B)


### Cosine similarity
a = np.array([1,2,3])
b = np.array([-2,-4,-6])
c = np.array([2,4,6])

cosine_similarity = np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))
print("Cosine similarity between a and b",cosine_similarity)
cosine_similarity = np.dot(a,c)/(np.linalg.norm(a) * np.linalg.norm(c))
print("Cosine similarity between a and b",cosine_similarity)