from svd_scripts.utils import * 

if __name__ == "__main__":
            
    print('Starting inference...\n')
    while True:
        choice = input('''
Select one of the following:
1) Get similar movies to a selected movie
2) Get similar users to a selected user with recommendations
3) Exit
Selected option: ''')
    
        if choice == '3':
            print("Exiting...")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        inp_rank = input('Enter SVD rank: ')
        if os.path.isfile(f'./data/processed_data/SVD-{inp_rank}.csv'):
            SVD = pd.read_csv(f'./data/processed_data/SVD-{inp_rank}.csv').to_numpy()
            data = pd.read_csv(f'./data/processed_data/data.csv')
            
        else:
            print('SVD with the following rank not yet created. Please use training.py')
        
        if choice == '1':
            movie_id = int(input('Enter Movie ID: '))
            try:
                movie_titles = top_movie_similarity(SVD, movie_id, 20)
                print_similar_movies(movie_titles, data)
            except ValueError as ve:
                print(f"ValueError: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")
                
        elif choice == '2':
            user_id = int(input("Enter User ID: ")) 
            try:
                reccs, matched_user = top_user_similarity(SVD, user_id, data)
                print_recommendations(reccs=reccs, matched_user= matched_user, data=data, length=5)
            except ValueError as ve:
                print(f"ValueError: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")