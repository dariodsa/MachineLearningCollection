#!/usr/bin/python
import numpy as np

DIM = 2

classes = [
   np.array([
      np.array([[2,0]]).T,
      np.array([[4,0]]).T
   ]),
   np.array([
      np.array([[0,-2]]).T,
      np.array([[0,-4]]).T
   ]),
   np.array([
      np.array([[2,-2]]).T,
      np.array([[4,-4]]).T
   ])
]

mis = np.zeros((0,DIM))
m = np.zeros((0, DIM))
numOfSamples = 0
for i, cls in enumerate(classes):
   
   for sam in cls:
       arr = []
       numOfSamples += 1
       for x in range(DIM):
           arr.append(sam[x][0])
       m = np.append(m, [arr], axis = 0 )
    
   mi = np.array([])
   sum = np.sum(cls, axis = 0)
   for x in range(DIM):
       mi = np.append(mi, sum[x][0])
   mi = mi / len(cls)
   mis = np.append(mis, [mi], axis = 0)
for i, mi in enumerate(mis):
   print("Mi({num}) = {mi}".format(num = i, mi = mi))
print("M = {m}".format( m = np.sum(m , axis = 0)/ numOfSamples))

S = np.zeros((0,DIM, DIM))
for i, cls in enumerate(classes):
    _S = np.zeros((DIM, DIM))
    for sam in cls:
        arr = np.array([])
        for x in range(DIM):
           arr = np.append(arr, sam[x][0])
        _S = _S + np.matmul(np.array([arr - mis[i]]).T, np.array([arr - mis[i]]))
    print("S{0} = {1}".format(i, _S))
    S = np.append(S, [_S], axis = 0)
print("Sw = S1 + S2 + ... = {0}".format(np.sum(S, axis = 0)))
_m = np.sum(m, axis = 0) / numOfSamples
Sb = np.zeros((DIM, DIM))
for i, cls in enumerate(classes):
    ni = len(cls) #/ float(numOfSamples)
    Sb = Sb +  ni * np.matmul(np.array([mis[i] - _m]).T , np.array([mis[i] - _m]))
print("Sb = {0}".format(Sb))

print("Sb w = lambda Sw w\n(Sb - lambda*Sw)*w = 0")
print("det(Sb - lambda*Sw) = 0")

