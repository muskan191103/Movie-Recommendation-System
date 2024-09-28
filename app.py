import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f1b432fdc71318655619af2ef955e2b4'.format(movie_id))
    data=response.json()
    # print (data)
    if 'poster_path' in data and data['poster_path']:
        return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "Error: Poster not available or invalid movie ID"



movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = list(movies_list).index(movie)
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list1:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies_list[i[0]])
        #fetch posters
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Movie Title",
    movies_list,
    index=None,
    placeholder="Choose an option"
)

if st.button("Recommend", type="primary"):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col1:
        st.text(names[5])
        st.image(posters[5])

    with col2:
        st.text(names[6])
        st.image(posters[6])

    with col3:
        st.text(names[7])
        st.image(posters[7])

    with col4:
        st.text(names[8])
        st.image(posters[8])

    with col5:
        st.text(names[9])
        st.image(posters[9])

    with col1:
        st.text(names[10])
        st.image(posters[10])

    with col2:
        st.text(names[11])
        st.image(posters[11])

    with col3:
        st.text(names[12])
        st.image(posters[12])

    with col4:
        st.text(names[13])
        st.image(posters[13])

    with col5:
        st.text(names[14])
        st.image(posters[14])