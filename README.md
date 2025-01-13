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

Untuk mencapai tujuan yang telah ditetapkan, sistem rekomendasi akan dirancang menggunakan dua pendekatan utama, yaitu Content-Based Filtering dan Collaborative Filtering. Berikut adalah uraian dari masing-masing pendekatan:

1. Content-Based Filtering
Content-Based Filtering adalah metode yang merekomendasikan item berdasarkan kesamaan antara spesifikasi ponsel dalam dataset dengan preferensi pengguna. Pendekatan ini memanfaatkan atribut atau fitur ponsel (seperti , RAM, prosesor, baterai, dan sistem operasi) untuk menemukan item yang relevan.

Cara Kerja:

- Sistem akan menganalisis data spesifikasi ponsel untuk mengidentifikasi fitur-fitur utama.
- Setiap ponsel dalam dataset akan direpresentasikan sebagai vektor fitur.
- Ketika pengguna memberikan preferensi, seperti ram dan baterau, sistem akan menghitung kesamaan (misalnya menggunakan Cosine Similarity atau Eclidean Distance) antara ponsel-ponsel dalam dataset dan preferensi pengguna.
- Ponsel dengan kesamaan tertinggi akan direkomendasikan.

2. Collaborative Filtering adalah metode yang merekomendasikan ponsel berdasarkan pola interaksi atau preferensi dari pengguna lain yang memiliki kesamaan perilaku. Pendekatan ini terbagi menjadi dua jenis utama: User-Based Collaborative Filtering dan Item-Based Collaborative Filtering.

Cara Kerja:

- User-Based Collaborative Filtering: Sistem menganalisis pola pembelian atau penilaian dari pengguna lain yang memiliki preferensi serupa untuk merekomendasikan ponsel.
- Item-Based Collaborative Filtering: Sistem mengidentifikasi ponsel yang sering dipilih atau dinilai secara positif bersama dengan ponsel lain yang diminati pengguna.
- Teknik seperti matriks dekomposisi atau algoritma k-nearest neighbors (k-NN) digunakan untuk menemukan pola ini.

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


