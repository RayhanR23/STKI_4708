import subprocess
subprocess.run(["pip", "install", "streamlit", "pandas", "scikit-learn", "numpy", "nltk"])

import streamlit as st
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

nltk.download('stopwords')

# Membaca data dari file CSV
df = pd.read_csv('games.csv')

# Membuat input teks untuk query
query = st.text_input("Masukkan Query")

# Membuat tombol untuk melakukan pencarian
calculate_button = st.button("Cari")

# Menambahkan elemen ke dalam container

# Jika tombol ditekan
if calculate_button:
    # Membuat DataFrame baru untuk query
    query_df = pd.DataFrame({'Title': ['Query'], 'Summary': [query]})

    # Menggabungkan DataFrame query dengan DataFrame asli
    df = pd.concat([df, query_df], ignore_index=True)

    # Menggunakan stop words dari NLTK dan mengonversi ke list
    stop_words = list(stopwords.words('english'))

    # Menggunakan TF-IDF Vectorizer dengan stop words
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(df['Summary'].values.astype('U'))  # Pastikan nilai diubah menjadi Unicode

    # Menghitung cosine similarity
    cosine_similarities = cosine_similarity(X[-1], X[:-1])

    # Mendapatkan urutan indeks berdasarkan skor similaritas
    result_indices = cosine_similarities.argsort()[0][::-1]

    # Menampilkan maksimal 5 hasil pencarian dalam bentuk tabel
    result_data = {'Judul Game': [], 'Isi Summary': [], 'Release Date': [], 'Team': [], 'Genres': [], 'Rating': []}

    displayed_titles = set()    
    for idx in result_indices:        
        if df['Title'][idx] not in displayed_titles and cosine_similarities[0][idx] != 0:
            result_data['Judul Game'].append(df['Title'][idx])
            result_data['Isi Summary'].append(df['Summary'][idx])
            result_data['Release Date'].append(df['Release Date'][idx])
            result_data['Team'].append(df['Team'][idx])
            result_data['Genres'].append(df['Genres'][idx])
            result_data['Rating'].append(df['Rating'][idx])
            displayed_titles.add(df['Title'][idx])            

    result_df = pd.DataFrame(result_data)
    st.table(result_df)
