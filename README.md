# Movie Recommendation System

This project is a movie recommendation system built using Python, Pandas, Scikit-Learn, and Streamlit. Users can input their preferred genres, keywords, or a specific movie they like, and the system provides personalized movie recommendations.

## Features
- **Content-Based Filtering**: Uses genres, tags, and keywords to recommend similar movies.
- **Integration with User Ratings**: Considers user ratings to enhance the relevance of recommendations.
- **Streamlit UI**: Provides a user-friendly web interface for input and displaying recommendations.

## Demo
Check out the live demo of the app here: [Movie Recommendation System](https://movies-recommendations-netflix.streamlit.app/)

## Installation
To run this project locally, follow these steps:

### Prerequisites
- Python 3.8+
- Git

### Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Directory Structure**:
    Ensure the directory structure is as follows:
    ```
    Movie-Recommendation-System/
    ├── data/
    │   ├── movies.csv
    │   ├── ratings.csv
    │   ├── tags.csv
    │   ├── links.csv
    ├── src/
    │   ├── app.py
    │   ├── recommender.py
    ├── requirements.txt
    └── README.md
    ```

5. **Run the application locally**:
    Navigate to the `src` directory and run the Streamlit app:
    ```bash
    cd src
    streamlit run app.py
    ```
    The app will be accessible at `http://localhost:8501` by default.

## Usage
1. **Select Your Favorite Genres**: Choose from a list of available genres.
2. **Enter Keywords**: Describe the type of movies you are interested in.
3. **Optional Movie Selection**: Choose a specific movie that you like for more tailored recommendations.
4. **Click 'Recommend'**: The app will provide the top movie recommendations based on your inputs.

## Files
- **`src/app.py`**: The main application file for Streamlit.
- **`src/recommender.py`**: The recommendation engine, containing functions for content-based filtering.
- **`data/movies.csv`**: Contains movie details and genres.
- **`data/ratings.csv`**: Contains user ratings for movies.
- **`data/tags.csv`**: Contains user-defined tags for movies.
- **`data/links.csv`**: Contains links to movie information on IMDb and TMDb.

## Deployed Version
You can access the deployed version of the app here: [https://movies-recommendations-netflix.streamlit.app/](https://movies-recommendations-netflix.streamlit.app/)

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add feature name"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request on the original repository.

## License
This project is licensed under the MIT License.

## Acknowledgments
- The datasets used for this project are sourced from the MovieLens dataset.
- Built with Streamlit, Scikit-Learn, and Pandas.