| **Kolom**   | **Jumlah Data** |
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
![image](https://github.com/garr007/ProjectRecommenderSystem/blob/main/grafik%201.png?raw=true)

Rating paling sering berada di rentang **80-85**, menunjukkan bahwa mayoritas produk memiliki penilaian positif. Ini menggambarkan bahwa produk dalam dataset cenderung memiliki kualitas yang baik, dengan sebagian besar memperoleh rating tinggi dari pengguna.

Rating secara umum cenderung meningkat dari 60 hingga mencapai puncaknya di sekitar 80-85 sebelum kembali menurun.

#### 10 Produk Dengan Rating Tertinggi
![image](https://github.com/garr007/ProjectRecommenderSystem/blob/dd6d77ac5d0d734ca1db654cc7c51f9e3cadf916/grafik%203.png)

Produk dengan rating tertinggi adalah OnePlus 11 5G, diikuti oleh Xiaomi 12T Pro 5G dan Infinix Zero Ultra.

Semua produk dalam grafik memiliki rating yang sangat baik, mendekati atau sama.

#### Distribusi Brand Produk 
![image](https://github.com/garr007/ProjectRecommenderSystem/blob/dd6d77ac5d0d734ca1db654cc7c51f9e3cadf916/grafik%204.png)

Xiaomi dan Samsung adalah dua brand dengan jumlah produk terbanyak, masing-masing melebihi 100 produk.Brand seperti Vivo, Realme, dan Oppo juga memiliki kontribusi besar terhadap total produk.

#### Distribusi Harga Produk 
![image](https://github.com/garr007/ProjectRecommenderSystem/blob/dd6d77ac5d0d734ca1db654cc7c51f9e3cadf916/grafik%205.png)

Sebagian besar produk memiliki harga rendah, terbukti dari puncak yang tinggi di kisaran harga rendah (di bawah ₹100.000). 

Grafik ini mengindikasikan bahwa sebagian besar produk berada di kategori harga terjangkau, dengan hanya sedikit produk di kategori harga premium.

#### Perbandingan 5 Produk Termahal dan Termurah
![image](https://github.com/garr007/ProjectRecommenderSystem/blob/dd6d77ac5d0d734ca1db654cc7c51f9e3cadf916/grafik%206.png)

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
###### Checking Missing Values
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
**Jumlah baris dan kolom:** `(868, 16)`

**Jumlah baris:** `868`

**Jumlah data di setiap kolom:**

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


## Modeling 
Content-based Filtering: Pendekatan ini mengandalkan informasi terkait atribut produk untuk memberikan rekomendasi. Dalam hal ini, digunakan dua ukuran jarak yaitu Cosine Similarity dan Euclidean Distance untuk menghitung kesamaan antara produk-produk berdasarkan fitur yang relevan.

Collaborative Filtering: Pendekatan ini memanfaatkan data interaksi pengguna untuk memberikan rekomendasi. Dua teknik utama yang digunakan adalah:

K-Nearest Neighbors (KNN): Algoritma ini digunakan untuk mencari pengguna atau produk yang serupa berdasarkan preferensi yang ada.
Deep Learning Auto Encoder: Model ini digunakan untuk melakukan pemodelan data dalam bentuk yang lebih terkompresi dan menangkap pola hubungan yang lebih kompleks antar pengguna dan produk.

### Content Based Filtering 
### Cosine Similarity 
Cosine similarity mengukur **sudut** antara dua vektor dalam ruang multidimensi. Semakin kecil sudut antara dua vektor, semakin mirip kedua vektor tersebut. Jika dua vektor memiliki arah yang sama, maka cosine similarity mereka akan mendekati **1**, sedangkan jika arah mereka berlawanan, nilai cosine similarity-nya akan mendekati **-1**. Jika kedua vektor tegak lurus (tidak ada kesamaan), nilai cosine similarity-nya adalah **0**.

Secara matematis, cosine similarity antara dua vektor **A** dan **B** dihitung dengan rumus berikut:

Cosine Similarity = (A ⋅ B) / (||A|| ||B||)

Dimana:
- **A** dan **B** adalah dua vektor yang ingin dihitung kesamaannya.
- **A ⋅ B** adalah hasil perkalian titik (dot product) antara vektor A dan vektor B, yang dihitung dengan menjumlahkan hasil perkalian elemen yang sesuai dari kedua vektor.
  
A ⋅ B = Σ (A_i × B_i)

- **||A||** dan **||B||** adalah panjang (norma) dari masing-masing vektor, yang dihitung menggunakan rumus Euclidean distance:

||A|| = √(Σ A_i²)

||B|| = √(Σ B_i²)

#### Konsep Perhitungan
1. **Perkalian Titik (Dot Product)**: Menghitung total kontribusi antara elemen-elemen yang sesuai dalam kedua vektor. Semakin besar hasil perkalian titik, semakin tinggi kesamaan antara kedua vektor.

2. **Normalisasi Vektor**: Vektor-divisor digunakan untuk menghilangkan efek panjang vektor dan hanya mempertimbangkan arah vektor. Ini berarti bahwa dua vektor dengan panjang yang berbeda tetap bisa memiliki cosine similarity yang tinggi jika arahnya mirip.

3. **Hasil**: Nilai hasil dari cosine similarity akan berada dalam rentang antara -1 hingga 1:
   - **1**: Vektor memiliki arah yang sama (mereka identik dalam hal fitur).
   - **0**: Vektor tegak lurus (tidak ada kesamaan).
   - **-1**: Vektor memiliki arah yang berlawanan.

**Kelebihan:**

1. **Mengabaikan Skala**: Tidak terpengaruh oleh perbedaan ukuran antara data.
2. **Efisien dan Sederhana**: Mudah dihitung dan cepat diterapkan.
3. **Cocok untuk Data Sparse**: Efektif untuk data dengan banyak nol, seperti dalam teks atau rekomendasi.
4. **Tidak Terpengaruh oleh Magnitudo**: Fokus pada arah, bukan ukuran data.

**Kekurangan:**

1. **Tidak Memperhitungkan Magnitudo**: Hanya melihat arah, tidak panjang data.
2. **Sensitif terhadap Fitur Tidak Relevan**: Fitur berisik dapat mempengaruhi hasil.
3. **Tidak Cocok untuk Data Non-Linear**: Kurang efektif untuk data dengan hubungan yang kompleks.
4. **Tidak Menghitung Urutan Data**: Tidak memperhitungkan urutan elemen dalam data.
##### Cosine Similarity berdasarkan 'os' dan 'brand'
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

##### Cosine Similarity berdasarkan data numeric berdasarkan ram size, storage size, dan battery capacity
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
### Eudlidean Distance 
Euclidean Distance adalah ukuran yang digunakan untuk menghitung jarak antara dua titik dalam ruang multidimensi. Dalam konteks sistem rekomendasi produk, Euclidean Distance digunakan untuk mengukur kedekatan antara dua produk berdasarkan fitur-fitur yang dimilikinya (seperti ukuran RAM, kapasitas penyimpanan, dan daya baterai).

#### Cara Kerja Euclidean Distance

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
```
recommended_products = recommend_products_os_brand_euclidean('P7')
```
Produk yang Diminta

| **product_id** | **model**               | **os**        | **brand**    |
|----------------|-------------------------|---------------|--------------|
| P7             | Apple iPhone 14         | iOS v16       | Apple        |

10 Rekomendasi Produk Teratas Berdasarkan Euclidean Distance

| **product_id** | **os**        | **brand**   | **euclidean_distance** |
|----------------|---------------|-------------|------------------------|
| P28            | iOS v16       | Apple       | 0.000000               |
| P57            | iOS v16       | Apple       | 0.000000               |
| P101           | iOS v16       | Apple       | 0.000000               |
| P211           | iOS v16       | Apple       | 0.000000               |
| P248           | iOS v16       | Apple       | 0.000000               |
| P291           | iOS v16       | Apple       | 0.000000               |
| P324           | iOS v16       | Apple       | 0.000000               |
| P421           | iOS v16       | Apple       | 0.000000               |
| P637           | iOS v16       | Apple       | 0.000000               |
| P765           | iOS v16       | Apple       | 0.000000               |

##### Euclidean Distance berdasarkan data numeric berdasarkan ram size, storage size, dan battery capacity
Produk yang Diminta

| **product_id** | **ram_size** | **storage_size** | **battery_capacity** |
|----------------|--------------|------------------|----------------------|
| P14            | 6.0          | 128.0            | 5000.0               |

10 Rekomendasi Produk Teratas Berdasarkan Euclidean Distance

| **product_id** | **ram_size** | **storage_size** | **battery_capacity** | **distance** |
|----------------|--------------|------------------|----------------------|--------------|
| P834           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P290           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P151           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P655           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P139           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P138           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P135           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P315           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P634           | 6.0          | 128.0            | 5000.0               | 0.0          |
| P129           | 6.0          | 128.0            | 5000.0               | 0.0  

### Collaborative Filtering 
### Dengan KKN 
KNN digunakan untuk mencari "tetangga terdekat", yaitu pengguna atau item yang memiliki pola interaksi atau preferensi yang serupa. Berikut adalah langkah-langkah dasar dalam Collaborative Filtering menggunakan KNN:
1. **Matriks Rating**:
   - Data input berupa matriks rating yang berisi informasi rating atau interaksi yang diberikan pengguna terhadap item (misalnya, film, produk).
   
2. **Mencari Kemiripan (Similarity)**:
   - Menggunakan algoritma KNN untuk menghitung kemiripan antara pengguna atau item berdasarkan rating atau preferensi mereka.
   - Ukuran kemiripan umum yang digunakan adalah **Cosine Similarity** atau **Euclidean Distance**.
   
3. **Menentukan K (Jumlah Tetangga)**:
   - KNN membutuhkan parameter `K` untuk menentukan jumlah tetangga terdekat yang akan dipertimbangkan untuk rekomendasi. Misalnya, jika `K=5`, maka lima pengguna atau item terdekat akan digunakan untuk menghasilkan rekomendasi.

4. **Membuat Rekomendasi**:
   - Berdasarkan kemiripan yang dihitung, produk yang disukai oleh tetangga terdekat akan direkomendasikan kepada pengguna target.

**Kelebihan:**

1. **Mudah Dipahami dan Implementasi**: Algoritma sederhana dan dapat diimplementasikan dengan mudah.
2. **Tidak Memerlukan Model Global**: Tidak ada pelatihan model yang rumit, hanya berdasarkan data yang ada.
3. **Cocok untuk Data yang Tidak Terstruktur**: Dapat digunakan dengan data yang tidak memerlukan bentuk tertentu atau preprocessing yang kompleks.

**Kekurangan:**

1. **Komputasi Berat**: Menghitung jarak untuk setiap prediksi membutuhkan banyak sumber daya, terutama untuk dataset besar.
2. **Kurang Efektif dengan Data Spars**: KNN kurang efektif ketika data memiliki banyak nilai yang hilang atau sparse.
3. **Memerlukan Banyak Memori**: Harus menyimpan seluruh dataset untuk melakukan prediksi, yang bisa menjadi tidak efisien pada skala besar.
```
knn_model = NearestNeighbors(metric='euclidean', algorithm='brute')
knn_model.fit(scaled_features)
```
Melatih model menggunakan data scaled_features, yang merupakan data fitur yang sudah dinormalisasi atau diskalakan.
```
recommendations = recommend_products('P14', num_recommendations=5)
```

Informasi Produk yang Dimasukkan:
| product_id | model                             | price | rating |
|------------|-----------------------------------|-------|--------|
| P14        | Vivo T1 5G (6GB RAM + 128GB)      | 16990 | 80.0   |

Rekomendasi untuk Produk P14:
| product_id | model                                    | price | rating | distance  |
|------------|------------------------------------------|-------|--------|-----------|
| P543       | OPPO K10 (8GB RAM + 128GB)              | 16990 | 80.0   | 0.000000  |
| P6         | Samsung Galaxy F23 5G (6GB RAM + 128GB) | 16999 | 80.0   | 0.000248  |
| P315       | Motorola Moto G71 5G                    | 16999 | 80.0   | 0.000248  |
| P320       | Honor X9 5G                             | 16999 | 80.0   | 0.000248  |
| P696       | Infinix Note 13 Pro                     | 16999 | 80.0   | 0.000248  |

### Dengan Auto Encoder 
Autoencoder adalah jenis jaringan saraf yang digunakan untuk mempelajari representasi terkompresi dari data. Dalam konteks sistem rekomendasi, Autoencoder dapat digunakan untuk melakukan **Collaborative Filtering** dengan mempelajari representasi tersembunyi (latent representation) dari data pengguna dan item. Autoencoder bekerja dengan cara memampatkan informasi input menjadi bentuk yang lebih kecil dan kemudian mencoba merekonstruksi input tersebut seakurat mungkin.

Langkah-langkah dalam Collaborative Filtering dengan Autoencoder:

1. **Preprocessing Data**:
   - Membuat matriks pengguna-item dengan rating atau interaksi pengguna terhadap item tertentu. Jika data kosong (belum ada rating), autoencoder akan mencoba memprediksi rating tersebut.
   
2. **Pelatihan Autoencoder**:
   - Autoencoder dilatih untuk mempelajari representasi tersembunyi dari data tersebut. Selama pelatihan, model berusaha untuk meminimalkan error antara rating yang diprediksi dan rating asli yang ada.

3. **Rekonstruksi dan Rekomendasi**:
   - Setelah pelatihan selesai, model autoencoder dapat digunakan untuk menghasilkan rekomendasi dengan memprediksi rating untuk item yang belum diberikan rating oleh pengguna. Produk atau item yang memiliki rating prediksi tertinggi akan direkomendasikan.
 
**Kelebihan:**

1. **Pengurangan Dimensi**:
   - Autoencoder mengurangi dimensi data, yang memungkinkan pemrosesan data yang lebih efisien dan mengurangi masalah sparsity pada matriks pengguna-item.

2. **Menangani Data yang Tidak Terlalu Terkurasi**:
   - Autoencoder dapat menangani matriks yang lebih jarang (sparse matrix), sehingga memungkinkan pemahaman yang lebih baik tentang hubungan tersembunyi antara pengguna dan item.

3. **Kemampuan Generalisasi yang Lebih Baik**:
   - Dengan model yang lebih sederhana, Autoencoder dapat menangani pola preferensi yang lebih kompleks, dan lebih baik dalam memberikan rekomendasi kepada pengguna baru atau item baru (masalah cold-start).

**Kekurangan:**

1. **Kompleksitas Model**:
   - Proses pelatihan Autoencoder membutuhkan lebih banyak waktu dan sumber daya komputasi dibandingkan dengan metode collaborative filtering tradisional.

2. **Tantangan dalam Pengaturan Hyperparameter**:
   - Menentukan jumlah neuron yang tepat di layer tersembunyi atau memilih arsitektur yang tepat dapat menjadi tantangan dalam pelatihan Autoencoder.

3. **Cold Start Problem**:
   - Masalah ini tetap ada pada pengguna baru atau item baru, meskipun model Autoencoder lebih mampu menangani masalah ini dibandingkan metode berbasis KNN tradisional.

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

Input Layer: Input(shape=(scaled_features.shape[1],)) – Lapisan input menerima data dengan jumlah fitur yang sesuai dengan jumlah kolom dalam scaled_features.

Encoder: Tiga lapisan Dense (fully connected) yang mengurangi dimensi fitur secara bertahap dari 64 ke 32 dan kemudian ke 16, menggunakan fungsi aktivasi ReLU.

Decoder: Tiga lapisan Dense yang membangun kembali dimensi fitur, dimulai dari 32 ke 64 dan akhirnya ke ukuran fitur asli menggunakan fungsi aktivasi ReLU dan linear.

```
autoencoder.fit(scaled_features, scaled_features, epochs=50, batch_size=32, shuffle=True)
```
Perintah ini melatih model autoencoder menggunakan data yang telah diskalakan
```
recommendations = recommend_products_deep_learning('P8', num_recommendations=5)
```
Informasi Produk yang Dimasukkan:
| product_id | model                              | price | rating |
|------------|------------------------------------|-------|--------|
| P8         | Xiaomi Redmi Note 12 Pro Plus     | 29999 | 86.0   |

Rekomendasi Produk Teratas:
| product_id | model                             | price | rating | similarity |
|------------|-----------------------------------|-------|--------|------------|
| P8         | Xiaomi Redmi Note 12 Pro Plus    | 29999 | 86.0   | 1.000000   |
| P360       | Poco F4 (12GB RAM + 256GB)       | 29999 | 86.0   | 1.000000   |
| P747       | Xiaomi Mi 10T Pro 5G             | 29999 | 86.0   | 1.000000   |
| P154       | Oppo A98                          | 30990 | 87.0   | 0.999910   |
| P37        | Oppo Reno 8T                      | 29990 | 87.0   | 0.999889   |

### Evaluasi 
#### Metrik Evaluasi: Mean Squared Error (MSE)

**MSE (Mean Squared Error)** digunakan untuk mengukur perbedaan antara nilai yang diprediksi oleh model dengan nilai yang sebenarnya. Dalam konteks ini, MSE digunakan untuk mengukur kesalahan prediksi berdasarkan jarak antara produk uji dan rata-rata produk tetangga terdekat.

MSE = (1 / n) * Σ (y_i - ŷ_i)²

Di mana:

y_i adalah nilai sebenarnya (data observasi),

ŷ_i adalah nilai prediksi (nilai yang diprediksi oleh model),
n adalah jumlah data atau sampel.

MSE mengukur rata-rata kuadrat perbedaan antara nilai prediksi dan nilai sebenarnya, semakin kecil nilai MSE, semakin baik prediksi model.

##### Evaluasi model KKN Menggunakan manual cross-validation
```
average_error = manual_cross_val(knn_model, scaled_features, n_splits=3)
```
Menghasilkan 
Average error from manual cross-validation: **0.14964355364582532**

Nilai ini menunjukkan bahwa rata-rata perbedaan (error) antara produk uji dan prediksi berdasarkan jarak tetangga terdekat adalah sekitar 0.15.

Nilai 0.15 merupakan kesalahan yang relatif kecil dalam konteks data, maka model ini dapat dianggap cukup baik.

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
