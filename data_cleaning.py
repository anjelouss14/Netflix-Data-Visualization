import pandas as pd
import os

# 1. Membaca dataset asli
df = pd.read_csv ("dataset/netflix_titles.csv")

print("Jumlah data sebelum dibersihkan:", len(df))

# 2. Menghapus data duplikat
df = df.drop_duplicates()

# 3. Menangani missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["date_added"] = df["date_added"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

# 4. Mengubah format tanggal
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# 5. Mengambil tahun dan bulan penambahan konten
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month

# 6. Membersihkan spasi pada kolom teks
text_columns = [
    "type", "title", "director", "cast",
    "country", "rating", "listed_in"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# 7. Membuat folder hasil cleaning
os.makedirs("dataset/cleaned", exist_ok=True)

# 8. Menyimpan dataset yang sudah dibersihkan
df.to_csv("dataset/cleaned/netflix_cleaned.csv", index=False)

print("Jumlah data setelah dibersihkan:", len(df))
print("Dataset berhasil dibersihkan!")
print("File tersimpan di dataset/cleaned/netflix_cleaned.csv")
