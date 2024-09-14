import pandas as pd
import streamlit as st

from recommender import get_movie_recommendations

# Load Data
movies_df = pd.read_csv('data/movies.csv')

# App Title
st.title('Enhanced Movie Recommendation System')

# User Inputs
genres = st.multiselect('Select Your Favorite Genres:', movies_df['genres'].str.split('|').explode().unique())
keywords = st.text_input('Enter Keywords (e.g., "thrilling, space, mystery"):', '')

# Optional: Select a specific movie you liked
movie_title = st.selectbox('Optional: Select a Movie You Liked', ['None'] + list(movies_df['title'].unique()))

# Recommend Button
if st.button('Recommend'):
    if genres or keywords or movie_title != 'None':
        selected_movie = None if movie_title == 'None' else movie_title
        recommendations = get_movie_recommendations(' '.join(genres), keywords, selected_movie)

        if not recommendations.empty:
            st.write('Top Recommendations:')
            for idx, row in recommendations.iterrows():
                st.write(f"{row['title']} - Average Rating: {row['average_rating']:.2f}")
        else:
            st.write('No recommendations found. Please try with different inputs.')
    else:
        st.write('Please select at least one genre, keyword, or movie to get recommendations.')
