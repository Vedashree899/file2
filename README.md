numpy
[[10  2]
 [30 40]] <class 'numpy.matrix'>
nm2=np.matrix([[10,20],[300,400]])
print(nm2,type(nm2))
[[ 10  20]
 [300 400]] <class 'numpy.matrix'>
print(nm1*nm2) #matrix multiplication result
[[  700  1000]
 [12300 16600]]
print(np.transpose(nm1))
[[10 30]
 [ 2 40]]
print(np.linalg.inv(nm1)) #inverse of a matrix
[[ 0.11764706 -0.00588235]
 [-0.08823529  0.02941176]]
print(np.linalg.det(nm1)) #determinant of a matrix
340.0000000000001
