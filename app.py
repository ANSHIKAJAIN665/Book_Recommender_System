import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Load data
@st.cache_resource
def load_data():
    popular_df = pickle.load(open('popular.pkl','rb'))
    pt = pickle.load(open('pt.pkl','rb'))
    books = pickle.load(open('books.pkl','rb'))
    similarity_scores = pickle.load(open('similarity_score.pkl','rb'))
    return popular_df, pt, books, similarity_scores

popular_df, pt, books, similarity_scores = load_data()

# Recommend function
def recommend(book_name):
    if book_name not in pt.index:
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

selected_book = st.selectbox("Select a book", pt.index.values)

if st.button("Recommend"):
    with st.spinner("Finding similar books..."):
        results = recommend(selected_book)

        if not results:
            st.error("Book not found")
        else:
            cols = st.columns(5)

            for i, col in enumerate(cols):
                with col:
                    st.image(results[i][2])
                    st.write(results[i][0])
                    st.caption(results[i][1])