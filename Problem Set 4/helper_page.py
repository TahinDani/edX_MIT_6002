from ps4 import generate_models


x = [1961, 1962, 1963]
y = [4.4, 5.5, 6.6]
degs = [1, 2]
print(len(x), len(y))
print(generate_models(x, y, degs))
