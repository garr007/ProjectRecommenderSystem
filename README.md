
- Nama: MUHAMMAD TEGAR ABHIRAM
- Email: tagar.abhiram77@student.ub.ac.id
- Id Dicoding: garrr007

# Proyek: Smartphone System Recomendation 

## Domain Proyek (Latar Belakang)

Dalam era digital yang berkembang pesat, ponsel telah menjadi kebutuhan utama bagi masyarakat modern. Berbagai model ponsel terus bermunculan dengan spesifikasi yang beragam, seperti kapasitas RAM, kualitas kamera, daya tahan baterai, dan jenis sistem operasi. Hal ini menciptakan tantangan bagi konsumen untuk memilih ponsel yang paling sesuai dengan kebutuhan dan preferensi mereka. Menurut laporan Statista (2024), pasar smartphone global diproyeksikan tumbuh dengan tingkat pertumbuhan tahunan sebesar 4,2%, yang menunjukkan meningkatnya permintaan terhadap perangkat mobile.

Namun, keputusan pembelian seringkali menjadi kompleks karena beragamnya pilihan yang tersedia. Survei oleh Deloitte (2023) menemukan bahwa 67% konsumen merasa kesulitan memilih ponsel yang sesuai dengan kebutuhan mereka karena kurangnya informasi yang jelas atau kesulitan dalam membandingkan fitur antar model. Oleh karena itu, sistem rekomendasi berbasis data sangat diperlukan untuk membantu konsumen membuat keputusan yang lebih terinformasi dan efisien.

Proyek ini bertujuan untuk mengembangkan solusi berbasis machine learning yang dapat memberikan rekomendasi ponsel kepada pengguna berdasarkan spesifikasi dan preferensi mereka. Sistem ini diharapkan dapat memberikan rekomendasi yang lebih relevan berdasarkan data objektif seperti harga, rating, dan spesifikasi teknis.

Referensi:
https://www.statista.com/outlook/cmo/consumer-electronics/telephony/smartphones/worldwide?currency=usd

## Business Understanding

### Problem Statements

Dalam perkembangan teknologi yang pesat, pasar ponsel menawarkan berbagai pilihan produk dengan spesifikasi yang sangat beragam. Konsumen sering kali menghadapi beberapa kendala, antara lain:

1. Overload Informasi: Konsumen sulit memproses berbagai informasi dari ratusan hingga ribuan model ponsel yang tersedia di pasar.
2.  Kompleksitas Spesifikasi: Beragamnya spesifikasi teknis, seperti jenis prosesor, kapasitas RAM, kamera, dan sistem operasi, sering kali membingungkan konsumen yang tidak memiliki latar belakang teknis.
3. Ketidakrelevanan Rekomendasi: Rekomendasi generik yang sering kali tidak disesuaikan dengan kebutuhan spesifik pengguna, seperti anggaran, preferensi merek, atau kebutuhan fitur tertentu.
4. Keterbatasan Waktu: Banyak konsumen tidak memiliki cukup waktu untuk membandingkan semua opsi yang tersedia sebelum membuat keputusan pembelian..*


### Goals

Berdasarkan problem statements, berikut tujuan yang ingin dicapai pada proyek ini:

1. Membuat model machine learning yang mampu menganalisis data spesifikasi ponsel dan preferensi pengguna untuk memberikan rekomendasi yang relevan.
2. Menyediakan rekomendasi yang informatif dan personalisasi, sehingga konsumen dapat memilih ponsel sesuai dengan kebutuhan mereka tanpa harus membandingkan secara manual.
## Solution Approach

Untuk mencapai tujuan yang telah ditetapkan, sistem rekomendasi akan dirancang menggunakan pendekatan Content-Based Filtering karena data tidak memiliki user-id. Berikut adalah uraian dari  pendekatan:

1. Content-Based Filtering
Content-Based Filtering adalah metode yang merekomendasikan item berdasarkan kesamaan antara spesifikasi ponsel dalam dataset dengan preferensi pengguna. Pendekatan ini memanfaatkan atribut atau fitur ponsel (seperti , RAM, prosesor, baterai, dan sistem operasi) untuk menemukan item yang relevan.

Cara Kerja:

- Sistem akan menganalisis data spesifikasi ponsel untuk mengidentifikasi fitur-fitur utama.
- Setiap ponsel dalam dataset akan direpresentasikan sebagai vektor fitur.
- Ketika pengguna memberikan preferensi, seperti ram dan baterau, sistem akan menghitung kesamaan (misalnya menggunakan Cosine Similarity atau Eclidean Distance) antara ponsel-ponsel dalam dataset dan preferensi pengguna.
- Ponsel dengan kesamaan tertinggi akan direkomendasikan.

2. Content-Based Filtering dengan KNN 
KNN (K-Nearest Neighbors) pada **content-based filtering** digunakan untuk menemukan produk atau item yang mirip berdasarkan fitur konten mereka (misalnya, harga, kategori, rating, atau deskripsi). Dalam pendekatan ini, KNN menghitung kedekatan atau kemiripan antar item menggunakan metrik jarak seperti **Euclidean distance** atau **cosine similarity**. Produk dengan fitur yang paling mirip dengan item yang sedang dianalisis (misalnya, produk yang dicari atau produk yang sudah dilihat oleh pengguna) akan direkomendasikan sebagai hasil dari KNN.

3. Content-Based Filtering dengan Autoencoder 
Autoencoder dalam **content-based filtering** digunakan untuk mereduksi dimensi fitur konten yang kompleks dan menghasilkan representasi fitur yang lebih kompak dan informatif. Autoencoder adalah jaringan saraf yang dilatih untuk mempelajari cara mengkodekan data masukan ke dalam bentuk yang lebih kecil (dimensi terkompresi) dan kemudian merekonstruksi kembali data tersebut. Setelah pelatihan, representasi terkompresi ini dapat digunakan untuk menghitung kemiripan antar produk menggunakan metrik seperti **cosine similarity** atau **Euclidean distance**. Produk dengan representasi terkompresi yang lebih mirip akan direkomendasikan.

## Data Understanding

### Informasi Dataset

