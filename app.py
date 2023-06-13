#-----------------------------------------------------------------------\
# MOVIA                                                                 #
# Movie Statistics & Recommender System                                 #
#                                                                       #
#-----------------------------------------------------------------------/
import streamlit as st
import requests

API_URL = "https://danw-debug-movia-apiv1main-bclc2u.streamlit.app"  # Reemplaza con la URL de tu servidor FastAPI



def get_shoots_per_month(month: int ):
    response = requests.get(f"{API_URL}/api/v1/shoots_per_month/{month}")
    if response.status_code == 200:
        count = response.json()
        return count
    else:
        st.error("Error al obtener los disparos por mes")

def get_shoots_per_day(day: int):
    response = requests.get(f"{API_URL}/api/v1/shoots_per_day/{day}")
    if response.status_code == 200:
        count = response.json()
        return count
    else:
        st.error("Error al obtener los disparos por día")

def get_title_score(title: str):
    response = requests.get(f"{API_URL}/api/v1/title_score/{title}")
    if response.status_code == 200:
        title_data = response.json()
        return title_data
    else:
        st.error("Error al obtener la puntuación del título")

def get_title_votes(title: str):
    response = requests.get(f"{API_URL}/api/v1/title_votes/{title}")
    if response.status_code == 200:
        title_votes = response.json()
        return title_votes
    else:
        st.error("Error al obtener los votos del título")

def get_actor(actor: str):
    response = requests.get(f"{API_URL}/api/v1/actor/{actor}")
    if response.status_code == 200:
        actor_data = response.json()
        return actor_data
    else:
        st.error("Error al obtener los datos del actor")

def get_director(director: str):
    response = requests.get(f"{API_URL}/api/v1/director/{director}")
    if response.status_code == 200:
        director_data = response.json()
        return director_data
    else:
        st.error("Error al obtener los datos del director")

def get_recommended_movies(movie_title: str):
    response = requests.get(f"{API_URL}/api/v1/get_recommended_movies/{movie_title}")
    st.write(f"{API_URL}/api/v1/get_recommended_movies/{movie_title}")
    st.write("msg received")
    if response.status_code == 200:
        st.write("STATUS 200")
        #st.write("Response: ", response.text)
        #st.write("Response: ", response.headers)
        backendmsg = response.json()
        #return recommended_movies
        #return "HOLA"
        if backendmsg.get("status") == "success":
            recommended_movies = backendmsg.get("data", {}).get("recommended_movies")
            return(recommended_movies)
        else:
            st.error("No se pudo obtener las recomendaciones de películas.")
    else:
            st.error("Ocurrió un error al obtener las recomendaciones de películas.")




   # else:
    #    st.error("Error al obtener las películas recomendadas")


def main():
    # Título de la página
    st.title("Mi Aplicación con Streamlit y FastAPI")
    
    movie = st.text_input("Ingrese el título de una película:")
    if st.button("Obtener recomendaciones:"):
        recommendations = get_recommended_movies(movie)
        st.success(f"Recommended movies: {recommendations}")
    
    month = st.number_input("Ingrese un mes:",min_value=1, max_value=12, step=1, format="%d")
    month = int(month)
    if st.button("Obtener disparos por mes"):
        count = get_shoots_per_month(month)
        st.success(f"Disparos por mes: {count}")

    day = st.number_input("Ingrese un día:",min_value=1, max_value=31, step=1, format="%d")
    day = int(day)
    if st.button("Obtener disparos por día"):
        count = get_shoots_per_day(day)
        st.success(f"Disparos por día: {count}")
    
    title = st.text_input("Ingrese un título:")
    if st.button("Obtener puntuación del título"):
        title_data = get_title_score(title)
        st.success(f"Puntuación del título: {title_data}")
    
    actor = st.text_input("Ingrese un actor:")
    if st.button("Obtener datos del actor"):
        actor_data = get_actor(actor)
        st.success(f"Datos del actor: {actor_data}")
    
    director = st.text_input("Ingrese un director:")
    if st.button("Obtener datos del director"):
        director_data = get_director(director)
        st.success(f"Datos del director: {director_data}")
    

if __name__ == "__main__":
    main()
