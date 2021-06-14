string = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'X', 'O']]
import numpy as np

arr = np.array(string)
print(arr.transpose())