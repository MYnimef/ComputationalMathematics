from scipy.linalg import solve
import numpy as np

if __name__ == '__main__':
    A = np.array([[9, 8, 3],
                  [3, 6, 3],
                  [5, 3, 1]])
    b = np.array([4, -3, 2])
    x = solve(A, b)
    print(x)
