import numpy as np
import pandas as pd
import os

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def cosine_similarity(x, y):
    denominator = np.dot(np.linalg.norm(x), np.linalg.norm(y))
    if denominator == 0:
        return 0
    else:
        return np.dot(x, y)/np.dot(np.linalg.norm(x), np.linalg.norm(y))
    
def top_movie_similarity(inp_data, movie_id, top_n):
    # Movie id starts from 1
    #Use the calculation formula above
    similarities = {}
    for i in range(len(inp_data.T)):
        similarities[i+1] = cosine_similarity(inp_data[:,i],inp_data[:, movie_id -1])
    
    sorted_list = sorted(similarities.items(), key = lambda x:x[1], reverse = True)
    return sorted_list[:top_n+1] #since top match is the movie itself, we add 1

def print_similar_movies(movie_titles, data):
    movie_titles = [id[0] for id in movie_titles]
    print(f'Movies similar to {data[data["MovieID"]==movie_titles[0]]["Title"].unique()[0]} are:\n')
    for i in movie_titles[1:]:
        print(data[data['MovieID']==i]['Title'].unique()[0])
        
def top_user_similarity(input_mat, id, data):
    similarities = {}
    for i in range(len(input_mat)):
        similarities[i+1] = cosine_similarity(input_mat[i],input_mat[id -1])
    
    sorted_list = sorted(similarities.items(), key = lambda x:x[1], reverse = True)
    sorted_list = [item[0] for item in sorted_list]
    matched_user = sorted_list[1] #since top match is the user itself
    # matched_user_likes = data[data['UserID']== matched_user].sort_values('Ratings',ascending=False)['Title'].tolist()
    matched_user_likes = data[data['UserID']== matched_user][data[data['UserID']== matched_user]['Ratings']>4]['Title'].tolist()
    if len(matched_user_likes) < 5:
        matched_user_likes = data[data['UserID']== matched_user][data[data['UserID']== matched_user]['Ratings']>3]['Title'].tolist()
    if len(matched_user_likes) < 5:
        return [], []
    recommendations = []
    for likes in matched_user_likes:
        if likes not in data[data['UserID']== id]['Title'].tolist():
            recommendations.append(likes)
    if len(recommendations) < 5:
        return [],[]
    return recommendations, matched_user

def print_recommendations(reccs, matched_user, data, length=5):
    if len(reccs) >=5:      
        print(f'Recommendations from matched user {matched_user}:\n')
        recommendations = np.random.choice(reccs, size=length, replace=False).tolist()
        for movies in recommendations:
            print(f'{movies} | Genre: {data[data["Title"]==movies]["Genres"].unique()[0]}')
    else:
        print("No similar users were found")