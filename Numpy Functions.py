import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 445
print(arr)
print(x)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 5)
print(newarr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 2)
print(x)

import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))



