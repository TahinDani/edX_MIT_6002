from ps3b import *
import random
random.seed(0)

# myVirus = SimpleVirus(0.5, 0.5)
# for i in range(10):
#     try:
#         print(myVirus.reproduce(random.random()))
#     except:
#         print("Exception")

#print(simulationWithoutDrug(1, 10, 1.0, 0.0, 1))


# def switch(bool):
#     if bool is True:
#         return False
#     return True

# dict = {'a': True, 'b': True, 'c': True}
# for k in dict.keys():
#     dict[k] = switch(dict[k])

# print(dict)


simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)