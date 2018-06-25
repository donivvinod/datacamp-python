#!/usr/bin/python

import numpy as np
print(np.random.rand())

#random with seed
#np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

#reset the seed and print again. Same two random numbers are printed
#np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

#reset the seed and print again. Same two random numbers are printed
#np.random.seed(123)
print(dice)

steps = 0
counter = 0
while counter <100 :
    dice = np.random.randint(1,7)
    if dice == 1 or dice == 2 :
        steps = steps - 1
        if steps < 0 :
            steps = 0 
    elif dice == 3 or dice == 4 or dice == 5  :
        steps = steps + 1
    else :
        dice = np.random.randint(1,6)
        steps = steps + dice
    counter = counter + 1    

print(steps)    
