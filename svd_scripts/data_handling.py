import pandas as pd

def load_movielens_data(datapath):
    column_list_ratings = ["UserID", "MovieID", "Ratings","Timestamp"]
    ratings  = pd.read_csv(f'{datapath}/ratings.dat',sep='::',names = column_list_ratings, engine='python', encoding = 'latin-1')
    
    column_list_movies = ["MovieID","Title","Genres"]
    movies = pd.read_csv(f'{datapath}/movies.dat',sep = '::',names = column_list_movies, engine='python', encoding = 'latin-1')
    
    column_list_users = ["UserID","Gender","Age","Occupation","Zixp-code"]
    users = pd.read_csv(f"{datapath}/users.dat",sep = "::",names = column_list_users, engine='python', encoding = 'latin-1')
    
    data = pd.merge(pd.merge(ratings,users),movies)
    pd.DataFrame(data).to_csv(f'{datapath}/processed_data/data.csv', index=False)
    return data

