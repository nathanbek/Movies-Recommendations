# Movie Recommendation System

A robust movie recommendation system using both content-based and collaborative filtering techniques, with a user-friendly interface built using Streamlit.

## Project Structure

Movie-Recommendation-System/ ├── data/ │ ├── movies.dat │ ├── ratings.dat │ ├── users.dat ├── notebooks/ │ ├── data_preprocessing.ipynb │ └── model_training.ipynb ├── src/ │ ├── app.py │ ├── recommender.py │ └── utils.py ├── README.md ├── requirements.txt

## Installation

1. Clone the repository.
2. Download the MovieLens 1M dataset and place the `movies.dat`, `ratings.dat`, and `users.dat` files in the `data/` directory.
3. Navigate to the root directory and create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
