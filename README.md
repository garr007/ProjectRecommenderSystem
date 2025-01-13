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

### Exploratory Data Analysis 
![image](https://github.com/garr007/ProjectRecommenderSystem/blob/main/grafik%201.png?raw=true)


### Checking Missing Values,Duplicate Data dan Outlier
##### Checking Missing Values
Skrip Python cek nilai null
```
pd.DataFrame({'Missing Value':df_cleaned.isnull().sum()})
```

| No. | Nama Fitur               | Missing Value |
|-----|--------------------------|---------------|
| 1   | Hours_Studied            | 0             |
| 2   | Attendance               | 0             |
| 3   | Parental_Involvement     | 0             |
| 4   | Access_to_Resources      | 0             |
| 5   | Extracurricular_Activities | 0           |
| 6   | Sleep_Hours              | 0             |
| 7   | Previous_Scores          | 0             |
| 8   | Motivation_Level         | 0             |
| 9   | Internet_Access          | 0             |
| 10  | Tutoring_Sessions        | 0             |
| 11  | Family_Income            | 0             |
| 12  | Teacher_Quality          | 78            |
| 13  | School_Type              | 0             |
| 14  | Peer_Influence           | 0             |
| 15  | Physical_Activity        | 0             |
| 16  | Learning_Disabilities    | 0             |
| 17  | Parental_Education_Level | 90            |
| 18  | Distance_from_Home       | 67            |
| 19  | Gender                   | 0             |
| 20  | Exam_Score               | 0             |

Berikut adalah fitur-fitur yang memiliki nilai _null_:
- **Teacher_Quality**: 78
- **Parental_Education_Level**: 90
- **Distance_from_home**: 67

Total nilai _null_ pada dataset adalah 78 + 90 + 67 = **235**

Dengan dimensi dataset 6,607 baris dan 20 kolom menjadikan total data pada dataset adalah 6,607 * 20 = **132,140**

Dengan demikian, persentase jumlah nilai _null_ pada dataset adalah 235/132,140 * 100 = **0.18%**, di mana persentase tersebut sangat kecil sehingga untuk _handling_ nilai _null_ pada dataset, baris yang memuat nilai-nilai _null_ tersebut cukup dihapuskan karena tidak akan mempengaruhi informasi yang dimuat oleh keseluruhan data.

##### Checking Duplicate Data
Skrip Python cek nilai duplikat
```
df_cleaned.duplicated().sum()
```

0

Tidak terdapat nilai duplikat dalam dataset yang digunakan.

### Outlier Detection

![image](https://github.com/user-attachments/assets/33c547e1-3af9-4f4e-969b-66780eead2dd)

Berikut adalah interpretasi dari boxplot yang ditampilkan di atas:

- Pada kolom Hours_Studied, terlihat beberapa outlier di sisi kiri (sekitar 0-5 jam) dan di sisi kanan (sekitar 35-45 jam). Meski demikian, 0-5 jam per minggu Ini mungkin terjadi, terutama jika seorang siswa tidak terlalu fokus pada studi, memiliki komitmen lain. 35-45 jam per minggu juga mungkin, terutama untuk siswa yang sangat berdedikasi. Outlier ini tidak akan dihapus karena memberikan gambaran lengkap tentang bagaimana siswa berbeda dalam waktu belajar.

- Pada kolom Tutoring_Sessions, dapat dilihat bahwa nilai 4 hingga 8 sesi per bulan, dianggap sebagai outliers secara statistik. Namun nilai-nilai ini sangat memungkinkan karena ada siswa yang mungkin merasa perlu belajar lebih banyak sehingga outlier tidak akan dihapus.

- Pada kolom Exam_Score, dapat dilihat bahwa mayoritas exam_score di rentang 65-70. Terdapat beberapa outlier, yaitu exam_score 75 ke atas. Namun terdapat outlier yaitu Exam_Score yang bernilai 101 yang mana tidak mungkin pada konteks ujian. Outlier lainnya akan dipertahankan karena sangat memungkinkan jika siswa mendapatkan nilai 75 keatas dan tidak melebihi 100.

- Pada kolom-kolom lainnya, dapat dilihat bahwa persebaran data merata dan tidak terdapat outlier yang signifikan. Secara keseluruhan, data ini siap untuk diproses dan dianalisis lebih mendalam tanpa perlu melakukan penghapusan outlier.

### Mengecek Exam_Score yang nilainya lebih dari 100 
```
df_cleaned[df_cleaned["Exam_Score"] > 100]
```
Karena maksimal nilai untuk sebuah ujian adalah 100, hasilnya 
| Hours Studied | Attendance | Parental Involvement | Access to Resources | Extracurricular Activities | Sleep Hours | Previous Scores | Motivation Level | Internet Access | Tutoring Sessions | Family Income | Teacher Quality | School Type | Peer Influence | Physical Activity | Learning Disabilities | Parental Education Level | Distance from Home | Gender  | Exam Score |
|---------------|------------|----------------------|----------------------|----------------------------|-------------|-----------------|------------------|-----------------|-------------------|---------------|----------------|-------------|----------------|----------------|---------------------|------------------------|------------------|---------|------------|
| 1525          | 27         | 98                  | Low                  | Medium                     | Yes         | 6               | 93               | Low             | No                | 5             | High           | High        | Public         | Positive       | 3                  | No                     | High School        | Moderate | Female  | 101        |
Terdapat 1 baris data yang perlu dihapus.
### Exploratory Data Analysis (EDA)

**Univariate Analysis**

Berikut adalah analisis jumlah nilai dari masing-masing fitur kategorikal:

![image](https://github.com/user-attachments/assets/92f50b2e-ef9f-4bd0-ba25-3b5651ea1909)

Secara umum, plot-plot pada gambar diatas dapat diinterpretasikan sebagai berikut:

- **Parental_Involvement**: Sebagian besar siswa memiliki keterlibatan orang tua di level medium.
- **Access_to_Resources**: Sebagian besar siswa memiliki akses ke sumber daya pada level medium.
- **Extracurricular_Activities**: Sebagian besar siswa terlibat dalam aktivitas ekstrakurikuler.
- **Motivation_Level**: Sebagian besar siswa memiliki tingkat motivasi pada level medium.
- **Internet_Access**: Sebagian besar siswa memiliki akses internet.
- **Family_Income**: Sebaran data pendapatan keluarga siswa cukup merata antara level medium dan low.
- **Teacher_Quality**: Sebagian besar siswa memiliki kualitas guru di level medium.
- **School_Type**: Sebagian besar siswa berasal dari sekolah negeri (public).
- **Peer_Influence**: Sebaran data pengaruh teman sebaya cukup merata di level neutral dan positive.
- **Learning_Disabilites**: Sebagian besar siswa tidak memiliki disabilitas belajar.
- **Parental_Education_Level**: Sebagian besar siswa memiliki orang tua dengan tingkat pendidikan setara sekolah menengah atas.
- **Distance_from_Home**: Sebagian besar siswa memiliki jarak tempat tinggal yang dekat dari sekolah.
- **Gender**: Sebagian besar siswa adalah laki-laki.

Berikut adalah analisis distribusi nilai dari masing-masing fitur numerikal:

![image](https://github.com/user-attachments/assets/25bc4205-44df-4a88-9cf2-fc8d191b2110)

Berdasarkan hasil plot histogram yang disajikan, dapat diinterpretasikan sebagai berikut:

- **Hours_Studied**: Distribusi data membentuk kurva normal dengan puncak di sekitar 20-25 jam. Mayoritas mahasiswa belajar sekitar 20-30 jam. Terdapat beberapa mahasiswa dengan jam belajar yang lebih ekstrim, baik sangat sedikit maupun sangat banyak.
- **Attendance**: Distribusi data menunjukkan pola bimodal, dengan dua puncak di sekitar 70-80% dan 90-100%. Mayoritas mahasiswa memiliki kehadiran di atas 80%. Terdapat beberapa mahasiswa dengan kehadiran yang rendah.
- **Sleep_Hours**: Distribusi data menunjukkan pola normal dengan puncak di sekitar 6-8 jam tidur. Mayoritas mahasiswa tidur sekitar 6-8 jam per hari. Terdapat beberapa mahasiswa dengan jam tidur yang ekstrim, baik sedikit maupun banyak.
- **Previous_Scores**: Distribusi data cenderung simetris dengan puncak di sekitar 70-80. Mayoritas mahasiswa memiliki skor sebelumnya di rentang 70-80. Terdapat beberapa mahasiswa dengan skor yang sangat rendah maupun sangat tinggi.
- **Tutoring_Sessions**: Distribusi data menunjukkan pola bimodal dengan dua puncak di sekitar 1 dan 6 sesi. Mayoritas mahasiswa mengikuti 1-2 sesi tutorial atau 5-6 sesi tutorial. Terdapat beberapa mahasiswa dengan jumlah sesi tutorial yang sangat sedikit maupun sangat banyak.
- **Physical_Activity**: Distribusi data menunjukkan pola bimodal dengan dua puncak yang jelas. Mayoritas mahasiswa memiliki aktivitas fisik yang rendah atau sangat tinggi. Terdapat sedikit mahasiswa dengan aktivitas fisik yang moderat.
- **Exam_Score**: Distribusi data cenderung normal dengan puncak di sekitar 70-80. Mayoritas mahasiswa memperoleh skor ujian di rentang 70-80. Terdapat beberapa mahasiswa dengan skor ujian yang sangat rendah maupun sangat tinggi.

**Multivariate Analysis**

![image](https://github.com/user-attachments/assets/8db8b289-7e22-4aef-9799-eaabba62ea75)

| Feature                      | Category          | Average Exam Score |
|------------------------------|-------------------|---------------------|
| Parental Involvement         | High              | 68.112200          |
|                              | Low               | 66.351938          |
|                              | Medium            | 67.113196          |
| Access to Resources          | High              | 68.103158          |
|                              | Low               | 66.223705          |
|                              | Medium            | 67.145801          |
| Extracurricular Activities   | No                | 66.951770          |
|                              | Yes               | 67.446138          |
| Motivation Level             | High              | 67.743931          |
|                              | Low               | 66.746108          |
|                              | Medium            | 67.338894          |
| Internet Access              | No                | 66.483471          |
|                              | Yes               | 67.309520          |
| Family Income                | High              | 67.814483          |
|                              | Low               | 66.853215          |
|                              | Medium            | 67.371005          |
| Teacher Quality              | High              | 67.664391          |
|                              | Low               | 66.775889          |
|                              | Medium            | 67.118662          |
| School Type                  | Private           | 67.316358          |
|                              | Public            | 67.216332          |
| Peer Influence               | Negative          | 66.582707          |
|                              | Neutral           | 67.215631          |
|                              | Positive          | 67.623433          |
| Learning Disabilities        | No                | 67.358557          |
|                              | Yes               | 66.291916          |
| Parental Education Level     | College           | 67.358432          |
|                              | High School       | 66.884104          |
|                              | Postgraduate      | 67.972656          |
| Distance from Home           | Far               | 66.498428          |
|                              | Moderate          | 66.969072          |
|                              | Near              | 67.513812          |
| Gender                       | Female            | 67.262179          |
|                              | Male              | 67.235629          |

Hasil analisis di atas dapat diinterpretasikan sebagai berikut:

- Learning_Disabilities: Mahasiswa tanpa learning disabilities memiliki rata-rata skor ujian yang lebih tinggi (67.36) dibandingkan dengan yang memiliki learning disabilities (66.29).
- Parental_Involvement: Mahasiswa dengan keterlibatan orang tua yang tinggi memiliki rata-rata skor ujian yang lebih tinggi (68.11) dibandingkan dengan yang rendah (66.35) atau sedang (67.11).
- Access_to_Resources: Mahasiswa dengan akses sumber daya yang tinggi memiliki rata-rata skor ujian yang lebih tinggi (68.10) dibandingkan dengan yang rendah (66.22) atau sedang (67.15).
- Extracurricular_Activities: Mahasiswa yang terlibat dalam kegiatan ekstrakurikuler memiliki rata-rata skor ujian yang lebih tinggi (67.45) dibandingkan dengan yang tidak terlibat (66.95).
- Motivation_Level: Mahasiswa dengan motivasi tinggi memiliki rata-rata skor ujian yang lebih tinggi (67.74) dibandingkan dengan yang rendah (66.75) atau sedang (67.34). Variabel lainnya juga menunjukkan perbedaan rata-rata skor ujian, meskipun mungkin tidak terlalu signifikan.

![image](https://github.com/user-attachments/assets/144243cb-8d39-4856-bd28-fb433da19106)

Berdasarkan heatmap yang ditunjukkan, dapat disimpulkan bahwa:
*   Terdapat korelasi positif yang kuat antara variabel-variabel tertentu,
yaitu jam belajar (Hours_Studied) dengan skor ujian (Exam_Score), serta kehadiran (Attendance) dengan skor ujian.
*   Terdapat korelasi positif yang lemah antara variabel-variabel tertentu,
yaitu nilai sebelumnya (Previous_Score) dengan skor ujian (Exam_Score), serta banyak sesi les (Tutoring_Sessions) dengan skor ujian.

![image](https://github.com/user-attachments/assets/51dce7a4-18bc-4a0f-a8fc-56b5d5586dbd)

Berdasarkan plot scatter yang disajikan, dapat disimpulkan bahwa:
*   Terdapat korelasi positif yang kuat antara persentase kehadiran siswa dan nilai ujian. Semakin tinggi kehadiran, semakin tinggi pula nilai ujian yang diraih.
*   Terdapat korelasi positif yang kuat antara jam belajar per minggu siswa dan nilai ujian. Semakin banyak jam belajar, semakin tinggi pula nilai ujian yang diraih.
*   Terdapat korelasi positif lemah antara nilai siswa sebelumnya dan nilai ujian. Dapat diartikan nilai sebelumnya hanya sedikit mempengaruhi nilai ujian.
*   Terdapat korelasi positif yang cukup kuat antara sesi les yang diikuti siswa per bulan dan nilai ujian. Tren visualnya menunjukkan garis tren yang naik, artinya semakin banyak sesi les yang diikuti, nilai ujian cenderung juga semakin tinggi, namun penyebaran data terlihat lebih banyak di bagian kiri.

## Data Preparation
Berdasarkan pengecekan data yang dilakukan pada tahap data understanading, perlu dilakukan beberapa proses handling terhadap data.
### Data Cleaning
#### Null Value Handling
Untuk menghapus nilai _null_ menggunakan sintaks:

```
# Menghapus baris yang memiliki missing values
df_cleaned = data.dropna()
```

#### Outlier Handling pada Kolom Exam_Score
Berikut adalah sintaks kode Python untuk menghapus baris yang memiliki Exam_Score lebih dari 100:
```
df_cleaned.drop(df_cleaned[df_cleaned["Exam_Score"] > 100].index, inplace=True)
```
### Encoding
Encoding adalah proses mengubah nilai kategorikal dalam dataset menjadi nilai numerikal. Hal ini dicapai dengan membuat nilai-nilai unik dalam sebuah fitur menjadi fitur-fitur baru yang didalamnya (sebagai contoh) bernilai 1 untuk mewakili 'ya' dan 0 untuk mewakili 'tidak'. Terdapat 3 macam teknik encoding yang digunakan, yaitu Categorical Encoding, One Hot Encoding, dan Ordinal Encoding.

Berikut adalah penjelasan singkat mengenai tiga teknik encoding yang digunakan:

1. **Categorical Encoding**  
   Categorical encoding adalah teknik untuk mengubah kategori dalam data menjadi angka. Teknik ini sering digunakan untuk data dengan kategori biner, seperti 'ya' dan 'tidak' menjadi nilai numerik, seperti 1 dan 0.

2. **One Hot Encoding**  
   One Hot Encoding adalah teknik yang mengubah setiap nilai kategori menjadi fitur biner terpisah. Setiap kategori diwakili oleh kolom baru dengan nilai 0 atau 1. Misalnya, untuk kategori "Merah", "Hijau", dan "Biru", kita akan membuat tiga kolom terpisah, dengan satu kolom yang bernilai 1 untuk kategori yang ada, sementara yang lainnya bernilai 0.

3. **Ordinal Encoding**  
   Ordinal Encoding digunakan untuk data kategorikal yang memiliki urutan tertentu. Setiap kategori diberikan nilai numerik yang mencerminkan urutan atau ranking. Misalnya, untuk kategori "Rendah", "Sedang", dan "Tinggi", kita bisa memberikan nilai 1, 2, dan 3, yang menunjukkan urutan dari yang terendah ke yang tertinggi.

**Encoding Kategorikal dilakukan terhadap 3 variabel, yaitu :**
```
- Extracurricular_Activities : Apakah Siswa Berpartisipasi dalam kegiatan ekstrakurikuler
- Internet_Access : Apakah Siswa Memiliki Akses ke Internet
- Learning_Disabilities : Apakah Siswa Memiliki Gangguan Pembelajaran
```
Karena masing-masing dari empat variabel tersebut hanya memiliki kategori ya (iya) dan tidak (tidak).

**One Hot Encoding diterapkan pada 2 variabel, yaitu :**
```
- School_Type : Jenis sekolah yang dihadiri siswa (Negeri, Swasta)
- Gender : Jenis kelamin siswa (Laki-laki, Perempuan)
```
Karena kategori Gender tidak memiliki urutan tertentu (nominal).

**Encoding Ordinal dilakukan terhadap 8 variabel, yaitu :**
```
- Parental_Involvement : Tingkat keterlibatan orang tua dalam pendidikan siswa (Rendah, Sedang, Tinggi)
- Access_to_Resources : Ketersediaan akses ke sumber daya pendidikan (Rendah, Sedang, Tinggi)
- Motivation_Level : Tingkat motivasi siswa (Rendah, Sedang, Tinggi)
- Family_Income : Tingkat pendapatan keluarga (Rendah, Sedang, Tinggi)
- Teacher_Quality : Kualitas pengajaran (Rendah, Sedang, Tinggi)
- Peer_Influence : Pengaruh teman sebaya terhadap kinerja akademik (Positif, Netral, Negatif)
- Parental_Education_Level : Tingkat pendidikan tertinggi orang tua (Sekolah Menengah, Perguruan Tinggi, Pascasarjana)
- Distance_from_Home : Jarak dari rumah ke sekolah (Dekat, Sedang, Jauh)
```
Karena ada urutan dan makna yang jelas, data diatas termasuk dalam kategori ordinal.

### Data Splitting
Split data dilakukan untuk membagi dataset menjadi bagian pelatihan dan pengujian. Ini penting untuk mengevaluasi kinerja model pada data yang tidak terlihat, mencegah overfitting, dan memastikan model dapat generalisasi dengan baik. Pembagian data menjadi data training dan data testing dilakukan dengan rasio sebagai berikut:

- Data training sebesar 80% untuk melatih model
- Data testing sebesar 20% untuk menguji model

## Modeling
Seluruh model yang akan dibuat tidak menggunakan hyperparameter tuning melainkan akan menggunakan beberapa algoritma dan memilih model terbaik sebagai solusi. Sesuai solusi yang ditawarkan pada bagian **_Solution Statement_**, beberapa algoritma yang akan digunakan untuk masalah regresi pada proyek ini adalah _Linear Regression_, _Decision Tree_, _Random Forest_, _Gradient Boosting_, dan _Support Vector regression_. Berikut adalah analisis kelebihan dan kekurangan dari masing-masing algoritma yang digunakan dalam proyek ini:

| **Model**               | **Kelebihan**                                                                                                                                       | **Kekurangan**                                                                                                  |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Linear Regression (LR)** | - Sederhana dan mudah dipahami. <br> - Cepat dalam pelatihan dan prediksi. <br> - Memiliki interpretasi yang jelas (koefisien menunjukkan pengaruh variabel). | - Hanya dapat menangkap hubungan linear. <br> - Sensitif terhadap outlier. <br> - Mengasumsikan hubungan linear. |
| **Decision Tree (DT)**    | - Mudah diinterpretasikan dan divisualisasikan. <br> - Mampu menangkap hubungan non-linear. <br> - Tidak memerlukan scaling data.                     | - Rentan terhadap overfitting, terutama dengan data yang kompleks. <br> - Sensitif terhadap perubahan kecil.    |
| **Random Forest (RF)**   | - Lebih robust dibandingkan Decision Tree, mengurangi risiko overfitting. <br> - Mampu menangkap interaksi yang kompleks antar fitur. <br> - Memberikan estimasi pentingnya fitur. | - Lebih lambat dalam pelatihan dan prediksi. <br> - Kurang interpretatif dibandingkan model linear. <br> - Memerlukan lebih banyak memori. |
| **Gradient Boosting (GB)**| - Mampu menangkap hubungan non-linear yang kompleks. <br> - Umumnya memberikan performa yang sangat baik dalam banyak kasus. <br> - Mampu mengatasi missing values. | - Rentan terhadap overfitting jika tidak dituning dengan baik. <br> - Lebih lambat dalam pelatihan. <br> - Memerlukan pemahaman yang lebih dalam tentang hyperparameter. |
| **Support Vector Regression (SVR)** | - Mampu menangkap hubungan non-linear dengan kernel yang tepat. <br> - Robust terhadap overfitting, terutama di dimensi tinggi. <br> - Efektif pada dataset kecil hingga menengah. | - Tidak efisien pada dataset yang sangat besar. <br> - Memerlukan pemilihan kernel yang tepat dan tuning hyperparameter. <br> - Sulit dalam interpretasi model. |

#### 1. Linear Regression (LR)

**Cara Kerja:**
- Linear Regression bertujuan untuk menemukan hubungan linier antara variabel independen (input) dan variabel dependen (output).
- Model mencoba meminimalkan *Mean Squared Error (MSE)*, yaitu perbedaan rata-rata kuadrat antara nilai prediksi dan nilai aktual.
- Persamaan yang dihasilkan adalah garis regresi dalam bentuk:
  y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
y: Variabel dependen (output/prediksi)
β: Koefisien regresi (kemiringan)
x: Variabel independen (fitur input)
ε: Error atau noise

---

#### 2. Decision Tree (DT)

**Cara Kerja:**
- Decision Tree bekerja dengan membagi dataset menjadi subset berdasarkan fitur tertentu.
- Setiap pemisahan (*split*) dibuat berdasarkan kriteria seperti:
  - *Gini Impurity*
  - *Information Gain*
- Proses ini diulang secara rekursif hingga mencapai daun (*leaf*), di mana setiap daun mewakili nilai prediksi.
- Struktur akhirnya adalah pohon dengan:
  - Keputusan di setiap simpul (*node*) internal
  - Prediksi di daun
- Persamaan yang digunakan adalah:
Prediction = Weighted_Average(Leaf_Values)
Leaf Values: Nilai target pada setiap daun (misal rata-rata target untuk regresi).
Weighted Average: Berdasarkan jumlah data di masing-masing cabang.
---

#### 3. Random Forest (RF)

**Cara Kerja:**
- Random Forest adalah kumpulan (*ensemble*) dari banyak Decision Tree yang bekerja secara bersamaan.
- Model membagi dataset menjadi subset secara acak dan melatih setiap Decision Tree pada subset yang berbeda.
- Untuk prediksi:
  - *Voting mayoritas* digunakan untuk klasifikasi.
  - Rata-rata prediksi digunakan untuk regresi.
- Metode *bagging* digunakan untuk mengurangi overfitting dengan mengkombinasikan hasil dari banyak model sederhana.
- Persamaan yang digunakan adalah:
Prediction = Mean(Tree₁_Output, Tree₂_Output, ..., Treeₖ_Output)
Treeₖ: Output dari setiap Decision Tree dalam hutan.
Mean: Digunakan untuk regresi (rata-rata hasil semua pohon).
Voting Majority: Untuk klasifikasi (mayoritas hasil pohon).

---

#### 4. Gradient Boosting (GB)

**Cara Kerja:**
- Gradient Boosting membangun model secara bertahap, dengan setiap model baru bertujuan untuk memperbaiki error dari model sebelumnya.
- Algoritma ini mengoptimalkan *loss function* (misalnya MSE untuk regresi) menggunakan metode *gradient descent*.
- Model baru dilatih pada *residuals* (selisih antara prediksi sebelumnya dan nilai aktual) dari model sebelumnya.
- Setelah beberapa iterasi, model akhir adalah kombinasi dari semua model individu, menghasilkan prediksi yang lebih baik.
- Persamaan yang digunakan adalah:
Fₘ(x) = Fₘ₋₁(x) + η * hₘ(x)
Fₘ(x): Model pada iterasi ke-m.
Fₘ₋₁(x): Model dari iterasi sebelumnya.
η: Learning rate (kecepatan pembelajaran).
hₘ(x): Weak learner pada iterasi ke-m (biasanya Decision Tree kecil).
---

#### 5. Support Vector Regression (SVR)

**Cara Kerja:**
- SVR adalah variasi dari Support Vector Machine (SVM) yang dirancang untuk regresi.
- Tujuan utama adalah menemukan hyperplane (dalam dimensi tinggi) yang memprediksi nilai output dengan margin error maksimum \( \epsilon \) dan meminimalkan error.
- Titik data yang berada di luar margin error dihukum dalam fungsi loss.
- Dengan kernel (misalnya *RBF* atau *Polynomial*), SVR dapat memodelkan hubungan non-linear antara input dan output.
- Persamaan yang digunakan adalah:
f(x) = Σ(αᵢ - α*ᵢ) K(xᵢ, x) + b
αᵢ, α*ᵢ: Koefisien Lagrange.
K(xᵢ, x): Kernel function (contohnya linear, polynomial, atau RBF).
b: Bias.
f(x): Prediksi untuk x.


---
Berikut adalah sintaks kode Python untuk instansiasi algoritma-algoritma yanng digunakan, pelatihan model, dan prediksi nilai oleh model:

**Linear Regression**
***Parameter:***
Default
```
# Membuat dan melatih model regresi linier
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Prediksi
predictions_lr = model_lr.predict(X_test)
```

**Decision Tree**
***Parameter:***
Parameter max_depth digunakan untuk menentukan kedalaman maksimum dari pohon keputusan yang akan dibangun. max_depth=10 berarti bahwa pohon keputusan tidak akan memiliki lebih dari 10 tingkat.
```
# Membuat dan melatih model decision tree
model_dt = DecisionTreeRegressor(max_depth=10)
model_dt.fit(X_train, y_train)

# Prediksi dan evaluasi
predictions_dt = model_dt.predict(X_test)
```

**Random Forest**
***Parameter:***
Parameter n_estimators digunakan untuk jumlah pohon keputusan (decision trees) yang akan dibangun dalam hutan acak (random forest). n_estimators=100 berarti 100 pohon keputusan akan dibangun.

Parameter random_state adalah nilai integer yang digunakan untuk mengatur seed generator angka acak. Dalam pelatihan model ini, random_state=30 berarti bahwa generator angka acak akan menggunakan seed 30. Ini membantu dalam membuat eksperimen yang konsisten dan dapat direproduksi.
```
# Membuat dan melatih model random forest
model_rf = RandomForestRegressor(n_estimators=100, random_state=30)
model_rf.fit(X_train, y_train)

# Prediksi
predictions_rf = model_rf.predict(X_test)
```

**Gradient Boosting**
***Parameter:***
Dalam pelatihan model ini, n_estimators=100 berarti 100 model akan dibangun.

Parameter learning rate digunakan untuk mengontrol seberapa besar kontribusi setiap model baru terhadap prediksi akhir. Learning_rate=0.1 menunjukkan bahwa setiap model berkontribusi 10% terhadap prediksi akhir. 

max_depth=3 berarti setiap pohon tidak akan memiliki lebih dari 3 tingkat. Ini membantu menjaga model agar tetap sederhana.
```
# Membuat dan melatih model gradient boosting
model_gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model_gb.fit(X_train, y_train)

# Prediksi dan evaluasi
predictions_gb = model_gb.predict(X_test)
```

**Support Vector Regression (SVR)**
***Parameter:***
Parameter ini menentukan jenis fungsi kernel yang digunakan untuk memetakan data ke ruang dimensi yang lebih tinggi. 

Pada perintah dibawah, kernel='rbf' menunjukkan bahwa kernel yang digunakan adalah RBF. Ini adalah pilihan umum dalam banyak aplikasi SVR karena fleksibilitasnya.
```
# Membuat dan melatih model support vector regression
model_svr = SVR(kernel='rbf')
model_svr.fit(X_train, y_train)

# Prediksi dan evaluasi
predictions_svr = model_svr.predict(X_test)
```



## Evaluation
### Metrik Evaluasi
Berikut adalah metrik evaluasi yang digunakan:

1. **Mean Squared Error (MSE)**  
   Formula:
   
   MSE = $\frac{1}{n} \sum_{i=1}^{n} (y_{\text{true},i} - y_{\text{pred},i})^2$
   
   Dimana:  
   - $\( y_{\text{true},i} \)$ adalah nilai sebenarnya untuk data ke-\(i\).  
   - $\( y_{\text{pred},i} \)$ adalah nilai prediksi untuk data ke-\(i\).  
   - $\( n \)$ adalah jumlah data.  

3. **Mean Absolute Error (MAE)**  
   Formula:
   
   MAE = $\frac{1}{n} \sum_{i=1}^{n} \lvert y_{\text{true},i} - y_{\text{pred},i} \rvert$

   Dimana:  
   - $\( y_{\text{true},i} \)$ adalah nilai sebenarnya untuk data ke-\(i\).  
   - $\( y_{\text{pred},i} \)$ adalah nilai prediksi untuk data ke-\(i\).  
   - $\( n \)$ adalah jumlah data.  

### Evaluasi Model
Berikut adalah hasil metrik yang didapatkan dari masing-masing proses evaluasi algoritma:

| Model | Mean Squared Error (MSE) | Mean Absolute Error (MAE) |
|-------|--------------------------|---------------------------|
| LR    | 3.508515                 | 0.454501                  |
| DT    | 13.946788                | 1.773880                  |
| RF    | 5.225100                 | 1.142210                  |
| GB    | 4.387732                 | 0.832583                  |
| SVR   | 5.093583                 | 1.139980                  |

Lebih jelasnya, hasil evaluasi model-model yang digunakan digambarkan pada grafik berikut:

![image](https://github.com/user-attachments/assets/e1fbe47c-94a6-4beb-8858-347cdcec3672)

- Berdasarkan grafik "Perbandingan Performa Model", model Linear Regression (LR) memiliki nilai Mean Squared Error (MSE) terendah, yaitu 3.51, serta nilai Mean Absolute Error (MAE) yang juga cukup rendah. Ini menunjukkan bahwa model Linear Regression memiliki akurasi prediksi terbaik di antara model-model yang dibandingkan.

- Model Gradient Boosting (GB) juga menunjukkan performa yang sangat baik, dengan nilai MSE 4.39 dan MAE yang relatif rendah. Meskipun sedikit lebih tinggi dibandingkan Linear Regression, Gradient Boosting masih merupakan salah satu model terbaik dalam kasus ini.

- Sementara itu, model Random Forest (RF) memiliki nilai MSE 5.23 dan MAE yang sedikit lebih tinggi. Support Vector Regression (SVR) memiliki nilai MSE 5.09 dan MAE yang juga lebih tinggi daripada Linear Regression dan Gradient Boosting. Meskipun masih menunjukkan performa yang cukup baik, model-model ini tidak unggul dibandingkan Linear Regression dan Gradient Boosting.

- Model Decision Tree (DT) memiliki nilai MSE paling tinggi, yaitu 12.82, serta nilai MAE yang juga lebih buruk daripada model-model lainnya. Ini menunjukkan bahwa model Decision Tree memiliki performa paling rendah di antara model-model yang dibandingkan.

**Secara keseluruhan, dapat disimpulkan bahwa model Linear Regression merupakan model terbaik berdasarkan nilai MSE dan MAE yang paling rendah.**

### Contoh 10 Data Prediksi
Berikut adalah 10 contoh perbandingan nilai asli dan hasil prediksi model yang digunakan:

| **Index** | **y_true** | **prediksi_LR** | **prediksi_DT** | **prediksi_RF** | **prediksi_GB** | **prediksi_SVR** |
|-----------|------------|-----------------|-----------------|-----------------|-----------------|------------------|
| 3024      | 62         | 62.123519       | 61.625000       | 63.71           | 63.707048       | 63.343930        |
| 2754      | 65         | 65.053911       | 64.888889       | 64.17           | 65.266467       | 63.599576        |
| 6363      | 70         | 69.709080       | 67.287500       | 68.32           | 68.856883       | 68.401405        |
| 3753      | 63         | 63.315235       | 62.645161       | 63.10           | 62.564249       | 63.268075        |
| 5154      | 62         | 61.858399       | 61.285714       | 61.59           | 61.404107       | 62.536896        |
| 2339      | 66         | 65.883455       | 66.500000       | 66.75           | 66.371123       | 66.859308        |
| 3500      | 68         | 67.799348       | 68.000000       | 69.08           | 68.613654       | 68.869134        |
| 1563      | 66         | 66.603065       | 65.000000       | 68.31           | 67.139535       | 65.750518        |
| 4493      | 65         | 64.944518       | 65.650000       | 65.15           | 65.212079       | 65.453077        |
| 1001      | 72         | 72.611754       | 71.500000       | 72.90           | 72.266877       | 72.486120        |

Berdasarkan tabel di atas, kita dapat melihat bahwa model Linear Regression (LR) memiliki prediksi yang paling mendekati nilai aktual (y_true) di antara model-model yang dibandingkan.

### Feature Importance
Analisis fitur terpenting dilakukan menggunakan framework SHAP (SHapley Additive exPlanations) untuk melihat pengaruh fitur-fitur dalam dataset terhadap prediksi model. Berikut adalah hasil analisis fitur terpenting terhadap model Linear Regression sebagai model dengan performa terbaik menggunakan SHAP:

![image](https://github.com/user-attachments/assets/97dc0631-74e8-4cb4-9219-f54da3da3c3d)

Dari hasil visualisasi di atas, didapatkan bahwa:
- **Attendance** dan **Hours_Studied** memiliki dampak terbesar pada prediksi model. Kehadiran yang tinggi dan jam belajar yang banyak berhubungan dengan nilai prediksi yang lebih tinggi.
- **Access_to_Resources**, **Parental_Involvement**, dan **Previous_Scores** juga memberikan pengaruh signifikan, meskipun lebih kecil dibandingkan dengan **Attendance** dan **Hours_Studied**.
- **Gender_Male**, **School_Type_Public**, dan **Sleep_Hours** memiliki dampak kecil pada model, dengan nilai SHAP yang lebih terpusat di sekitar 0.
- Pada fitur **Parental_Education_Level**, tingkat pendidikan orang tua yang lebih tinggi meningkatkan prediksi model, sementara tingkat pendidikan yang lebih rendah menurunkan prediksi.

## Conclusion
Proyek ini bertujuan untuk memahami faktor-faktor yang memengaruhi kinerja akademik siswa, menentukan faktor utama, serta membangun model prediksi nilai ujian. Berdasarkan analisis data dan eksperimen model, berikut adalah poin-poin utama kesimpulan yang dapat menjawab problem statement dan mencapai goals proyek ini:

### Model Prediksi Terbaik  
Dari berbagai model yang diuji (**Linear Regression**, **Decision Tree**, **Random Forest**, **Gradient Boosting**, dan **Support Vector Regression**), **Linear Regression** menunjukkan performa terbaik dengan nilai **MSE terendah (3.51)** dan **MAE terendah (0.45)**. Hal ini mengindikasikan bahwa model ini memiliki kemampuan prediksi yang paling akurat dalam kasus ini.

### Faktor Utama yang Mempengaruhi Nilai Ujian  
Berdasarkan analisis feature importance menggunakan metode SHAP, didapatkan 5 fitur dengan pengaruh paling signifikan terhadap nilai ujian adalah sebagai berikut:
1. **Attendance**
2. **Hours_Studied**
3. **Access_to_Resources**
4. **Parental_Involvement**
5. **Previous_Scores**

### Implikasi Praktis  
- **Untuk Sekolah**: Peningkatan kehadiran siswa sangat penting. Sekolah dapat merancang kebijakan yang memotivasi siswa untuk hadir secara teratur, seperti memberikan penghargaan bagi siswa dengan kehadiran tinggi atau meningkatkan keterlibatan siswa dalam aktivitas kelas. Selain itu, program belajar tambahan atau bimbingan dapat dioptimalkan untuk membantu siswa yang kurang hadir.  
- **Untuk Orang Tua**: Orang tua harus lebih terlibat dalam proses pendidikan anak, khususnya dalam mendukung jam belajar dan kehadiran mereka di sekolah. Orang tua dapat membantu menciptakan rutinitas belajar yang lebih terstruktur di rumah dan memotivasi anak untuk berpartisipasi aktif dalam kegiatan sekolah.  
- **Untuk Kebijakan Pendidikan**: Memperbaiki akses ke sumber daya pendidikan sangat penting untuk mendukung hasil akademik. Pemerintah dan lembaga pendidikan dapat meningkatkan kualitas fasilitas pendidikan, memperluas akses ke alat belajar yang lebih baik, serta memastikan bahwa siswa mendapatkan dukungan yang cukup dari lingkungan sosial mereka.  

### Rekomendasi Intervensi Berbasis Data  
1. **Peningkatan Kehadiran Siswa**: Mengimplementasikan program penghargaan atau insentif untuk siswa yang memiliki kehadiran tinggi, serta menyediakan sistem pemantauan untuk mendeteksi siswa dengan tingkat absensi tinggi dan memberikan dukungan tambahan.  
2. **Peningkatan Jam Belajar**: Sekolah dapat menyediakan lebih banyak sesi bimbingan atau kelas tambahan untuk mendukung jam belajar siswa, terutama bagi mereka yang membutuhkan bantuan lebih.  
3. **Peningkatan Akses ke Sumber Daya Pendidikan**: Menyediakan lebih banyak akses ke bahan ajar digital, buku, atau alat bantu belajar lainnya, dan memperbaiki infrastruktur sekolah untuk mendukung pembelajaran yang lebih baik.  
4. **Keterlibatan Orang Tua**: Menyelenggarakan lebih banyak kegiatan yang melibatkan orang tua, seperti workshop atau seminar tentang cara mendukung anak-anak mereka dalam belajar dan menciptakan lingkungan belajar yang kondusif di rumah.  
5. **Peningkatan Kualitas Pendidikan Sebelumnya**: Memberikan dukungan ekstra kepada siswa yang memiliki skor rendah sebelumnya, termasuk sesi remedial atau bimbingan khusus, agar mereka dapat mengejar ketertinggalan dan memperbaiki hasil akademiknya.

