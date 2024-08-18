import pandas as pd
import numpy as np

def perform_svd(normalized_ratings_matrix, rank=1000):
    normalized_ratings_matrix = normalized_ratings_matrix

    U, S, VT = np.linalg.svd(normalized_ratings_matrix)
    sigma = np.diag(S)
    SVD = U[:,:rank]@sigma[:rank,:rank]@VT[:rank,:]
    return SVD