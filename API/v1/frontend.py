#-----------------------------------------------------------------------\
# MOVIA                                                                 #
# Movie Statistics & Recommender System - Frontend Side                 #
#                                                                       #
#-----------------------------------------------------------------------/
import streamlit as st
import requests
import subprocess

API_URL = "http://localhost"  

# Starting FastAPI server using uvicorn
def start_fastapi_server():
    command = "uvicorn backend:app --host 0.0.0.0 --port 8080"
    subprocess.Popen(command, shell=True)


def get_shoots_per_month(month: int ):
    response = requests.get(f"{API_URL}/api/v1/shoots_per_month/{month}")
    if response.status_code == 200:
        count = response.json()
        return count
    else:
        st.error("Error getting shoots per month")

def get_shoots_per_day(day: int):
    response = requests.get(f"{API_URL}/api/v1/shoots_per_day/{day}")
    if response.status_code == 200:
        count = response.json()
        return count
    else:
        st.error("Error getting shoots per day")

def get_title_score(title: str):
    response = requests.get(f"{API_URL}/api/v1/title_score/{title}")
    if response.status_code == 200:
        title_data = response.json()
        return title_data
    else:
        st.error("Error getting title score")

def get_title_votes(title: str):
    response = requests.get(f"{API_URL}/api/v1/title_votes/{title}")
    if response.status_code == 200:
        title_votes = response.json()
        return title_votes
    else:
        st.error("Error getting title votes")

def get_actor(actor: str):
    response = requests.get(f"{API_URL}/api/v1/actor/{actor}")
    if response.status_code == 200:
        actor_data = response.json()
        return actor_data
    else:
        st.error("Error getting actor data")

def get_director(director: str):
    response = requests.get(f"{API_URL}/api/v1/director/{director}")
    if response.status_code == 200:
        director_data = response.json()
        return director_data
    else:
        st.error("Error getting director data")

def get_recommended_movies(movie_title: str):
    response = requests.get(f"{API_URL}/api/v1/get_recommended_movies/{movie_title}")
    if response.status_code == 200:
        backendmsg = response.text
        if backendmsg.get("status") == "success":
            recommended_movies = backendmsg.get("data", {}).get("recommended_movies")
            return(recommended_movies)
        else:
            st.error("Can't get movie recommendations.")
    else:
            st.error("Error during movie requests")

def main():
    # Page Title
    st.title("MOVIA Movie statistics and Recommender System built with Streamlit and FastAPI")
    
 # Start FastAPI server in background
    #start_fastapi_server()

    st.write("Loading backend process...")

    movie = st.text_input("Input movie title:")
    if st.button("Getting recommendations:"):
        recommendations = get_recommended_movies(movie)
        st.success(f"Recommended movies: {recommendations}")
    
    month = st.number_input("Input a month number:",min_value=1, max_value=12, step=1, format="%d")
    month = int(month)
    if st.button("Getting shoots per month"):
        count = get_shoots_per_month(month)
        st.success(f"Shoots per month: {count}")

    day = st.number_input("Input a day number:",min_value=1, max_value=31, step=1, format="%d")
    day = int(day)
    if st.button("Getting shoots per day"):
        count = get_shoots_per_day(day)
        st.success(f"Shoots per day: {count}")
    
    title = st.text_input("Input a title:")
    if st.button("Getting title score"):
        title_data = get_title_score(title)
        st.success(f"Title score: {title_data}")
    
    actor = st.text_input("Input an actor name:")
    if st.button("Geting actor data"):
        actor_data = get_actor(actor)
        st.success(f"Actor data: {actor_data}")
    
    director = st.text_input("Input a director name:")
    if st.button("Getting director data"):
        director_data = get_director(director)
        st.success(f"Director data: {director_data}")
    

