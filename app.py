import streamlit as st
import pickle
import numpy as np
import gdown
import os

# Page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Download books.pkl from Google Drive (only if not present)
FILE_ID = "1lpLdrCDoaFn6BceDbgNRJs-Y2g6ccnY5"
BOOKS_PATH = "books.pkl"

if not os.path.exists(BOOKS_PATH):
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    with st.spinner("Downloading model files..."):
        gdown.download(url, BOOKS_PATH, quiet=False)

# Load data (cached for performance)
@st.cache_resource
def load_data():
    try:
        popular_df = pickle.load(open('popular.pkl','rb'))
        pt = pickle.load(open('pt.pkl','rb'))
        books = pickle.load(open('books.pkl','rb'))
        similarity_scores = pickle.load(open('similarity_score.pkl','rb'))
        return popular_df, pt, books, similarity_scores
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None, None

popular_df, pt, books, similarity_scores = load_data()

# Recommendation function
def recommend(book_name):
    if pt is None or book_name not in pt.index:
        return []

    index = np.where(pt.index == book_name)[0][0]
    distances = similarity_scores[index]

    similar_items = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

        if not temp_df.empty:
            data.append((
                temp_df['Book-Title'].values[0],
                temp_df['Book-Author'].values[0],
                temp_df['Image-URL-M'].values[0]
            ))
    return data

# UI
st.title("📚 Book Recommendation System")

if pt is not None:
    selected_book = st.selectbox("Select a book", pt.index.values)

    if st.button("Recommend"):
        with st.spinner("Finding similar books..."):
            results = recommend(selected_book)

            if not results:
                st.warning("No recommendations found")
            else:
                cols = st.columns(min(5, len(results)))

                for i in range(len(results)):
                    with cols[i]:
                        st.image(results[i][2])
                        st.write(results[i][0])
                        st.caption(results[i][1])
else:
    st.error("Data not loaded properly. Please check files.")