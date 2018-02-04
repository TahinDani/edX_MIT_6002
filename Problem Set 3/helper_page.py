from ps3b import SimpleVirus
import random
#random.seed(1)

myVirus = SimpleVirus(0.5, 0.5)
for i in range(10):
    try:
        print(myVirus.reproduce(random.random()))
    except:
        print("Exception")
