import numpy as np

#numbers = np.array([[1,2,3], [4, 5, 6]])
#print(numbers)

#array = np.zeros((3, 3), dtype=int)
#print(array)
#print(array.shape)
#
#array = np.ones((3, 3), dtype=int)
#print(array)
#
#array = np.full((3, 3), 5, dtype=int)
#print(array)

#array = np.random.random((4, 4))
#print(array)
#print(array[0, 0])
#print(array > 0.5)
#print(array[array > 0.5])
#print(np.floor(array))
#print(np.ceil(array))
#print(np.round(array))

# operations with numpy
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(f"dimensions_cm with numpy......: {dimensions_cm}")

# operations with pure python
dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]
print(f"dimensions_cm with pure python: {dimensions_cm}")
