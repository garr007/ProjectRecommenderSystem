# -*- coding: utf-8 -*-
"""Sistem Rekomendasi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MnK2zZ8QWY0kGssbXRF7SLDEqs-57Jft

# Proyek: Smartphone Recommendation System

## Data Collection

### Import Library
"""

import kagglehub
from google.colab import files
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow import keras
from pathlib import Path
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.layers import Input, Dense
from keras.optimizers import Adam
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import NearestNeighbors
import re
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

"""### Import Data"""

!pip install -q kaggle

files.upload()

from google.colab import drive
drive.mount('/content/drive')

import os
HOME = '/content/drive/MyDrive/SistemRekomendasi/'
print(HOME)

# Commented out IPython magic to ensure Python compatibility.
!mkdir {HOME}/datasets
# %cd {HOME}/datasets

!kaggle datasets download -d shrutiambekar/smartphone-specifications-and-prices-in-india

!unzip -qq /content/drive/MyDrive/SistemRekomendasi/datasets/smartphone-specifications-and-prices-in-india.zip

"""### Data Understanding"""

dataset = pd.read_csv('/content/drive/MyDrive/SistemRekomendasi/datasets/smartphones - smartphones.csv')

dataset.head()

# Menampilkan jumlah baris dan kolom
print("Jumlah baris dan kolom:", dataset.shape)

# Menampilkan jumlah baris saja
print("Jumlah baris:", dataset.shape[0])

# Atau menggunakan metode count() untuk jumlah data di setiap kolom
print("Jumlah data di setiap kolom:")
print(dataset.count())

# Menampilkan informasi lengkap tentang dataset
print("Informasi Dataset:")
dataset.info()

# Menampilkan jumlah nilai unik di setiap kolom
unique_counts = {column: dataset[column].nunique() for column in dataset.columns}

# Mencetak hasil
for column, count in unique_counts.items():
    print(f"Jumlah nilai unik di kolom '{column}': {count}")

# Daftar kolom yang ingin diperiksa
selected_columns = ['sim', 'rating', 'os', 'ram']

# Menampilkan jumlah nilai unik dan nilai unik di setiap kolom yang dipilih
for column in selected_columns:
    if column in dataset.columns:
        unique_values = dataset[column].unique()
        print(f"Nilai unik di kolom '{column}': {unique_values}\n")
    else:
        print(f"Kolom '{column}' tidak ditemukan dalam dataset.\n")

"""#### EDA"""

# Menambahkan kolom product_id dengan ID unik untuk memudahkan visualisasi dan modeling
dataset['product_id'] = ['P' + str(i + 1) for i in range(len(dataset))]

# Buat kolom baru untuk brand agar memudahkan visualisasi
dataset["brand"] = dataset["model"].str.split().str[0]

# Menghapus simbol mata uang dan koma (jika ada) untuk mengonversi ke format numerik untuk memudahkan visualisasi
dataset['price'] = dataset['price'].replace({'₹': '', ',': ''}, regex=True)

# Mengonversi kolom price menjadi tipe data numerik
dataset['price'] = pd.to_numeric(dataset['price'])

"""#### Distribusi Rating Produk"""

# Mengatur ukuran plot
plt.figure(figsize=(10, 6))

