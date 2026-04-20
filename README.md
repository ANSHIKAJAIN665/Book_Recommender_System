# 📚 Book Recommendation System

A machine learning-based book recommendation system that suggests similar books using collaborative filtering. The application analyzes user ratings to compute similarity scores and provides personalized recommendations through an interactive web interface built with Streamlit.

---

## 🚀 Features

* Recommend top 5 similar books
* Displays book title, author, and cover image
* Interactive UI using Streamlit
* Handles missing/invalid input
* Dynamic loading of large model files using Google Drive
* Fast and lightweight deployment

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Streamlit
* Machine Learning (Collaborative Filtering)

---

## 📊 How It Works

* Data preprocessing and cleaning
* Creation of pivot table (user-book matrix)
* Similarity score calculation using cosine similarity
* Recommendation based on nearest neighbors

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

https://bookrecommendersystem-ydd2xpsfhjasffhzwcmszd.streamlit.app

---

## 📁 Project Structure

```
book-recommender/
│
├── app.py
├── requirements.txt
├── popular.pkl
├── pt.pkl
├── similarity_score.pkl
├── notebook.ipynb
└── README.md
```

---

## 📌 Dataset

Dataset used: Books Dataset (Kaggle)

---

## ⚠️ Note

Large file `books.pkl` is not included in this repository due to GitHub size limitations.
It is dynamically downloaded from Google Drive during app execution.

---

## 🎯 Future Improvements

* Add search suggestions
* Improve UI design (card layout)
* Add user authentication
* Hybrid recommendation system

---

## 👩‍💻 Author

Anshika Jain

---

## 📜 License

This project is licensed under the MIT License.
