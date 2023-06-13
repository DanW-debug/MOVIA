# MOVIA
# Movies Recommender System

# importing libraries
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import re
import os
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Data_Repository', 'movies_finalversion.csv')

# Loading the dataset
data = pd.read_csv(csv_path, low_memory=False, encoding='latin-1', sep=',')

#Choosing different sets of features
data_full = data [['title', 'belongs_to_collection', 'original_language', 'genres', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'actors', 'director']]
#data = data[['genres', 'overview', 'popularity', 'release_date', 'actors', 'director']]
data_title_genres_overview =data [['title', 'genres', 'overview']] 
data_title_overview = data [['title', 'overview']]
data_title_genres_overview_actors_director = data [['title', 'genres', 'overview', 'actors', 'director']]

# Combining features in only one column
#data['features'] = data_title_genres_overview_actors_director.apply(lambda x: ' '.join(x.values.astype(str)), axis=1)
data['features'] = data_full.apply(lambda x: ' '.join(x.values.astype(str)), axis=1)

corpus = data['features'].tolist()

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

def stemming_tokenizer2(str_input):
    words = re.sub(r"[^A-Za-z0-9\-]", " ", str_input).lower().split()
    words = [porter_stemmer.stem(word) for word in words]
    return words

count_vectorizer = CountVectorizer(stop_words='english', min_df=0.0005, max_features=2000)
X = count_vectorizer.fit_transform(corpus)

movie_0 = pd.DataFrame(X.toarray(), columns=count_vectorizer.get_feature_names_out())

# Crear el modelo de vecinos más cercanos
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(X)

def get_recommendations(title, knn_model, data, num_recommendations=5):
    # Obtener el índice de la película que coincide con el título
    idx = data[data['title'] == title].index[0]

    # Encontrar los vecinos más cercanos
    distances, indices = knn_model.kneighbors(X[idx], n_neighbors=num_recommendations+1)

    # Obtener los índices de las películas más similares (excluyendo la película de consulta)
    movie_indices = indices.flatten()[1:]

    # Devolver las películas recomendadas
    return data['title'].iloc[movie_indices]

# Obtener las recomendaciones para una película específica
movie_title = "Star Wars"
recommendations = get_recommendations(movie_title, knn, data)

# Imprimir las recomendaciones
st.write("Recomendaciones para", movie_title)
st.write(recommendations)


