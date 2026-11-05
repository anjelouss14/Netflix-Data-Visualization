# Netflix Content Analysis Dashboard

## Identitas Project

- **Nama Project:** Netflix Content Analysis Dashboard
- **Nama Mahasiswa:** Angelika
- **NIM:** 241051027
- **Mata Kuliah:** Visualisasi Data
- **Tahun:** 2026

## Deskripsi Project

Netflix Content Analysis Dashboard merupakan project visualisasi data yang bertujuan untuk menganalisis distribusi film dan serial TV yang tersedia pada platform Netflix.

Project ini menggunakan dataset Netflix Movies and TV Shows yang diperoleh dari Kaggle. Data diolah dan dibersihkan menggunakan Python dan Pandas, kemudian divisualisasikan melalui dashboard interaktif menggunakan Streamlit dan Plotly.

Dashboard ini membantu pengguna memahami karakteristik konten Netflix berdasarkan jenis konten, tahun rilis, negara produksi, kategori rating, dan genre.

## Dataset

Dataset yang digunakan:

- **Nama Dataset:** Netflix Movies and TV Shows
- **Sumber:** Kaggle
- **Link Dataset:** https://www.kaggle.com/datasets/shivamb/netflix-shows
- **Jumlah Data:** 8.807 baris
- **Jumlah Kolom:** 12 kolom

Dataset merupakan data sekunder yang berisi informasi mengenai film dan serial TV pada platform Netflix.

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Visual Studio Code

## Fitur Dashboard

Dashboard menyediakan beberapa fitur utama:

### 1. KPI Cards
Menampilkan ringkasan jumlah keseluruhan konten, jumlah Movies, dan jumlah TV Shows.

### 2. Visualisasi Data
Dashboard menyediakan lima jenis visualisasi:

- Bar Chart: Distribusi Movies dan TV Shows.
- Line Chart: Tren konten berdasarkan tahun rilis.
- Horizontal Bar Chart: 10 negara dengan konten terbanyak.
- Pie Chart: Distribusi rating konten.
- Treemap: Distribusi 10 genre terpopuler.

### 3. Filter Interaktif
Pengguna dapat melakukan penyaringan data melalui:

- Filter jenis konten (Movie dan TV Show).
- Filter rentang tahun rilis.

### 4. Insight dan Kesimpulan
Menampilkan temuan berdasarkan data yang telah difilter, termasuk jenis konten terbanyak dan tahun rilis dengan jumlah konten tertinggi.

## Data Cleaning

Proses preprocessing dilakukan menggunakan file `data_cleaning.py`, yang mencakup:

1. Membaca dataset asli.
2. Menghapus data duplikat.
3. Menangani missing values.
4. Mengubah format tanggal.
5. Mengekstrak tahun dan bulan penambahan konten.
6. Membersihkan spasi pada kolom teks.
7. Menyimpan dataset hasil preprocessing ke folder `dataset/cleaned/`.

## Struktur Repository

```text
Netflix-Data-Visualization/
│
├── app.py
├── data_cleaning.py
├── requirements.txt
│
└── dataset/
    ├── netflix_titles.csv
    └── cleaned/
        └── netflix_cleaned.csv
```

## Key Insights

Dashboard digunakan untuk mengidentifikasi beberapa temuan utama:

1. Perbandingan jumlah film dan serial TV yang tersedia dalam dataset Netflix.
2. Tren distribusi konten berdasarkan tahun rilis.
3. Negara-negara dengan jumlah produksi konten terbanyak.
4. Distribusi konten berdasarkan kategori rating.
5. Genre dengan jumlah konten terbanyak.

Hasil analisis dapat dieksplorasi lebih lanjut melalui filter interaktif pada dashboard.

## Live Dashboard

Dashboard dapat diakses melalui link berikut:

**[Link Dashboard akan ditambahkan setelah deployment]**

## Cara Menjalankan Project

Untuk menjalankan project secara lokal, ikuti langkah berikut:

1. Pastikan Python sudah terinstal.
2. Clone repository GitHub:

```bash
git clone [LINK-REPOSITORY]
```

3. Masuk ke folder project:

```bash
cd Netflix-Data-Visualization
```

4. Instal library yang dibutuhkan:

```bash
py -m pip install -r requirements.txt
```

5. Jalankan dashboard:

```bash
py -m streamlit run app.py
```

6. Buka alamat lokal yang ditampilkan pada terminal.

## Penutup

Project ini dibuat sebagai implementasi penerapan preprocessing, eksplorasi data, dan visualisasi data menggunakan Python. Melalui dashboard interaktif ini, diharapkan informasi dalam dataset Netflix dapat disajikan secara lebih informatif dan mudah dipahami.
