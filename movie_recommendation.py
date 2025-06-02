import random
import streamlit as st
import pyttsx3

MOVIES = [
    {"title": "The Shawshank Redemption", "genre": "drama", "mood": "thought-provoking", "decade": "1990s"},
    {"title": "Groundhog Day", "genre": "comedy", "mood": "feel-good", "decade": "1990s"},
    {"title": "Titanic", "genre": "romance", "mood": "romantic", "decade": "1990s"},
    {"title": "The Matrix", "genre": "sci-fi", "mood": "intense", "decade": "1990s"},
    {"title": "Amélie", "genre": "romance", "mood": "feel-good", "decade": "2000s"},
    {"title": "The Notebook", "genre": "romance", "mood": "romantic", "decade": "2000s"},
    {"title": "The Dark Knight", "genre": "thriller", "mood": "intense", "decade": "2000s"},
    {"title": "WALL-E", "genre": "sci-fi", "mood": "thought-provoking", "decade": "2000s"},
    {"title": "Juno", "genre": "comedy", "mood": "feel-good", "decade": "2000s"},
    {"title": "Inception", "genre": "sci-fi", "mood": "intense", "decade": "2010s"},
    {"title": "Interstellar", "genre": "sci-fi", "mood": "thought-provoking", "decade": "2010s"},
    {"title": "The Grand Budapest Hotel", "genre": "comedy", "mood": "feel-good", "decade": "2010s"},
    {"title": "La La Land", "genre": "musical", "mood": "romantic", "decade": "2010s"},
    {"title": "Parasite", "genre": "thriller", "mood": "intense", "decade": "2010s"},
    {"title": "Get Out", "genre": "horror", "mood": "intense", "decade": "2010s"},
    {"title": "The Theory of Everything", "genre": "drama", "mood": "thought-provoking", "decade": "2010s"},
    {"title": "Crazy Rich Asians", "genre": "romance", "mood": "feel-good", "decade": "2010s"},
]

engine = pyttsx3.init()

st.title("🎬 Movie Recommendation Chatbot")

genre = st.selectbox("Choose a genre", ["", "sci-fi", "romance", "comedy", "drama", "musical", "thriller", "horror"])
mood = st.selectbox("Choose a mood", ["", "feel-good", "intense", "thought-provoking", "romantic"])
decade = st.selectbox("Choose a decade", ["", "1990s", "2000s", "2010s"])

if st.button("Get Recommendation"):
    if not genre and not mood and not decade:
        movie = random.choice(MOVIES)
        result = f"Try watching: {movie['title']}"
    else:
        recommendations = [
            movie for movie in MOVIES
            if genre == movie['genre'] and mood == movie['mood'] and decade == movie['decade']
        ]

        if not recommendations:
            recommendations = [
                movie for movie in MOVIES
                if (genre == movie['genre'] and mood == movie['mood']) or
                   (genre == movie['genre'] and decade == movie['decade']) or
                   (mood == movie['mood'] and decade == movie['decade'])
            ]

        if not recommendations:
            recommendations = [
                movie for movie in MOVIES
                if genre == movie['genre'] or mood == movie['mood'] or decade == movie['decade']
            ]

        if not recommendations:
            movie = random.choice(MOVIES)
            result = f"No match found. How about: {movie['title']}?"
        else:
            movie = random.choice(recommendations)
            result = f"I recommend you watch: {movie['title']}"

    st.success(result)
    try:
        engine.say(result)
        engine.runAndWait()
    except:
        st.info("Text-to-speech might not be supported in this environment.")
