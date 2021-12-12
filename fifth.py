import numpy as np

if __name__ == '__main__':
    '''
    A = np.array([[9, 8, 3],
                  [3, 6, 3],
                  [5, 3, 1]])
    b = np.array([4, -3, 2])
    '''

    A = np.array([[4, 2],
                  [0, 3]])
    b = np.array([0, 1])
    print('A =\n{}\n'.format(A))
    print('b =\n{}\n'.format(b))

    x = np.linalg.solve(A, b)
    print('x =\n{}\n'.format(x))

    eigenValues, ownVectors = np.linalg.eig(A)
    ownVectors = ownVectors.transpose()

    print(eigenValues, "\n")
    print(ownVectors, "\n")

    A = np.matrix(A)
    for i in range(len(ownVectors)):
        vec = ownVectors[i].reshape(-1, 1)
        print((A * vec) / eigenValues[i])
