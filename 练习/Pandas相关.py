import pandas as pd
import numpy as np

res = pd.Series([214, 38, 618, 1111, 1212], index=['a', 'b', 'c', 'd', 'e'])
print(res)

a = np.array([2, 3, 4])
print(a)

b = np.array([1.2, 3.5, 5.1])
print(b)

a2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a2)

b2 = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b2)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