Sumber: [https://www.kaggle.com/datasets/shrutiambekar/smartphone-specifications-and-prices-in-india](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors/data), Kaggle

Datasets yang digunakan berupa  file csv (Comma-Seperated Values).
Dataset yang digunakan memuat dimensi sebesar **1020 baris** dan **11 kolom**. Untuk kolom yang terdapat pada dataset dijabarkan sebagai berikut:

| **No** | **Feature**       | **Description**                                                                 | **Data Type**   |
|-------|--------------------|-------------------------------------------------------------------------------|----------------|
| 1     | **name**          | The name of the mobile phone model.                                           | object         |
| 2     | **price**         | The cost of the mobile phone in the local currency.                          | object         |
| 3     | **rating**        | Average customer rating (out of 5 stars) for the mobile phone.               | float64        |
| 4     | **sim**           | The number of SIM cards supported (e.g., Single SIM, Dual SIM).              | object         |
| 5     | **processor**     | The processor brand and model (e.g., Qualcomm Snapdragon 865).               | object         |
| 6     | **ram**           | Amount of RAM in gigabytes (GB).                                             | object         |
| 7     | **battery**       | Battery capacity in milliampere-hours (mAh).                                 | object         |
| 8     | **display**       | Screen size in inches and resolution (e.g., 6.1 inches, 1080 x 2340 pixels). | object         |
| 9     | **camera**        | Rear camera specifications (e.g., 48 MP + 12 MP + 5 MP).                     | object         |
| 10    | **card**          | External memory card type and maximum capacity (e.g., microSDXC).            | object         |
| 11    | **os**            | Operating system of the mobile phone.                                        | object         |

Jumlah kolom dan baris setelah data diload adalah sebagai berikut:


| Kolom  |Jumlah Data |
|-------------|-----------------|
| model       | 1020            |
| price       | 1020            |
| rating      | 879             |
| sim         | 1020            |
| processor   | 1020            |
| ram         | 1020            |
| battery     | 1020            |
| display     | 1020            |
| camera      | 1019            |
| card        | 1013            |
| os          | 1003            |

### Exploratory Data Analysis 
#### Distribusi Rating Produk 
![grafik 1](https://github.com/user-attachments/assets/1a7875f5-fb57-4764-af84-5b500423171b)

Rating paling sering berada di rentang **80-85**, menunjukkan bahwa mayoritas produk memiliki penilaian positif. Ini menggambarkan bahwa produk dalam dataset cenderung memiliki kualitas yang baik, dengan sebagian besar memperoleh rating tinggi dari pengguna.

Rating secara umum cenderung meningkat dari 60 hingga mencapai puncaknya di sekitar 80-85 sebelum kembali menurun.

#### 10 Produk Dengan Rating Tertinggi
![grafik 3](https://github.com/user-attachments/assets/f73a78d6-524c-44e5-8db7-3ea991c2eb8f)


Produk dengan rating tertinggi adalah OnePlus 11 5G, diikuti oleh Xiaomi 12T Pro 5G dan Infinix Zero Ultra.

Semua produk dalam grafik memiliki rating yang sangat baik, mendekati atau sama.

#### Distribusi Brand Produk 
![grafik 4](https://github.com/user-attachments/assets/129a8cab-aa60-4ebc-927e-d9098559bb50)


Xiaomi dan Samsung adalah dua brand dengan jumlah produk terbanyak, masing-masing melebihi 100 produk.Brand seperti Vivo, Realme, dan Oppo juga memiliki kontribusi besar terhadap total produk.

#### Distribusi Harga Produk 
![grafik 5](https://github.com/user-attachments/assets/a69e3000-b840-4bff-91f6-8fa1ee63d138)

Sebagian besar produk memiliki harga rendah, terbukti dari puncak yang tinggi di kisaran harga rendah (di bawah ₹100.000). 

Grafik ini mengindikasikan bahwa sebagian besar produk berada di kategori harga terjangkau, dengan hanya sedikit produk di kategori harga premium.

#### Perbandingan 5 Produk Termahal dan Termurah
![grafik 6](https://github.com/user-attachments/assets/f77882f2-94e9-45ee-a18b-c201b2426593)



Produk dengan ID P432 memiliki harga tertinggi sebesar ₹650.000, diikuti oleh P922 (₹480.000), dan tiga lainnya di kisaran ₹199.990–₹239.999.
Produk termahal memiliki perbedaan harga yang signifikan, terutama antara P432 dan P922.

Harga produk termurah berada di kisaran ₹99–₹958, dengan produk termurah adalah P609 (₹99).
Harga produk murah cukup seragam dan tidak terlalu bervariasi dibandingkan kelompok termahal.

### Data Preparation 
#### Pembersihan dan Ekstraksi Data

Proses data preparation yang dilakukan bertujuan untuk membersihkan, memproses, dan menambahkan informasi baru pada dataset agar lebih siap untuk analisis, visualisasi, dan modeling. Berikut adalah penjelasan dari langkah-langkah yang dilakukan:

1. Penambahan Kolom Unik product_id
```
dataset['product_id'] = ['P' + str(i + 1) for i in range(len(dataset))]
```
Untuk memberikan ID unik pada setiap produk, sehingga mempermudah pelacakan dan analisis. ID unik dibuat dengan format "P1", "P2", dan seterusnya menggunakan kombinasi string dan indeks.


2. Penambahan Kolom brand
```
dataset["brand"] = dataset["model"].str.split().str[0]
```
Memudahkan analisis berdasarkan merek (brand) dengan mengekstrak nama brand dari kolom model. Nama brand diambil dari kata pertama pada kolom model.

3. Membersihkan Kolom price
```
dataset['price'] = dataset['price'].replace({'₹': '', ',': ''}, regex=True)
```
Menghapus simbol mata uang (₹) dan tanda koma untuk memungkinkan konversi ke format numerik. Menggunakan fungsi replace dengan ekspresi reguler untuk menghapus karakter yang tidak relevan.

4. Konversi price ke Format Numerik
```
dataset['price'] = pd.to_numeric(dataset['price'])
```
Mengubah harga ke tipe numerik agar dapat digunakan dalam visualisasi atau modeling.
Fungsi pd.to_numeric diterapkan setelah pembersihan.


5. Membersihkan dan Memperbaiki Kolom ram
```
dataset["ram"] = dataset["ram"].str.replace(r"\u2009", " ", regex=True)\
dataset["ram"] = dataset["ram"].str.replace(r"(\d+)\s?TB", lambda x: str(int(x.group(1)) * 1024) + " GB inbuilt", regex=True)
```
Menghapus karakter non-breaking space yang dapat mengganggu pemrosesan.
Mengonversi satuan TB ke GB untuk menjaga konsistensi data. Menggunakan replace untuk membersihkan spasi non-breaking.
Ekspresi reguler dengan fungsi lambda untuk mengganti satuan TB ke GB (1 TB = 1024 GB).

6. Ekstraksi RAM dan Storage
```
dataset[["ram_size", "storage_size"]] = dataset["ram"].str.extract(r"(\d+)\s?GB RAM.*?(\d+)\s?GB inbuilt")
dataset["ram_size"] = dataset["ram_size"].astype(float)
dataset["storage_size"] = dataset["storage_size"].astype(float)
```
Memisahkan informasi RAM dan storage ke dalam kolom yang berbeda (ram_size dan storage_size). Ekstraksi menggunakan regex untuk menangkap angka diikuti dengan satuan GB, lalu mengonversinya ke tipe data float.

7. Ekstraksi battery_capacity
```
dataset['battery_capacity'] = dataset['battery'].str.extract(r'(\d+)\s?mAh').astype(float)
```
Membuat kolom baru yang hanya berisi kapasitas baterai dalam mAh. Menggunakan regex untuk mengekstrak angka dari kolom battery, lalu mengonversinya ke tipe data float.

#### Checking Missing Values dan Duplicate Data
##### Checking Missing Values
```
pd.DataFrame({'Missing Value':dataset.isnull().sum()})
```

| No  | Kolom              | Missing Value |
|------|---------------------|---------------|
| 1    | model              | 0             |
| 2    | price              | 0             |
| 3    | rating             | 141           |
| 4    | sim                | 0             |
| 5    | processor          | 0             |
| 6    | ram                | 0             |
| 7    | battery            | 0             |
| 8    | display            | 0             |
| 9    | camera             | 1             |
| 10   | card               | 7             |
| 11   | os                 | 17            |
| 12   | product_id         | 0             |
| 13   | brand              | 0             |
| 14   | ram_size           | 42            |
| 15   | storage_size       | 42            |
| 16   | battery_capacity   | 33            |

Berikut adalah fitur-fitur yang memiliki nilai _null_:
- **rating**: 141
- **camera**: 1
- **card**: 7
- **os**: 17
- **ram_size**: 42
- **ram_size**: 42
- **battery_capacity**: 33

Total nilai _null_ pada dataset adalah 78 + 90 + 67 = **259**

Baris yang memiliki nilai null akan dihapus dengan perintah:
```
dataset_clean = dataset.dropna()
```

##### Checking Duplicate Data
```
duplicated_data = pd.DataFrame({'Duplicated Data': [dataset.duplicated().sum()]})
```

0


Tidak ada dulicated data yang ditemukan pada dataset


Setelah dibersihkan sekarang jumlah kolom dan baris pada data adalah sebagai berikut :
umlah baris dan kolom: `(868, 16)`

Jumlah baris: `868`

Jumlah data di setiap kolom:

| **Kolom**            | **Jumlah Data** |
|-----------------------|-----------------|
| model                | 868             |
| price                | 868             |
| rating               | 868             |
| sim                  | 868             |
| processor            | 868             |
| ram                  | 868             |
| battery              | 868             |
| display              | 868             |
| camera               | 868             |
| card                 | 868             |
| os                   | 868             |
| product_id           | 868             |
| brand                | 868             |
| ram_size             | 868             |
| storage_size         | 868             |
| battery_capacity     | 868             |

#### Content Based Filtering dengan Data Text 
##### Ekstraksi Fitur TF-IDF
```
tfidf = TfidfVectorizer(analyzer="word", ngram_range=(1,  2), stop_words="english")
```
TfidfVectorizer untuk mengonversi kolom os dan brand menjadi representasi fitur berbasis frekuensi kata dan n-gram (1 hingga 2 kata), sambil menghapus kata-kata umum (stop words) dalam bahasa Inggris.
##### Mendefinisikan features 
```
combined_features = text_df['os'] + ' ' + text_df['brand']
```
Menggabungkan kolom 'os' dan 'brand' dalam text_df untuk membentuk sebuah kolom baru yang mengandung kombinasi informasi dari kedua kolom tersebut.
##### Konversi Data
```
tfidf_matrix = tfidf.fit_transform(combined_features)
```
Mengonversi data dari kolom combined_features menjadi matriks TF-IDF
#### Content Based Filtering dengan Data Numeric 
##### Mendefinisikan features 
```
features = ['ram_size',  'storage_size',  'battery_capacity']
```
Memilih kolom-kolom numerik dalam dataset, yaitu ram_size, storage_size, dan battery_capacity, yang akan digunakan untuk analisis atau model yang berfokus pada fitur-fitur numerik tersebut.
##### Normalisasi data
```
scaler = StandardScaler()
scaled_features = scaler.fit_transform(numeric_df[features])
```
Melakukan normalisasi pada kolom-kolom numerik yang telah dipilih (ram_size, storage_size, dan battery_capacity) menggunakan StandardScaler. Proses ini akan mengubah nilai-nilai fitur menjadi distribusi dengan rata-rata 0 dan deviasi standar 1, yang membantu algoritma machine learning dalam mempercepat konvergensi dan meningkatkan performa model yang sensitif terhadap skala data.

#### Content Based Filtering dengan KNN dan Auto Encoder
##### Mendefinisikan features 
```
features = ['price',  'rating']
```
Memilih dua fitur, yaitu 'price' (harga) dan 'rating' (penilaian), dari dataset untuk analisis lebih lanjut
##### Normalisasi data
```
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])
```
Normalisasi pada data harga ('price') dan rating ('rating') menggunakan StandardScaler, yang mengubah data menjadi distribusi dengan rata-rata 0 dan deviasi standar 1.

## Modeling 
Content-based Filtering: Pendekatan ini mengandalkan informasi terkait atribut produk untuk memberikan rekomendasi. Dalam hal ini, digunakan dua ukuran jarak yaitu Cosine Similarity dan Euclidean Distance untuk menghitung kesamaan antara produk-produk berdasarkan fitur yang relevan.

K-Nearest Neighbors (KNN): KNN adalah algoritma supervised yang digunakan untuk klasifikasi atau regresi, tetapi juga dapat digunakan dalam content-based filtering untuk pencarian rekomendasi. KNN bekerja dengan mencari sejumlah **k tetangga terdekat** berdasarkan fitur produk yang telah dinormalisasi.

Deep Learning Auto Encoder: Autoencoder adalah jenis jaringan saraf yang digunakan untuk mereduksi dimensi data. Dalam konteks content-based filtering, autoencoder digunakan untuk mengekstrak fitur yang lebih representatif dari data yang sangat kompleks.

### Content Based Filtering 
#### Cosine Similarity 
Cosine similarity mengukur **sudut** antara dua vektor dalam ruang multidimensi. Semakin kecil sudut antara dua vektor, semakin mirip kedua vektor tersebut. Jika dua vektor memiliki arah yang sama, maka cosine similarity mereka akan mendekati **1**, sedangkan jika arah mereka berlawanan, nilai cosine similarity-nya akan mendekati -1. Jika kedua vektor tegak lurus (tidak ada kesamaan), nilai cosine similarity-nya adalah 0.

Secara matematis, cosine similarity antara dua vektor **A** dan **B** dihitung dengan rumus berikut:

Cosine Similarity = (A ⋅ B) / (||A|| ||B||)

Dimana:
- A dan B adalah dua vektor yang ingin dihitung kesamaannya.
- A ⋅ Badalah hasil perkalian titik (dot product) antara vektor A dan vektor B, yang dihitung dengan menjumlahkan hasil perkalian elemen yang sesuai dari kedua vektor.
  
A ⋅ B = Σ (A_i × B_i)

- ||A|| dan ||B|| adalah panjang (norma) dari masing-masing vektor, yang dihitung menggunakan rumus Euclidean distance:

||A|| = √(Σ A_i²)

||B|| = √(Σ B_i²)

##### Konsep Perhitungan
1. Perkalian Titik (Dot Product): Menghitung total kontribusi antara elemen-elemen yang sesuai dalam kedua vektor. Semakin besar hasil perkalian titik, semakin tinggi kesamaan antara kedua vektor.

2. Normalisasi Vektor: Vektor-divisor digunakan untuk menghilangkan efek panjang vektor dan hanya mempertimbangkan arah vektor. Ini berarti bahwa dua vektor dengan panjang yang berbeda tetap bisa memiliki cosine similarity yang tinggi jika arahnya mirip.

3. Hasil: Nilai hasil dari cosine similarity akan berada dalam rentang antara -1 hingga 1:
   - 1: Vektor memiliki arah yang sama (mereka identik dalam hal fitur).
   - 0: Vektor tegak lurus (tidak ada kesamaan).
   - -1: Vektor memiliki arah yang berlawanan.

Kelebihan:

1. Mengabaikan Skala: Tidak terpengaruh oleh perbedaan ukuran antara data.
2. Efisien dan Sederhana: Mudah dihitung dan cepat diterapkan.
3. Cocok untuk Data Sparse: Efektif untuk data dengan banyak nol, seperti dalam teks atau rekomendasi.
4. Tidak Terpengaruh oleh Magnitudo: Fokus pada arah, bukan ukuran data.

Kekurangan:

1. Tidak Memperhitungkan Magnitudo: Hanya melihat arah, tidak panjang data.
2. Sensitif terhadap Fitur Tidak Relevan: Fitur berisik dapat mempengaruhi hasil.
3. Tidak Cocok untuk Data Non-Linear: Kurang efektif untuk data dengan hubungan yang kompleks.
4. Tidak Menghitung Urutan Data: Tidak memperhitungkan urutan elemen dalam data.

##### Perintah untuk Menghitung Cosine Similarity
```
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
```
Menghitung kemiripan antara produk-produk dalam dataset menggunakan cosine similarity berdasarkan matriks TF-IDF yang telah dihasilkan
##### Cosine Similarity berdasarkan 'os' dan 'brand'
##### Fungsi Rekomendasi
```
# Fungsi rekomendasi berdasarkan cosine similarity untuk fitur 'os' dan 'brand'
def  recommend_products_os_brand(product_id, num_recommendations=20):
# Menampilkan detail produk yang diminta
input_product = text_df[text_df['product_id'] == product_id]
print("\nProduk yang diminta:")
print(input_product[['product_id',  'model',  'os',  'brand']])  
# Mendapatkan indeks dari produk yang diminta
idx = text_df[text_df['product_id'] == product_id].index[0]
# Ambil skor cosine similarity dengan produk lainnya
sim_scores = list(enumerate(cosine_sim[idx]))
# Urutkan produk berdasarkan similarity
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
# Ambil rekomendasi berdasarkan urutan similarity (exclude produk itu sendiri)
sim_scores = sim_scores[1:num_recommendations+1]
# Ambil produk yang direkomendasikan
recommended_product_ids = [text_df.iloc[i[0]]  for i in sim_scores]
# Menggabungkan detail produk rekomendasi
recommended_products = pd.DataFrame(recommended_product_ids)
recommended_products['similarity_score'] = [i[1]  for i in sim_scores]
# Menampilkan hasil rekomendasi
print("\n10 Rekomendasi Produk Teratas berdasarkan OS dan Brand:")
print(recommended_products[['product_id',  'os',  'brand',  'similarity_score']])
return recommended_products
```
Fungsi recommend_products_os_brand memberikan rekomendasi produk berdasarkan kesamaan fitur os dan brand menggunakan cosine similarity, dengan menampilkan produk yang diminta dan 10 produk teratas yang paling mirip berdasarkan skor similarity, mengabaikan produk itu sendiri.
##### Hasil Rekomendasi
```
recommended_products = recommend_products_os_brand('P4')
```

Produk yang Diminta

| **product_id** | **model**               | **os**        | **brand**    |
|----------------|-------------------------|---------------|--------------|
| P4             | Motorola Moto G62 5G    | Android v12   | Motorola     |

10 Rekomendasi Produk Teratas Berdasarkan OS dan Brand

| **product_id** | **os**        | **brand**   | **similarity_score** |
|----------------|---------------|-------------|----------------------|
| P54            | Android v12   | Motorola    | 1.000000             |
| P60            | Android v12   | Motorola    | 1.000000             |
| P81            | Android v12   | Motorola    | 1.000000             |
| P93            | Android v12   | Motorola    | 1.000000             |
| P127           | Android v12   | Motorola    | 1.000000             |
| P152           | Android v12   | Motorola    | 1.000000             |
| P188           | Android v12   | Motorola    | 1.000000             |
| P195           | Android v12   | Motorola    | 1.000000             |
| P205           | Android v12   | Motorola    | 1.000000             |
| P351           | Android v12   | Motorola    | 1.000000             |
Hasil ini menunjukkan rekomendasi produk berdasarkan kesamaan fitur os dan brand. Produk yang diminta, yaitu P4 (Motorola Moto G62 5G, Android v12), memiliki beberapa produk yang sangat mirip (dengan skor similarity 1.000000), yang semuanya menjalankan Android v12 dan berasal dari merek Motorola.
#### Cosine Similarity berdasarkan data numeric berdasarkan ram size, storage size, dan battery capacity
##### Fungsi Rekomendasi
```
def  recommend_products(product_id, num_recommendations=20):
# Menampilkan detail produk yang diminta
input_product = numeric_df[numeric_df['product_id'] == product_id]
print("Produk yang diminta:")
print(input_product[['product_id',  'model',  'ram_size',  'storage_size',  'battery_capacity']])
# Mendapatkan indeks dari produk yang diminta
idx = numeric_df[numeric_df['product_id'] == product_id].index[0]
# Ambil skor cosine similarity dengan produk lainnya
sim_scores = list(enumerate(numeric_cosine_sim[idx]))
# Urutkan produk berdasarkan similarity
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# Ambil rekomendasi berdasarkan urutan similarity (exclude produk itu sendiri)
sim_scores = sim_scores[1:num_recommendations+1]
# Ambil produk yang direkomendasikan
recommended_product_ids = [numeric_df.iloc[i[0]]  for i in sim_scores] 
# Menggabungkan detail produk rekomendasi
recommended_products = pd.DataFrame(recommended_product_ids)
recommended_products['similarity_score'] = [i[1]  for i in sim_scores] 
# Menyaring produk yang sama dengan produk yang diminta (bila ada)
recommended_products = recommended_products[recommended_products['product_id'] != product_id]  
# Menampilkan hasil rekomendasi
print("\n10 Rekomendasi Produk Teratas:")
print(recommended_products[['product_id',  'ram_size',  'storage_size',  'battery_capacity','similarity_score']]) 
return recommended_products
```
Memberikan rekomendasi produk berdasarkan cosine similarity antara produk yang diminta dan produk lainnya, menggunakan fitur numerik seperti ram_size, storage_size, dan battery_capacity. Fungsi ini menampilkan produk yang diminta dan 10 produk teratas yang paling mirip berdasarkan skor similarity, mengabaikan produk itu sendiri dalam rekomendasi.
##### Hasil Rekomendasi
```
recommended_products = recommend_products('P4')
```
Produk yang Diminta

| **product_id** | **model**               | **ram_size** | **storage_size** | **battery_capacity** |
|----------------|-------------------------|--------------|------------------|----------------------|
| P4             | Motorola Moto G62 5G    | 6.0          | 128.0            | 5000.0               |

10 Rekomendasi Produk Teratas

| **product_id** | **ram_size** | **storage_size** | **battery_capacity** | **similarity_score** |
|----------------|--------------|------------------|----------------------|----------------------|
| P5             | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P6             | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P11            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P13            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P14            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P32            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P35            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P41            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P42            | 6.0          | 128.0            | 5000.0               | 1.0                  |
| P43            | 6.0          | 128.0            | 5000.0               | 1.0                  |
Hasil ini menunjukkan bahwa produk yang diminta, yaitu Motorola Moto G62 5G (P4), memiliki banyak produk lain yang memiliki skor cosine similarity yang sangat tinggi (nilai 1), yang berarti produk-produk tersebut memiliki kesamaan yang sangat mirip dalam hal ram_size, storage_size, dan battery_capacity. Semua produk yang direkomendasikan (P5, P6, P11, dll.) memiliki fitur yang identik dengan produk yang diminta, yang menghasilkan skor similarity sempurna.
#### Euclidean Distance 
Euclidean Distance adalah ukuran yang digunakan untuk menghitung jarak antara dua titik dalam ruang multidimensi. Dalam konteks sistem rekomendasi produk, Euclidean Distance digunakan untuk mengukur kedekatan antara dua produk berdasarkan fitur-fitur yang dimilikinya (seperti ukuran RAM, kapasitas penyimpanan, dan daya baterai).

##### Cara Kerja Euclidean Distance

Secara umum, Euclidean Distance mengukur jarak linear antara dua titik dalam ruang tersebut. Setiap produk direpresentasikan sebagai titik dalam ruang, dan jarak antara dua titik dihitung dengan menggunakan rumus Euclidean.

##### Rumus Euclidean Distance

Rumus Euclidean Distance antara dua titik A dan B adalah sebagai berikut:

d(A, B) = √[(x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²]

Di mana:
- x₁, y₁, z₁ adalah fitur produk pertama (misalnya RAM, kapasitas penyimpanan, dan daya baterai),
- x₂, y₂, z₂ adalah fitur produk kedua,
- d(A, B) adalah jarak Euclidean antara produk A dan B.

Jika produk memiliki lebih dari tiga fitur, rumusnya diperluas menjadi:

d(A, B) = √[(x₁ - x₂)² + (y₁ - y₂)² + (z₁ - z₂)² + ...]

**Kelebihan:**

1. **Mudah Dipahami dan Dihitung**: Mengukur jarak langsung antara dua titik dalam ruang fitur.
2. **Cocok untuk Data Berukuran Sama**: Efektif jika data memiliki skala dan ukuran yang sama.
3. **Kesesuaian dengan Jarak Fisik**: Cocok untuk masalah yang melibatkan jarak nyata, seperti pengenalan pola dan pengelompokan.

**Kekurangan:**

1. **Sensitif terhadap Skala**: Tidak dapat mengatasi fitur dengan skala yang berbeda tanpa normalisasi.
2. **Terpengaruh Outlier**: Nilai ekstrim dapat memengaruhi perhitungan jarak secara signifikan.
3. **Tidak Baik untuk Data Spars**: Kurang efektif ketika data memiliki banyak nol atau elemen yang hilang.
4. **Kurang Tepat untuk Data Non-Linear**: Tidak cocok untuk data yang memiliki hubungan non-linear atau kompleks.

##### Euclidean Distance berdasarkan 'os' dan 'brand'
##### Fungsi Rekomendasi
```
# Fungsi rekomendasi berdasarkan Euclidean Distance untuk fitur 'os' dan 'brand'
def  recommend_products_os_brand_euclidean(product_id, num_recommendations=20):
# Menampilkan detail produk yang diminta
input_product = text_df[text_df['product_id'] == product_id]
print("\nProduk yang diminta:")
print(input_product[['product_id',  'model',  'os',  'brand']])
# Mendapatkan indeks dari produk yang diminta
idx = text_df[text_df['product_id'] == product_id].index[0]
# Menghitung jarak Euclidean antar produk berdasarkan fitur 'os' dan 'brand'
euclidean_dist = euclidean_distances(tfidf_matrix[idx], tfidf_matrix)  
# tfidf_matrix berisi representasi teks
# Urutkan produk berdasarkan jarak Euclidean terdekat (kecil lebih mirip)
sim_scores = list(enumerate(euclidean_dist[0]))
sim_scores = sorted(sim_scores, key=lambda x: x[1])  # Urutkan berdasarkan jarak (semakin kecil semakin mirip)
# Ambil rekomendasi berdasarkan urutan jarak terdekat (exclude produk itu sendiri)
sim_scores = sim_scores[1:num_recommendations+1]  # Hapus produk yang diminta (index 0)
# Ambil produk yang direkomendasikan
recommended_product_ids = [text_df.iloc[i[0]]  for i in sim_scores]
# Menggabungkan detail produk rekomendasi
recommended_products = pd.DataFrame(recommended_product_ids)
recommended_products['euclidean_distance'] = [i[1]  for i in sim_scores]
# Menyaring produk yang sama dengan produk yang diminta (bila ada)
recommended_products = recommended_products[recommended_products['product_id'] != product_id]
# Menampilkan hasil rekomendasi
print("\n10 Rekomendasi Produk Teratas berdasarkan Euclidean Distance (tanpa produk yang diminta):")
print(recommended_products[['product_id',  'os',  'brand',  'euclidean_distance']]
return recommended_products
```
Fungsi recommend_products_os_brand_euclidean memberikan rekomendasi produk berdasarkan jarak Euclidean Distance antara produk yang diminta dan produk lain, menggunakan fitur os dan brand. Produk dengan jarak Euclidean terkecil dianggap paling mirip, dan fungsi ini menampilkan 10 produk teratas yang paling mirip berdasarkan jarak tersebut.
##### Hasil Rekomendasi
```
recommended_products = recommend_products_os_brand_euclidean('P7')
```
Produk yang Diminta:
| Product ID | Model             | OS       | Brand  |
|------------|-------------------|----------|--------|
| P7         | Apple iPhone 14   | iOS v16  | Apple  |

10 Rekomendasi Produk Teratas Berdasarkan Euclidean Distance (tanpa produk yang diminta):

| Product ID | OS        | Brand | Euclidean Distance |
|------------|-----------|-------|--------------------|
| P28        | iOS v16   | Apple | 0.000000           |
| P57        | iOS v16   | Apple | 0.000000           |
| P101       | iOS v16   | Apple | 0.000000           |
| P211       | iOS v16   | Apple | 0.000000           |
| P248       | iOS v16   | Apple | 0.000000           |
| P291       | iOS v16   | Apple | 0.000000           |
| P324       | iOS v16   | Apple | 0.000000           |
| P421       | iOS v16   | Apple | 0.000000           |
| P637       | iOS v16   | Apple | 0.000000           |
| P765       | iOS v16   | Apple | 0.000000           |
Hasil ini menunjukkan rekomendasi produk berdasarkan Euclidean Distance dari produk yang diminta, P7 (Apple iPhone 14, iOS v16). Produk dengan Euclidean Distance 0.000000 memiliki kesamaan yang sangat tinggi (berjalan dengan iOS v16 dan merek Apple).
##### Euclidean Distance  berdasarkan data numeric berdasarkan ram size, storage size, dan battery capacity
##### Fungsi Rekomendasi
```
def  recommend_products_euclidean(product_id, num_recommendations=20):
# Menampilkan detail produk yang diminta
input_product = numeric_df[numeric_df['product_id'] == product_id]
print("Produk yang diminta:")
print(input_product[['product_id',  'ram_size',  'storage_size',  'battery_capacity']])
# Mendapatkan indeks dari produk yang diminta
idx = numeric_df[numeric_df['product_id'] == product_id].index[0]
# Hitung jarak Euclidean antara produk yang diminta dengan produk lainnya
distances = euclidean_distances([numeric_df.iloc[idx][['ram_size',  'storage_size',  'battery_capacity']]],
numeric_df[['ram_size',  'storage_size',  'battery_capacity']])
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
print("\n10 Rekomendasi Produk Teratas berdasarkan Euclidean Distance:")
print(recommended_product_ids[['product_id',  'ram_size',  'storage_size',  'battery_capacity',  'distance']])
return recommended_product_ids
```
Fungsi ini digunakan untuk memberikan rekomendasi produk berdasarkan jarak Euclidean antara produk yang diminta dengan produk lainnya, menggunakan fitur ram_size, storage_size, dan battery_capacity. Produk yang memiliki jarak terdekat (nilai Euclidean terkecil) akan dianggap paling mirip dan disarankan sebagai rekomendasi
##### Hasil rekomendasi
```
recommended_products = recommend_products_os_brand_euclidean('P7')
```
Produk yang Diminta:
| Product ID | RAM Size | Storage Size | Battery Capacity |
|------------|----------|--------------|------------------|
| P14        | 6.0      | 128.0        | 5000.0           |

10 Rekomendasi Produk Teratas Berdasarkan Euclidean Distance:

| Product ID | RAM Size | Storage Size | Battery Capacity | Distance |
|------------|----------|--------------|------------------|----------|
| P834       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P290       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P151       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P655       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P139       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P138       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P135       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P315       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P634       | 6.0      | 128.0        | 5000.0           | 0.0      |
| P129       | 6.0      | 128.0        | 5000.0           | 0.0      |
Hasil ini menunjukkan bahwa produk yang diminta (P14) memiliki beberapa produk lain yang sangat mirip, dengan jarak Euclidean 0, yang berarti mereka memiliki nilai ram_size, storage_size, dan battery_capacity yang sama persis. Produk-produk ini disarankan karena fitur-fitur teknis mereka sangat mirip dengan produk yang diminta.

#### Dengan KKN 
K-Nearest Neighbors (KNN) adalah algoritma yang digunakan untuk mencari "tetangga terdekat", yaitu produk yang memiliki kemiripan dengan produk yang sudah diberikan preferensi oleh pengguna. Dalam **Content-Based Filtering**, KNN digunakan untuk mencari produk yang memiliki kesamaan dalam atribut-atribut konten (seperti kategori, harga, atau deskripsi) dengan produk yang sudah disukai atau dipilih oleh pengguna.
Berikut adalah langkah-langkah dasar dalam Content-Based Filtering menggunakan KNN:

1.  Matriks Fitur Produk:
    
    -   Data input berupa matriks fitur produk yang berisi informasi terkait atribut produk (seperti kategori, harga, spesifikasi, atau deskripsi). Setiap produk direpresentasikan sebagai vektor fitur.
2.  **Mencari Kemiripan (Similarity):
    
    -   Menggunakan algoritma KNN untuk menghitung kemiripan antar produk berdasarkan atribut fitur yang relevan.
    -   Ukuran kemiripan yang umum digunakan adalah **Cosine Similarity** atau **Euclidean Distance**.
3.  Menentukan K (Jumlah Tetangga):
    
    -   KNN membutuhkan parameter `K` untuk menentukan jumlah produk terdekat yang akan dipertimbangkan untuk rekomendasi. Misalnya, jika `K=5`, maka lima produk terdekat akan digunakan untuk menghasilkan rekomendasi berdasarkan kesamaan fitur.
4.  Membuat Rekomendasi:
    
    -   Berdasarkan kemiripan yang dihitung, produk-produk yang mirip dengan produk yang sudah dipilih atau disukai oleh pengguna akan direkomendasikan.

Kelebihan:

1.  Mudah Dipahami dan Implementasi: KNN adalah algoritma yang sederhana, mudah dipahami, dan dapat diimplementasikan tanpa memerlukan model yang kompleks.
2.  Tidak Memerlukan Data Pengguna: KNN hanya bergantung pada informasi konten produk, sehingga cocok digunakan untuk rekomendasi tanpa perlu melibatkan data pengguna.
3.  Rekomendasi Berdasarkan Fitur Produk: KNN menghasilkan rekomendasi berdasarkan kesamaan fitur produk, yang memungkinkan sistem untuk memberikan rekomendasi produk yang serupa dengan yang telah disukai atau dipilih pengguna.

Kekurangan:
1.  Komputasi Berat: Menghitung jarak antara produk satu dengan lainnya membutuhkan banyak sumber daya, terutama ketika dataset produk besar.
2.  Kurang Efektif pada Data Spars: Jika banyak fitur produk yang hilang atau tidak lengkap, KNN bisa kurang efektif karena perhitungan kemiripan akan menjadi kurang akurat.
3.  Memerlukan Banyak Memori: KNN perlu menyimpan seluruh dataset produk untuk melakukan prediksi, yang bisa menjadi tidak efisien jika dataset besar.
##### Inisialisasi Model KKN 
```
knn_model = NearestNeighbors(metric='euclidean', algorithm='brute')
knn_model.fit(scaled_features)
```
Menginisialisasi model K-Nearest Neighbors (KNN) dengan metrik jarak Euclidean dan algoritma brute-force untuk pencarian tetangga terdekat, kemudian melatih model menggunakan data fitur yang sudah dinormalisasi.
##### Fungsi Rekomendasi Berdasarkan KNN
```
def  recommend_products(product_id, num_recommendations=5):
# Cari indeks produk berdasarkan ID
idx = df[df['product_id'] == product_id].index[0] 
# Cari produk paling mirip
distances, indices = knn_model.kneighbors([scaled_features[idx]], n_neighbors=num_recommendations + 1)
# Hapus produk itu sendiri dari rekomendasi
recommendations = []
for i, dist in  zip(indices[0], distances[0]):
if i != idx:  # Pastikan tidak memasukkan produk input
recommendations.append({'product_id': df.iloc[i]['product_id'],  'distance': dist})
# Konversi hasil rekomendasi ke DataFrame
recommendations_df = pd.DataFrame(recommendations)
# Gabungkan detail produk dari dataset
recommended_details = df.loc[df['product_id'].isin(recommendations_df['product_id'])]
recommended_details = recommended_details.merge(recommendations_df, on='product_id')
# Urutkan berdasarkan jarak (distance)
recommended_details = recommended_details.sort_values(by='distance').reset_index(drop=True)
# Menampilkan hanya informasi yang diminta
result = recommended_details[['product_id',  'model',  'price',  'rating',  'distance']]
# Menampilkan informasi produk yang dimasukkan
input_product = df.loc[df['product_id'] == product_id]
input_product_details = input_product[['product_id',  'model',  'price',  'rating']]
print("Informasi Produk yang Dimasukkan:")
print(input_product_details)
return result
```
Fungsi ini memberikan rekomendasi produk berdasarkan kedekatannya dengan produk yang dimasukkan, menggunakan model KNN untuk menghitung jarak antara produk, dan mengembalikan produk yang paling mirip beserta informasi harga, rating, dan jarak dari produk yang diminta.
##### Hasil Rekomendasi
```
recommendations = recommend_products('P14', num_recommendations=5)
```
Informasi Produk yang Dimasukkan:
| product_id | model                                | price  | rating |
|------------|--------------------------------------|--------|--------|
| P14        | Vivo T1 5G (6GB RAM + 128GB)         | 16990  | 80.0   |

Rekomendasi Produk untuk P14:
| product_id | model                               | price  | rating | distance |
|------------|-------------------------------------|--------|--------|----------|
| P543       | OPPO K10 (8GB RAM + 128GB)          | 16990  | 80.0   | 0.000000 |
| P6         | Samsung Galaxy F23 5G (6GB RAM + 128GB) | 16999  | 80.0   | 0.000248 |
| P315       | Motorola Moto G71 5G               | 16999  | 80.0   | 0.000248 |
| P320       | Honor X9 5G                        | 16999  | 80.0   | 0.000248 |
| P696       | Infinix Note 13 Pro                | 16999  | 80.0   | 0.000248 |
| P792       | Realme Narzo 30 5G                 | 16999  | 80.0   | 0.000248 |
| P254       | iQOO Z6 5G (6GB RAM + 128GB)       | 16940  | 80.0   | 0.001377 |
| P649       | Vivo Y33s                           | 16685  | 80.0   | 0.008399 |
| P444       | Samsung Galaxy A32                 | 16499  | 80.0   | 0.013521 |
| P572       | Xiaomi Redmi Note 9 Pro Max        | 16490  | 80.0   | 0.013769 |
Hasil rekomendasi menunjukkan daftar produk yang paling mirip dengan produk Vivo T1 5G (6GB RAM + 128GB) berdasarkan jarak yang dihitung dengan model KNN. Produk yang paling mirip adalah Xiaomi 12T Pro 5G, dengan jarak 0.000, yang memiliki harga lebih tinggi dan rating yang lebih tinggi. Produk-produk lain dalam daftar juga memiliki jarak yang sangat kecil, yang menunjukkan kesamaan fitur seperti harga dan rating, dengan sedikit perbedaan harga yang masih relatif terjangkau jika dibandingkan dengan produk yang diminta.

#### Dengan Autoencoder 
Autoencoder adalah jenis jaringan saraf yang digunakan untuk mempelajari representasi terkompresi dari data, yang dapat diterapkan dalam **Content-Based Filtering**. Dalam konteks ini, Autoencoder digunakan untuk mempelajari representasi tersembunyi dari fitur-fitur produk (seperti spesifikasi, kategori, atau deskripsi) untuk membuat rekomendasi berdasarkan kemiripan antara produk.

Langkah-langkah dalam Content-Based Filtering dengan Autoencoder:

1.  Preprocessing Data:
    
    -   Fitur-fitur produk yang relevan (seperti harga, rating, spesifikasi, dan deskripsi) dikumpulkan dan diproses. Data ini kemudian dinormalisasi atau diubah ke dalam format yang sesuai agar bisa digunakan sebagai input untuk model Autoencoder.
2.  Pelatihan Autoencoder:
    
    -   Autoencoder dilatih untuk mempelajari representasi tersembunyi dari fitur produk tersebut. Model berusaha untuk memampatkan data input (fitur produk) ke dalam bentuk yang lebih kecil dan kemudian merekonstruksinya seakurat mungkin. Selama pelatihan, model ini meminimalkan error antara data asli dan data yang telah direkonstruksi.
3.  Rekonstruksi dan Rekomendasi:
    
    -   Setelah pelatihan selesai, Autoencoder dapat digunakan untuk merekonstruksi fitur-fitur produk yang belum ada data lengkapnya. Produk yang memiliki representasi tersembunyi yang mirip dengan produk yang dicari pengguna akan lebih mungkin untuk direkomendasikan.

Kelebihan:

1.  Pengurangan Dimensi:
    
    -   Autoencoder mengurangi dimensi data fitur produk, yang memungkinkan pemrosesan data yang lebih efisien dan dapat mengurangi masalah sparsity pada dataset produk.
2.  Menangani Fitur yang Beragam:
    
    -   Autoencoder dapat menangani berbagai jenis data fitur produk, termasuk data numerik dan kategorikal, dengan lebih baik, yang membuatnya fleksibel untuk berbagai jenis produk.
3.  Kemampuan Menangkap Pola Tersembunyi:
    
    -   Dengan representasi tersembunyi yang dihasilkan, Autoencoder dapat menangkap pola-pola kompleks antar fitur produk yang mungkin tidak terlihat secara langsung. Hal ini memungkinkan rekomendasi yang lebih relevan bagi pengguna.

Kekurangan:

1.  Kompleksitas Model:
    
    -   Proses pelatihan Autoencoder untuk Content-Based Filtering memerlukan sumber daya komputasi yang lebih banyak dan bisa lebih kompleks dibandingkan dengan metode berbasis aturan atau metode lain yang lebih sederhana.
2.  Kesulitan dalam Interpretasi:
    
    -   Karena Autoencoder mempelajari representasi tersembunyi, sulit untuk menginterpretasi apa yang sebenarnya terjadi di dalam model dan bagaimana representasi tersembunyi tersebut mempengaruhi keputusan rekomendasi.
3.  Masalah Overfitting:
    
    -   Autoencoder dapat mengalami overfitting jika data latih tidak cukup beragam atau terlalu kecil. Ini bisa menyebabkan model menghasilkan rekomendasi yang kurang generalizable.
##### Mendefinisikan Model 
```
input_layer = Input(shape=(scaled_features.shape[1],))
encoded = Dense(64, activation='relu')(input_layer)
encoded = Dense(32, activation='relu')(encoded)
encoded = Dense(16, activation='relu')(encoded)

decoded = Dense(32, activation='relu')(encoded)
decoded = Dense(64, activation='relu')(decoded)
output_layer = Dense(scaled_features.shape[1], activation='linear')(decoded)

autoencoder = Model(input_layer, output_layer)
autoencoder.compile(optimizer=Adam(), loss='mse')
```
Mendefinisikan model autoencoder untuk mengurangi dimensi data dan mempelajari representasi yang lebih kompak dari fitur produk. Berikut penjelasan singkat setiap bagian:

Input Layer: Layer pertama yang menerima input dengan jumlah fitur yang sesuai dengan data yang telah dinormalisasi (scaled_features.shape[1]).
Encoder: Bagian dari model yang bertanggung jawab untuk mereduksi dimensi data. Terdiri dari tiga layer berturut-turut dengan ukuran masing-masing 64, 32, dan 16 unit, dengan fungsi aktivasi ReLU.

Decoder: Bagian yang bertugas mengembalikan data ke bentuk semula setelah dikompresi oleh encoder. Terdiri dari dua layer berturut-turut dengan ukuran 32 dan 64 unit, dan juga menggunakan ReLU sebagai fungsi aktivasi.

Output Layer: Layer terakhir yang menghasilkan output yang memiliki dimensi yang sama dengan input, dengan fungsi aktivasi linear (untuk memastikan output tetap dalam rentang nilai kontinu).

Model Compile: Model autoencoder dikompilasi menggunakan optimizer Adam dan loss function Mean Squared Error (MSE), yang umum digunakan untuk tugas regresi dan pembelajaran representasi.
##### Melatih Model
```
autoencoder.fit(scaled_features, scaled_features, epochs=50, batch_size=32, shuffle=True)
```
Melatih model autoencoder yang telah didefinisikan menggunakan data fitur yang telah dinormalisasi (scaled_features)
##### Hasil Fitur
```
encoder = Model(input_layer, encoded)
encoded_features = encoder.predict(scaled_features)
```
Menghasilkan fitur terkompresi dari model autoencoder yang telah dilatih.
##### Hasil Rekomendasi
```
recommendations = recommend_products_deep_learning('P8', num_recommendations=5)
```
Informasi Produk yang Dimasukkan:
| product_id | model                            | price  | rating |
|------------|----------------------------------|--------|--------|
| P8         | Xiaomi Redmi Note 12 Pro Plus   | 29999  | 86.0   |

Rekomendasi Produk Teratas:
| product_id | model                            | price  | rating | similarity |
|------------|----------------------------------|--------|--------|------------|
| P360       | Poco F4 (12GB RAM + 256GB)       | 29999  | 86.0   | 1.000000   |
| P721       | Vivo V21s                        | 29999  | 86.0   | 1.000000   |
| P747       | Xiaomi Mi 10T Pro 5G            | 29999  | 86.0   | 1.000000   |
| P37        | Oppo Reno 8T                     | 29990  | 87.0   | 0.999945   |
| P154       | Oppo A98                         | 30990  | 87.0   | 0.999939   |
| P509       | Honor 70 5G (8GB RAM + 256GB)    | 30990  | 86.0   | 0.999914   |
| P811       | Xiaomi Redmi K60i               | 28999  | 85.0   | 0.999901   |
| P1018      | POCO X4 GT 5G (8GB RAM + 256GB)  | 28990  | 85.0   | 0.999900   |
| P62        | Vivo S16                         | 29990  | 85.0   | 0.999896   |
| P942       | Xiaomi Civi 2                    | 29999  | 85.0   | 0.999895   |
Menunjukkan rekomendasi produk yang sangat mirip dengan produk yang dimasukkan, yaitu Xiaomi Redmi Note 12 Pro Plus (P8). Berdasarkan fitur terkompresi yang dihasilkan oleh model autoencoder dan dihitung menggunakan cosine similarity

### Evaluasi 
Metrik Evaluasi: Mean Squared Error (MSE)

MSE (Mean Squared Error) digunakan untuk mengukur perbedaan antara nilai yang diprediksi oleh model dengan nilai yang sebenarnya. Dalam konteks ini, MSE digunakan untuk mengukur kesalahan prediksi berdasarkan jarak antara produk uji dan rata-rata produk tetangga terdekat.

MSE = (1 / n) * Σ (y_i - ŷ_i)²

Di mana:

y_i adalah nilai sebenarnya (data observasi),

ŷ_i adalah nilai prediksi (nilai yang diprediksi oleh model),
n adalah jumlah data atau sampel.

MSE mengukur rata-rata kuadrat perbedaan antara nilai prediksi dan nilai sebenarnya, semakin kecil nilai MSE, semakin baik prediksi model.

##### Evaluasi model KKN Menggunakan manual cross-validation
##### Fungsi Evaluasi
```
# Fungsi untuk cross-validation manual
def  manual_cross_val(knn_model, scaled_features, n_splits=3):
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
```
Melakukan cross-validation manual untuk mengevaluasi model K-Nearest Neighbors (KNN) dengan menggunakan data yang telah dinormalisasi
##### Hasil Evaluasi 
```
average_error = manual_cross_val(knn_model, scaled_features, n_splits=3)
```

Nilai rata-rata error sebesar 0.1496 dari manual cross-validation menunjukkan seberapa besar perbedaan rata-rata antara prediksi (berdasarkan jarak tetangga terdekat) dan nilai aktual untuk data uji. Meskipun nilai error ini terbilang kecil, ini menunjukkan bahwa model K-Nearest Neighbors (KNN) yang digunakan bekerja dengan cukup baik dalam merekomendasikan produk berdasarkan jarak Euclidean antar fitur-fitur yang telah dinormalisasi.

#### Kesimpulan 
Evaluasi Terhadap Problem Statements
-   Overload Informasi
    -   Masalah: Banyaknya informasi spesifikasi ponsel membuat konsumen kesulitan membuat keputusan.
    -   Solusi: Model KNN yang dibangun berhasil memberikan rekomendasi yang relevan berdasarkan kesamaan fitur antarproduk. Dengan rata-rata error sebesar 0.1496, model mampu memberikan hasil yang cukup akurat, sehingga mengurangi kebutuhan konsumen untuk menyaring informasi secara manual.
    -   Dampak: Mengurangi beban kognitif konsumen dengan menyajikan daftar rekomendasi yang ringkas dan relevan.
-   Kompleksitas Spesifikasi
    
    -   Masalah: Beragamnya spesifikasi teknis sering membingungkan konsumen yang tidak memiliki latar belakang teknis.
    -   Solusi: Model menggunakan fitur-fitur yang terstruktur, seperti RAM, kapasitas penyimpanan, harga, dan rating, yang diolah menjadi jarak Euclidean untuk menentukan tingkat kesamaan produk.
    -   Dampak: Model mengabstraksikan kompleksitas spesifikasi menjadi rekomendasi sederhana yang mudah dipahami konsumen.
-   Ketidakrelevanan Rekomendasi
    
    -   Masalah: Rekomendasi generik tidak sesuai dengan kebutuhan spesifik pengguna.
    -   Solusi: Model ini memanfaatkan pendekatan content-based filtering untuk memberikan rekomendasi berdasarkan spesifikasi ponsel yang mirip dengan preferensi pengguna.
    -   Dampak: Rekomendasi lebih relevan dan personalisasi, sehingga meningkatkan peluang konsumen menemukan produk yang sesuai.
-   Keterbatasan Waktu
    
    -   Masalah: Konsumen tidak memiliki waktu untuk membandingkan semua opsi.
    -   Solusi: Dengan menyajikan rekomendasi secara otomatis, model menghemat waktu konsumen yang seharusnya digunakan untuk melakukan riset manual.
    -   Dampak: Proses pengambilan keputusan menjadi lebih cepat dan efisien.

Evaluasi Terhadap Goals

1.  Mampu menganalisis spesifikasi ponsel dan preferensi pengguna
    
    -   Pencapaian: Model berhasil memproses data spesifikasi ponsel untuk memberikan rekomendasi yang relevan. Rata-rata error yang rendah menunjukkan kemampuan model dalam memahami pola preferensi pengguna.
    -   Dampak: Model ini memungkinkan bisnis untuk memberikan pengalaman yang lebih personal kepada konsumen, yang dapat meningkatkan kepuasan dan loyalitas.
2.  Menyediakan rekomendasi informatif dan personalisasi
    
    -   Pencapaian: Rekomendasi yang dihasilkan berdasarkan jarak Euclidean antara fitur-fitur yang dinormalisasi memastikan bahwa hasil yang diberikan bersifat personal.
    -   Dampak: Konsumen mendapatkan rekomendasi yang sesuai dengan kebutuhan, yang meningkatkan peluang konversi menjadi pembelian.
   
##### Evaluasi model Auto Encoder 
```
reconstructed_features = autoencoder.predict(scaled_features)
mse = np.mean(np.square(scaled_features - reconstructed_features), axis=1)
average_mse = np.mean(mse)
```
Kode ini melakukan rekonstruksi data menggunakan autoencoder dan menghitung Mean Squared Error (MSE) untuk menilai kualitas rekonstruksi.

Rekonstruksi Data:

reconstructed_features = autoencoder.predict(scaled_features) melakukan prediksi terhadap data yang telah diubah (scaled_features) menggunakan model autoencoder. Ini menghasilkan data yang telah direkonstruksi oleh autoencoder.
Hitung MSE per Data:

mse = np.mean(np.square(scaled_features - reconstructed_features), axis=1) menghitung MSE untuk setiap contoh data, dengan membandingkan antara data asli (scaled_features) dan data yang telah direkonstruksi (reconstructed_features).
Hitung Rata-rata MSE:

average_mse = np.mean(mse) menghitung rata-rata MSE dari seluruh data untuk mendapatkan nilai kesalahan keseluruhan dari proses rekonstruksi.

Output:
Rata-rata MSE: 0.0025

Nilai Rata-rata MSE = 0.0025 menunjukkan bahwa model autoencoder berhasil melakukan rekonstruksi data dengan cukup baik.

##### Kesimpulan 
Evaluasi Terhadap Problem Statements

1.  Overload Informasi
    
    -   Masalah: Banyaknya informasi spesifikasi ponsel membuat konsumen kesulitan memilih produk.
    -   Solusi: Autoencoder berhasil merekonstruksi data dengan rata-rata MSE sebesar 0.0025, menunjukkan bahwa model mampu memahami pola dalam data spesifikasi ponsel. Hal ini memungkinkan penyaringan informasi yang lebih relevan untuk rekomendasi.
    -   Dampak: Mengurangi jumlah informasi yang harus diproses konsumen, sehingga membantu mereka fokus pada produk yang relevan.
2.  Kompleksitas Spesifikasi
    
    -   Masalah: Beragamnya spesifikasi teknis sering kali membingungkan konsumen.
    -   Solusi: Autoencoder menangkap representasi tersembunyi (latent representation) dari data, menyederhanakan kompleksitas spesifikasi teknis menjadi fitur yang lebih mudah diproses.
    -   Dampak: Rekomendasi yang dihasilkan menjadi lebih informatif dan membantu konsumen memahami perbedaan antarproduk tanpa perlu membedah spesifikasi secara mendetail.
3.  Ketidakrelevanan Rekomendasi
    
    -   Masalah: Rekomendasi generik sering kali tidak sesuai dengan kebutuhan pengguna.
    -   Solusi: Model autoencoder mendeteksi pola-pola spesifik dalam data dan menghasilkan rekomendasi berdasarkan rekonstruksi yang akurat. Nilai MSE yang rendah menunjukkan bahwa model mampu memberikan rekomendasi yang relevan.
    -   Dampak: Rekomendasi lebih sesuai dengan preferensi individu pengguna, sehingga meningkatkan kemungkinan konsumen menemukan produk yang cocok.
4.  Keterbatasan Waktu
    
    -   Masalah: Konsumen tidak memiliki waktu untuk membandingkan semua produk.
    -   Solusi: Autoencoder mempercepat proses analisis data dengan mereduksi dimensi dan memberikan rekomendasi langsung berdasarkan pola yang teridentifikasi.
    -   Dampak: Konsumen dapat membuat keputusan pembelian dengan lebih cepat dan efisien.

Evaluasi Terhadap Goals

1.  Mampu menganalisis spesifikasi ponsel dan preferensi pengguna
    
    -   Pencapaian: Model autoencoder menunjukkan performa yang baik dengan rata-rata MSE sebesar 0.0025, yang mencerminkan kemampuan model dalam memahami dan merekonstruksi pola dalam data spesifikasi ponsel.
    -   Dampak: Analisis data yang lebih baik memungkinkan rekomendasi produk yang lebih relevan bagi pengguna.
2.  Menyediakan rekomendasi informatif dan personalisasi
    
    -   Pencapaian: Dengan menggunakan representasi tersembunyi, autoencoder menghasilkan rekomendasi yang akurat dan personal, mengatasi tantangan spesifikasi teknis yang kompleks.
    -   Dampak: Konsumen mendapatkan informasi yang lebih relevan dan mudah dipahami, meningkatkan pengalaman belanja mereka.

