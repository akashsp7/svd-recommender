import pandas as pd
import os

from svd_scripts import data_handling as dh
from svd_scripts import matrix
from svd_scripts import svd
from svd_scripts import utils

path = './data'
save_path = './data/processed_data'
utils.ensure_directory_exists(save_path)

def pipline(path, inp_rank):
    data = dh.load_movielens_data(datapath=path)
    ratings_matrix = matrix.create_ratings_matrix(data)
    norm_matrix = matrix.normalize_ratings_matrix(ratings_matrix)
    check_svd_path = os.path.join(save_path, f'SVD-{inp_rank}.csv')
    
    if os.path.isfile(check_svd_path):
        print(f'SVD already performed and saved at {check_svd_path}\n')
        print('To perform SVD again, delete or rename the above mentioned file')
    else:
        print('Performing SVD...\n')
        SVD = svd.perform_svd(norm_matrix, rank=inp_rank)
        svd_path = os.path.join(save_path, f'SVD-{inp_rank}.csv')
        pd.DataFrame(SVD).to_csv(f'{svd_path}', index=False)
        print(f'SVD saved at {svd_path}') 
        

if __name__ == "__main__":
    path = './data'
    input_rank = 1000
    while True:
        try:
            input_rank = int(input('Please enter input rank:\n'))
            adjusted_inp = max(1000, min(3952, input_rank))
            print(f"Input rank adjusted to: {adjusted_inp}" if adjusted_inp != input_rank else f"Input rank is within the accepted range: {input_rank}")
            break  
        except ValueError:
            print('Please enter a valid integer.')
    pipline(path, input_rank)


            
        