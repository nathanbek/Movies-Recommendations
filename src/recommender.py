import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load Data
movies = pd.read_csv('../data/movies.csv')
ratings = pd.read_csv('../data/ratings.csv')
tags = pd.read_csv('../data/tags.csv')
links = pd.read_csv('../data/links.csv')

# Enhanced content-based filtering
def enhanced_content_recommender(genres, keywords, movies_df, tags_df, ratings_df, movie_title=None):
    # Merge tags into the movies DataFrame
    movies_df['tags'] = movies_df['movieId'].map(tags_df.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)))

    # Merge average ratings into movies DataFrame
    movies_df['average_rating'] = movies_df['movieId'].map(ratings_df.groupby('movieId')['rating'].mean())

    # Combine genres, keywords, and tags into a single feature column
    movies_df['combined_features'] = movies_df['genres'].fillna('') + ' ' + movies_df['tags'].fillna('')
    if keywords:
        movies_df['combined_features'] += ' ' + keywords

    # Optional: Include specific movie details for similarity
    if movie_title:
        movie_features = movies_df.loc[movies_df['title'] == movie_title, 'combined_features'].values
        if movie_features:
            movies_df['combined_features'] += ' ' + movie_features[0]

    # Remove rows where combined_features is empty
    movies_df = movies_df[movies_df['combined_features'].str.strip() != '']

    # Vectorize combined features using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
    except ValueError:
        return pd.Series([], dtype='str')

    # Compute cosine similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Find similarity scores for user input (last row)
    sim_scores = list(enumerate(cosine_sim[-1]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 10 movie indices, excluding the user input itself
    movie_indices = [i[0] for i in sim_scores[1:11]]

    # Return the titles and average ratings of the recommended movies
    return movies_df[['title', 'average_rating']].iloc[movie_indices]

# Main function to get recommendations
def get_movie_recommendations(genres, keywords, movie_title=None):
    # Create DataFrame for user input (genres and keywords)
    user_input_df = pd.DataFrame({'movieId': [0], 'genres': [genres], 'tags': [keywords], 'average_rating': [0]})

    # Add user input to the movies DataFrame
    movies_with_input = pd.concat([movies, user_input_df], ignore_index=True)

    # Get recommendations
    recommendations = enhanced_content_recommender(genres, keywords, movies_with_input, tags, ratings, movie_title)
    return recommendations