# Membuat histogram untuk kolom 'rating'
sns.histplot(data=dataset, x='rating', bins=20, kde=True, color='blue')
plt.title('Distribusi Rating Produk', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Membuat boxplot untuk kolom 'rating'
plt.figure(figsize=(8, 4))
sns.boxplot(data=dataset, x='rating', color='green')
plt.title('Boxplot Rating Produk', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.show()

# Urutkan dataset berdasarkan rating secara menurun
top_rated = dataset.sort_values(by='rating', ascending=False).head(10)

# Buat plot bar untuk produk dengan rating tertinggi
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_rated,
    x='rating',
    y='model',
    color='skyblue'  # Menggunakan warna solid
)

# Tambahkan judul dan label
plt.title('10 Produk dengan Rating Tertinggi', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Model Produk', fontsize=12)

# Tampilkan visualisasi
plt.tight_layout()
plt.show()

"""##### Distribusi Produk Berdasarkan Brand"""

# Hitung distribusi produk berdasarkan brand
plt.figure(figsize=(12, 6))

# Membuat countplot dengan orientasi horizontal agar nama brand lebih terlihat
sns.countplot(data=dataset, y='brand', palette='Set3', order=dataset['brand'].value_counts().index)

# Menambahkan judul dan label
plt.title('Distribusi Brand Produk')
plt.xlabel('Jumlah Produk')
plt.ylabel('Brand')

# Menampilkan grafik
plt.tight_layout()
plt.show()

"""##### Disribusi Harga Produk"""

# Mengatur ukuran plot
plt.figure(figsize=(10, 6))

# Membuat histogram untuk kolom 'price_numeric'
sns.histplot(data=dataset, x='price', bins=20, kde=True, color='orange')
plt.title('Distribusi Harga Produk', fontsize=16)
plt.xlabel('Harga (₹)', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Mengambil 5 produk dengan harga termahal dan termurah
top_5_expensive = dataset.nlargest(5, 'price')
top_5_cheap = dataset.nsmallest(5, 'price')

# Menambahkan kolom 'category' untuk membedakan produk termahal dan termurah
top_5_expensive['category'] = 'Termahal'
top_5_cheap['category'] = 'Termurah'

# Menggabungkan kedua dataframe
top_5_products = pd.concat([top_5_expensive, top_5_cheap])

# Membuat bar plot dengan warna berbeda berdasarkan kategori
plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_products, x='product_id', y='price', hue='category', palette={'Termahal': 'red', 'Termurah': 'green'})

# Menambahkan judul dan label
plt.title('Perbandingan 5 Produk Termahal dan Termurah')
plt.ylabel('Harga (₹)')
plt.xlabel('ID Produk')

# Menambahkan harga di atas setiap batang
for i in range(len(top_5_products)):
    plt.text(i, top_5_products['price'].iloc[i] + 500,
             f"₹{top_5_products['price'].iloc[i]}", ha='center', va='bottom', fontsize=10)

# Menampilkan grafik
plt.tight_layout()
plt.show()

"""## Data Preparation"""

# Penambahan kolom baru yang dibutuhkan untuk tahap Modeling
# Membersihkan karakter non-breaking space dan mengganti satuan TB dengan GB
dataset["ram"] = dataset["ram"].str.replace(r"\u2009", " ", regex=True)

# Mengganti TB dengan GB (jika ada TB di storage, konversi ke GB)
dataset["ram"] = dataset["ram"].str.replace(r"(\d+)\s?TB", lambda x: str(int(x.group(1)) * 1024) + " GB inbuilt", regex=True)

# Ekstraksi RAM dan Storage
dataset[["ram_size", "storage_size"]] = dataset["ram"].str.extract(r"(\d+)\s?GB RAM.*?(\d+)\s?GB inbuilt")

# Mengonversi kolom ram_size dan storage_size ke float
dataset["ram_size"] = dataset["ram_size"].astype(float)
dataset["storage_size"] = dataset["storage_size"].astype(float)

# Membuat kolom battery_capacity dengan regex
dataset['battery_capacity'] = dataset['battery'].str.extract(r'(\d+)\s?mAh').astype(float)

pd.DataFrame({'Missing Value':dataset.isnull().sum()})

# Menampilkan jumlah data duplikat
duplicated_data = pd.DataFrame({'Duplicated Data': [dataset.duplicated().sum()]})

# Menampilkan DataFrame
print(duplicated_data)

# Membersihkan missing value dengan fungsi dropna()
dataset_clean = dataset.dropna()
dataset_clean

# Mengecek kembali missing value pada variabel dataset
dataset_clean.isnull().sum()

# Menampilkan kembali jumlah baris dan kolom
print("Jumlah baris dan kolom:", dataset_clean.shape)

# Menampilkan jumlah baris saja
print("Jumlah baris:", dataset_clean.shape[0])

# Atau menggunakan metode count() untuk jumlah data di setiap kolom
print("Jumlah data di setiap kolom:")
print(dataset_clean.count())

dataset_clean.describe().T

dataset_clean.info()

"""## Model Development"""

dataset_clean = dataset_clean.drop(columns=["sim", "processor", "ram", "battery", "display", "camera", "card"])

# Menampilkan data setelah penghapusan kolom
print(dataset_clean.head())

"""### Model Content Based Filtering

#### Model Content Based Filtering dengan Data Text
"""

text_df = pd.DataFrame(dataset_clean)

# Menggunakan TfidfVectorizer untuk 'os' dan 'brand'
tfidf = TfidfVectorizer(analyzer="word", ngram_range=(1, 2), stop_words="english")

# Menggabungkan 'os' dan 'brand' untuk analisis teks
combined_features = text_df['os'] + ' ' + text_df['brand']

# Transformasi data menggunakan TfidfVectorizer
tfidf_matrix = tfidf.fit_transform(combined_features)

# Menghitung cosine similarity antar produk
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

"""##### Rekomendasi berdasarkan Cosine Similarity"""

# Fungsi rekomendasi berdasarkan cosine similarity untuk fitur 'os' dan 'brand'
def recommend_products_os_brand(product_id, num_recommendations=20):
    # Menampilkan detail produk yang diminta
    input_product = text_df[text_df['product_id'] == product_id]
    print("\nProduk yang diminta:")
    print(input_product[['product_id', 'model', 'os', 'brand']])

    # Mendapatkan indeks dari produk yang diminta
    idx = text_df[text_df['product_id'] == product_id].index[0]

    # Ambil skor cosine similarity dengan produk lainnya
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Urutkan produk berdasarkan similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Ambil rekomendasi berdasarkan urutan similarity (exclude produk itu sendiri)
    sim_scores = sim_scores[1:num_recommendations+1]

    # Ambil produk yang direkomendasikan
    recommended_product_ids = [text_df.iloc[i[0]] for i in sim_scores]

    # Menggabungkan detail produk rekomendasi
    recommended_products = pd.DataFrame(recommended_product_ids)
    recommended_products['similarity_score'] = [i[1] for i in sim_scores]

    # Menampilkan hasil rekomendasi
    print("\n20 Rekomendasi Produk Teratas berdasarkan OS dan Brand:")
    print(recommended_products[['product_id', 'os', 'brand', 'similarity_score']])

    return recommended_products

# Rekomendasi produk berdasarkan produk dengan ID 'P3'
recommended_products = recommend_products_os_brand('P4')

"""##### Rekomendasi dengan Eclidean Distace"""

# Fungsi rekomendasi berdasarkan Euclidean Distance untuk fitur 'os' dan 'brand'
def recommend_products_os_brand_euclidean(product_id, num_recommendations=20):
    # Menampilkan detail produk yang diminta
    input_product = text_df[text_df['product_id'] == product_id]
    print("\nProduk yang diminta:")
    print(input_product[['product_id', 'model', 'os', 'brand']])

    # Mendapatkan indeks dari produk yang diminta
    idx = text_df[text_df['product_id'] == product_id].index[0]

    # Menghitung jarak Euclidean antar produk berdasarkan fitur 'os' dan 'brand'
    euclidean_dist = euclidean_distances(tfidf_matrix[idx], tfidf_matrix)  # tfidf_matrix berisi representasi teks

    # Urutkan produk berdasarkan jarak Euclidean terdekat (kecil lebih mirip)
    sim_scores = list(enumerate(euclidean_dist[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1])  # Urutkan berdasarkan jarak (semakin kecil semakin mirip)

    # Ambil rekomendasi berdasarkan urutan jarak terdekat (exclude produk itu sendiri)
    sim_scores = sim_scores[1:num_recommendations+1]  # Hapus produk yang diminta (index 0)

    # Ambil produk yang direkomendasikan
    recommended_product_ids = [text_df.iloc[i[0]] for i in sim_scores]

    # Menggabungkan detail produk rekomendasi
    recommended_products = pd.DataFrame(recommended_product_ids)
    recommended_products['euclidean_distance'] = [i[1] for i in sim_scores]

    # Menyaring produk yang sama dengan produk yang diminta (bila ada)
    recommended_products = recommended_products[recommended_products['product_id'] != product_id]

    # Menampilkan hasil rekomendasi
    print("\n20 Rekomendasi Produk Teratas berdasarkan Euclidean Distance (tanpa produk yang diminta):")
    print(recommended_products[['product_id', 'os', 'brand', 'euclidean_distance']])

    return recommended_products

# Rekomendasi produk berdasarkan produk dengan ID 'P3'
recommended_products = recommend_products_os_brand_euclidean('P7')

"""#### Model Based Filtering dengan Data Numeric"""

numeric_df = pd.DataFrame(dataset_clean)

# Pilih fitur numerik
features = ['ram_size', 'storage_size', 'battery_capacity']

# Normalisasi data menggunakan StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(numeric_df[features])

# Hitung cosine similarity antar produk
numeric_cosine_sim = cosine_similarity(scaled_features, scaled_features)
numeric_cosine_sim[:4, :4]

"""##### Rekomendasi berdasarkan Cosine Similarity"""

def recommend_products(product_id, num_recommendations=20):
    # Menampilkan detail produk yang diminta
    input_product = numeric_df[numeric_df['product_id'] == product_id]
    print("Produk yang diminta:")
    print(input_product[['product_id', 'model', 'ram_size', 'storage_size', 'battery_capacity']])

    # Mendapatkan indeks dari produk yang diminta
    idx = numeric_df[numeric_df['product_id'] == product_id].index[0]

    # Ambil skor cosine similarity dengan produk lainnya
    sim_scores = list(enumerate(numeric_cosine_sim[idx]))

    # Urutkan produk berdasarkan similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Ambil rekomendasi berdasarkan urutan similarity (exclude produk itu sendiri)
    sim_scores = sim_scores[1:num_recommendations+1]

    # Ambil produk yang direkomendasikan
    recommended_product_ids = [numeric_df.iloc[i[0]] for i in sim_scores]

    # Menggabungkan detail produk rekomendasi
    recommended_products = pd.DataFrame(recommended_product_ids)
    recommended_products['similarity_score'] = [i[1] for i in sim_scores]

     # Menyaring produk yang sama dengan produk yang diminta (bila ada)
    recommended_products = recommended_products[recommended_products['product_id'] != product_id]

    # Menampilkan hasil rekomendasi
    print("\n20 Rekomendasi Produk Teratas:")
    print(recommended_products[['product_id', 'ram_size', 'storage_size', 'battery_capacity','similarity_score']])

    return recommended_products

# Rekomendasi produk berdasarkan produk dengan ID 'P1'
recommended_products = recommend_products('P4')

def recommend_products_euclidean(product_id, num_recommendations=20):
    # Menampilkan detail produk yang diminta
    input_product = numeric_df[numeric_df['product_id'] == product_id]
    print("Produk yang diminta:")
    print(input_product[['product_id', 'ram_size', 'storage_size', 'battery_capacity']])

    # Mendapatkan indeks dari produk yang diminta
    idx = numeric_df[numeric_df['product_id'] == product_id].index[0]

    # Hitung jarak Euclidean antara produk yang diminta dengan produk lainnya
    distances = euclidean_distances([numeric_df.iloc[idx][['ram_size', 'storage_size', 'battery_capacity']]],
                                    numeric_df[['ram_size', 'storage_size', 'battery_capacity']])

    # Dapatkan jarak untuk produk lainnya (exclude produk itu sendiri)
    distances = distances.flatten()
    sorted_indices = distances.argsort()[1:num_recommendations + 1]  # Exclude produk itu sendiri

    # Ambil produk yang direkomendasikan
    recommended_product_ids = numeric_df.iloc[sorted_indices]

    # Gabungkan dengan skor jarak (semakin kecil jarak, semakin mirip)
    recommended_product_ids['distance'] = distances[sorted_indices]

    # Menyaring produk yang sama dengan produk yang diminta (bila ada)
    recommended_product_ids = recommended_product_ids[recommended_product_ids['product_id'] != product_id]

    # Menampilkan hasil rekomendasi
    print("\n20 Rekomendasi Produk Teratas berdasarkan Euclidean Distance:")
    print(recommended_product_ids[['product_id', 'ram_size', 'storage_size', 'battery_capacity', 'distance']])

    return recommended_product_ids

# Rekomendasi produk berdasarkan produk dengan ID 'P1'
recommended_products = recommend_products_euclidean('P14')

"""### Collaborative Filtering

#### Collaborative Filtering dengan Model KKN
"""

df = pd.DataFrame(dataset_clean)

# Pilih fitur yang relevan
features = ['price', 'rating']

# Normalisasi data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

# Melihat hasil normalisasi dalam bentuk DataFrame
scaled_df = pd.DataFrame(scaled_features, columns=features)
# Menampilkan beberapa baris pertama untuk memverifikasi hasil normalisasi
print(scaled_df.head())

# Inisialisasi model KNN
knn_model = NearestNeighbors(metric='euclidean', algorithm='brute')
knn_model.fit(scaled_features)

def recommend_products(product_id, num_recommendations=5):
    # Cari indeks produk berdasarkan ID
    idx = df[df['product_id'] == product_id].index[0]

    # Cari produk paling mirip
    distances, indices = knn_model.kneighbors([scaled_features[idx]], n_neighbors=num_recommendations + 1)

    # Hapus produk itu sendiri dari rekomendasi
    recommendations = []
    for i, dist in zip(indices[0], distances[0]):
        if i != idx:  # Pastikan tidak memasukkan produk input
            recommendations.append({'product_id': df.iloc[i]['product_id'], 'distance': dist})

    # Konversi hasil rekomendasi ke DataFrame
    recommendations_df = pd.DataFrame(recommendations)

    # Gabungkan detail produk dari dataset
    recommended_details = df.loc[df['product_id'].isin(recommendations_df['product_id'])]
    recommended_details = recommended_details.merge(recommendations_df, on='product_id')

    # Urutkan berdasarkan jarak (distance)
    recommended_details = recommended_details.sort_values(by='distance').reset_index(drop=True)

    # Menampilkan hanya informasi yang diminta
    result = recommended_details[['product_id', 'model', 'price', 'rating', 'distance']]

    # Menampilkan informasi produk yang dimasukkan
    input_product = df.loc[df['product_id'] == product_id]
    input_product_details = input_product[['product_id', 'model', 'price', 'rating']]
    print("Informasi Produk yang Dimasukkan:")
    print(input_product_details)

    return result

recommendations = recommend_products('P14', num_recommendations=5)
print("Rekomendasi untuk produk P14:")
print(recommendations)

"""#### Collaborating Filtering dengan Deep Learning Auto Decoder"""

# Definisikan Autoencoder
input_layer = Input(shape=(scaled_features.shape[1],))
encoded = Dense(64, activation='relu')(input_layer)
encoded = Dense(32, activation='relu')(encoded)
encoded = Dense(16, activation='relu')(encoded)

decoded = Dense(32, activation='relu')(encoded)
decoded = Dense(64, activation='relu')(decoded)
output_layer = Dense(scaled_features.shape[1], activation='linear')(decoded)

autoencoder = Model(input_layer, output_layer)
autoencoder.compile(optimizer=Adam(), loss='mse')

# Latih Autoencoder
autoencoder.fit(scaled_features, scaled_features, epochs=50, batch_size=32, shuffle=True)

# Mendapatkan fitur terkompresi (encoded)
encoder = Model(input_layer, encoded)
encoded_features = encoder.predict(scaled_features)

def recommend_products_deep_learning(product_id, num_recommendations=5):
    # Cari indeks produk berdasarkan ID
    idx = df[df['product_id'] == product_id].index[0]

    # Ambil informasi produk yang dimasukkan
    input_product = df.loc[df['product_id'] == product_id]

    # Hitung jarak cosine antar produk berdasarkan fitur terkompresi
    cosine_similarities = np.dot(encoded_features, encoded_features[idx]) / (np.linalg.norm(encoded_features, axis=1) * np.linalg.norm(encoded_features[idx]))

    # Urutkan berdasarkan kemiripan tertinggi
    similar_indices = cosine_similarities.argsort()[-(num_recommendations + 1):-1][::-1]

    recommendations = []
    for i in similar_indices:
        recommendations.append({'product_id': df.iloc[i]['product_id'], 'similarity': cosine_similarities[i]})

    # Konversi hasil rekomendasi ke DataFrame
    recommendations_df = pd.DataFrame(recommendations)

    # Gabungkan detail produk dari dataset
    recommended_details = df.loc[df['product_id'].isin(recommendations_df['product_id'])]
    recommended_details = recommended_details.merge(recommendations_df, on='product_id')

    # Urutkan berdasarkan kemiripan tertinggi (similarity)
    recommended_details = recommended_details.sort_values(by='similarity', ascending=False).reset_index(drop=True)

    # Menampilkan informasi produk yang dimasukkan
    input_product_details = input_product[['product_id', 'model', 'price', 'rating']]
    print("Informasi Produk yang Dimasukkan:")
    print(input_product_details)

    # Menampilkan rekomendasi produk dengan detail yang diminta
    print("\nRekomendasi Produk Teratas:")
    print(recommended_details[['product_id', 'model', 'price', 'rating', 'similarity']])

    return recommended_details

# Contoh penggunaan untuk produk P8
recommendations = recommend_products_deep_learning('P8', num_recommendations=5)

"""### Evaluation"""

# Fungsi untuk cross-validation manual
def manual_cross_val(knn_model, scaled_features, n_splits=3):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    errors = []

    for train_index, test_index in kf.split(scaled_features):
        X_train, X_test = scaled_features[train_index], scaled_features[test_index]
        # Model tidak membutuhkan target y karena hanya mencari tetangga
        # Kita menggunakan jarak yang dihitung dari NearestNeighbors sebagai 'prediksi'

        # Latih model dengan data pelatihan
        knn_model.fit(X_train)

        # Prediksi untuk data uji (hanya mengambil jarak dari tetangga terdekat)
        distances, indices = knn_model.kneighbors(X_test)

        # Hitung error dengan MSE berdasarkan jarak (ini bisa dimodifikasi dengan metrik lain)
        # MSE dihitung berdasarkan jarak antara produk uji dan produk tetangga terdekat
        error = mean_squared_error(X_test, X_train[indices].mean(axis=1))  # Menggunakan rata-rata tetangga terdekat
        errors.append(error)

    return np.mean(errors)

# Menggunakan manual cross-validation
average_error = manual_cross_val(knn_model, scaled_features, n_splits=3)

print(f"Average error from manual cross-validation: {average_error}")

# Rekonstruksi data menggunakan autoencoder
reconstructed_features = autoencoder.predict(scaled_features)

# Hitung MSE
mse = np.mean(np.square(scaled_features - reconstructed_features), axis=1)

# Hitung rata-rata MSE
average_mse = np.mean(mse)
print(f"Rata-rata MSE: {average_mse:.4f}")