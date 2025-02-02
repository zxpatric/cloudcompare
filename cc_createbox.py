import numpy as np

# Vertices of the cube
VERTICES = np.array([
    [-0.5, -0.5, -0.5],
    [-0.5, -0.5, 0.5],
    [-0.5, 0.5, -0.5],
    [-0.5, 0.5, 0.5],
    [0.5, -0.5, -0.5],
    [0.5, -0.5, 0.5],
    [0.5, 0.5, -0.5],
    [0.5, 0.5, 0.5]
])

MATRIX = np.matrix(
    '1 2; \
     3 4'
)



if __name__ ==  "__main__":

    #print (VERTICES[:,0])
    print(MATRIX)
    _inverse_mat = np.linalg.inv(MATRIX)
    print(_inverse_mat)
    print(MATRIX*_inverse_mat)
    print(_inverse_mat*MATRIX)
    print(MATRIX+_inverse_mat)