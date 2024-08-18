import numpy as np

def create_ratings_matrix(data):
    ratings_matrix = np.zeros((data['UserID'].max(),data['MovieID'].max()))
    for i in data.itertuples():
        ratings_matrix[i[1]-1,i[2]-1] = i[3]
    return ratings_matrix

def normalize_ratings_matrix(ratings_matrix):
    ratings_matrix[ratings_matrix==0] = np.nan
    all_nan_columns = np.all(np.isnan(ratings_matrix), axis=0)
    ratings_matrix[:, all_nan_columns] = 0
    matrix_mean = np.nanmean(ratings_matrix, axis=0)
    matrix_std = np.nanstd(ratings_matrix, axis=0)
    matrix_std[matrix_std==0] = 1
    ratings_matrix_filled = ratings_matrix.copy()
    for col in range(ratings_matrix.shape[1]):
        ratings_matrix_filled[np.isnan(ratings_matrix[:, col]), col] = matrix_mean[col] 
    ratings_matrix_normalized = (ratings_matrix_filled - matrix_mean)/matrix_std
    return ratings_matrix_normalized