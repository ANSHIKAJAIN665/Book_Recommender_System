# 📚 Book Recommendation System

A machine learning-based book recommendation system that suggests similar books using collaborative filtering. The application analyzes user ratings to compute similarity scores and provides personalized recommendations through an interactive web interface.

---

## 🚀 Features

* Recommend top 5 similar books
* Displays book title, author, and cover image
* Fast and interactive UI using Streamlit
* Handles invalid or missing inputs
* Easy to deploy on cloud platforms

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
* Similarity score calculation
* Recommendation based on nearest neighbors

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

(Add your Streamlit link here after deployment)

---

## 📁 Project Structure

```
book-recommender/
│
├── app.py
├── requirements.txt
├── popular.pkl
├── pt.pkl
├── books.pkl
├── similarity_score.pkl
├── notebook.ipynb
└── README.md
```

---

## 📌 Dataset

Dataset used: Books Dataset (from Kaggle)

---

## 🎯 Future Improvements

* Add search suggestions
* Improve UI design
* Add user login system
* Hybrid recommendation system

---

## 👩‍💻 Author

Anshika Jain

---

## 📜 License

This project is licensed under the MIT License.
