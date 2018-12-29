#!/usr/bin/python

import numpy as np

class1 = np.array([
      np.array([[1,2]]).T,
      np.array([[2,3]]).T,
      np.array([[3,3]]).T, 
      np.array([[4,5]]).T,
      np.array([[5,5]]).T
])
class2 = np.array([
      np.array([[1,0]]).T,
      np.array([[2,1]]).T,
      np.array([[3,1]]).T, 
      np.array([[3,2]]).T,
      np.array([[5,3]]).T,
      np.array([[6,5]]).T
])

mi1 = np.sum(class1, axis = 0) / float(len(class1))
mi2 = np.sum(class2, axis = 0) / float(len(class2))

print("Mi1: {mi1}\nMi2: {mi2}".format(mi1 = mi1, mi2 = mi2))

S1 = mi1 - mi1
S2 = mi1 - mi1 

for sam in class1:
    S1 = S1 + np.matmul((sam - mi1),((sam - mi1).T))
for sam in class2:
    S2 = S2 + np.matmul((sam - mi2), ((sam - mi2).T))

print("S1: {s1}\nS2: {s2}".format(s1 = S1, s2 = S2))
Sw = S1 + S2
w = (np.matmul(np.linalg.inv(Sw) ,(mi1-mi2)))
print(w)

