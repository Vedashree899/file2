import numpy as np
a_ran=np.arange(4) #4-no of elements
print(a_ran)
a_ran=np.arange(6)
print(a_ran)
a_diag=np.eye(3) #all the major diagonal will be filled with 1
print(a_diag)
a_diag2=np.eye(2,3) #all the major diagonal will be filled with 1
print(a_diag2)
a_lin=np.linspace(1,10,5) #start,end,no of elements
print(a_lin)
a_lin=np.linspace(1,10,7) #start,end,no of elements
print(a_lin)
random1=np.random.rand(5) #no of elements (all the elements in the array will be in the range 0-1)
print(random1)random2=np.random.rand(2,3) #rows,cols
print(random2)
random4=np.random.randint(15,25,7) #starting range,ending range,no of elements
print(random4)
