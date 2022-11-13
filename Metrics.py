from math import sqrt
import numpy as np

#   ^
#   |
# y |
#   |
#   |
# 5 |      *(5,2)
# 4 |		
# 3 |		 
# 3 |		  
# 2 |           *(2,4)
# 1 |    
#  -|-------------------------->
#   |  1  2  3  4		     x


p = [5, 2] 
q = [2, 4]

a = np.array(p)
b = np.array([0,0])
c = np.array(q)

ba = a - b
bc = c - b


# d =  ((p1 - q2)^2 + (p2 - q2)^2)^1/2
d = sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
print("Eucledian distance: ",d)

# d = | p2 - p1 | + | q2 - q1 |
d = abs(p[1]-p[0]) + abs(q[1]-q[0])
print("Manhattan distance: ", d)

# d = max (|p - y|)
d = max( abs(p[0] - q[0]), abs(p[1] - q[1]) )
print("Chebyshev distance: ",d)

# d = sum (|p - q|^2)^(1/p)
p=2
d = np.sum(np.abs(a-c)**p)**(1/p)
print("Minkowski distance: ", d)


s1 = "karolin"
s2 = "manhattan"
result = 0
for x, (i, j) in enumerate(zip(s1, s2)):
	if i != j:
		result += 1

print("Hamming distance :  ", result)


cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print("Cosine distance  :  ",np.degrees(angle),u"\u00B0")
