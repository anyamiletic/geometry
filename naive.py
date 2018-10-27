import numpy as np
import constraint

def algorithm(M1,M2,M3,M4,M1p,M2p,M3p,M4p):
    # get the points and their images
    A, B, C, D = M1,M2,M3,M4
    Ap, Bp, Cp, Dp = M1p,M2p,M3p,M4p

    # matrix [A B C]
    point_matrix = np.transpose(np.array([A, B, C]))
    # ABC^(-1)
    point_matrix_inverse = np.linalg.inv(point_matrix)
    # P1 = ABC^(-1) * D * ABC
    P1 = point_matrix_inverse.dot(D) * point_matrix

    # repeat the same steps for images
    image_matrix = np.transpose(np.array([Ap, Bp, Cp]))
    image_matrix_inverse = np.linalg.inv(image_matrix)
    P2 = image_matrix_inverse.dot(Dp) * image_matrix

    # P2 * P1^(-1)
    return P2.dot(np.linalg.inv(P1))


