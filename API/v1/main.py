# API CODE

import pandas as pd
from fastapi import FastAPI
from ML_Code import *

app = FastAPI()


csv_path = "../../Data_Repository/movies_finalversion.csv"

# Loading the dataset
df_movies = pd.read_csv(csv_path, low_memory=False, encoding='latin-1', sep=',',  parse_dates=['release_date'])

# End point functions

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/api/v1/shoots_per_month/{month}")
def shoots_per_month(month: int):
    df1= df_movies[df_movies["release_date"].dt.month == month]
    count = df1.shape[0]
    return count

@app.get("/api/v1/shoots_per_day/{day}")
def shoots_per_day(day: int):
    df1 = df_movies[df_movies["release_date"].dt.day == day]
    count = df1.shape[0]
    return count

@app.get("/api/v1/title_score/{title}")
def title_score(title: str):
    df1 = df_movies[df_movies['title'] == title]
    response = df1[['title', 'release_year', 'vote_average']].to_dict(orient='records')

    return response

@app.get("/api/v1/title_votes/{title}")
def title_votes(title: str):
    df1 = df_movies[(df_movies['title'] == title) & (df_movies['vote_count'] >= 2000)]
    response = df1[['title', 'vote_count', 'vote_average']].to_dict(orient='records')
    return response

@app.get("/api/v1/actor/{actor}")
def get_actor(actor: str):
    df1 = df_movies[df_movies['actors'].apply(lambda actors_list: actor in actors_list)]
    movies_count = df1.shape[0]
    revenue = df1['revenue'].sum()
    avg_revenue = revenue / movies_count
    response = [actor, movies_count, int(revenue), int(avg_revenue)]
    return response

@app.get("/api/v1/director/{director}")
def get_director(director: str):
    df1 = df_movies[df_movies['director'].apply(lambda director_list: director in director_list)]
    revenue = df1['revenue'].sum()
    response = df1[['title', 'release_date', 'ROI', 'budget', 'revenue']].to_dict(orient='records')
    return [director, revenue, response]


# Obtener las recomendaciones para una película específica
@app.get("/api/v1/get_recommended_movies/{movie_title}")
def get_recommended_movies(movie_title: str):
    recommendations = get_recommendations(movie_title, knn, data)
    return(recommendations)



