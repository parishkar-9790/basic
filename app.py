import pandas as pd
import sys
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv(f'{os.getcwd()}/Projects/basic/dataset.csv')
required_columns =['title','original_title', 'tagline', 'keywords', 'overview', 'genres', 'cast', 'director']
movies = movies[required_columns]
movies.isna().sum()
movies.fillna(' ', inplace=True)
movies.isna().sum()
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['director'] = movies['director'].apply(lambda x: x.replace(" ","") )
movies['genres'] = movies['genres'].apply(lambda x: ','.join(map(str, x)))
movies['keywords'] = movies['keywords'].apply(lambda x: ','.join(map(str, x)))
movies['cast'] = movies['cast'].apply(lambda x: ','.join(map(str, x)))
movies['content'] = movies['title'] + ' ' + movies['overview'] + ' ' + movies['keywords'] + ' ' + movies['cast'] + ' ' + movies ['director']
vectorizer = TfidfVectorizer(max_features=1000)
movie_vectors = vectorizer.fit_transform(movies['content'].values) 
similarity = cosine_similarity(movie_vectors)
similarity_df = pd.DataFrame(similarity)
# recommend(sys.argv[1])
# print('hey there')
# recommend('Now You See Me')
movie='Now You See Me'
movies_index = movies[movies['title'] == movie].index[0]
distances = similarity[movies_index]    
movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
for i in movies_list:
    print(movies.iloc[i[0]].title)
sys.stdout.flush()