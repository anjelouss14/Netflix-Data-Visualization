import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🎬",
    layout="wide"
)


# ==========================================
# 2. MEMBACA DATASET
# ==========================================

df = pd.read_csv("dataset/cleaned/netflix_cleaned.csv")

df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
)


# ==========================================
# 3. JUDUL DAN DESKRIPSI DASHBOARD
# ==========================================

st.title("🎬 Netflix Content Analysis Dashboard")

st.markdown("""
Dashboard ini menyajikan analisis terhadap film dan serial TV
yang tersedia pada platform Netflix.

Melalui dashboard ini, pengguna dapat melihat distribusi konten,
tren tahun rilis, negara produksi, genre, dan kategori usia penonton.
""")

st.divider()


# ==========================================
# 4. FILTER INTERAKTIF
# ==========================================

st.sidebar.header("🔎 Filter Dashboard")

# Filter jenis konten
selected_types = st.sidebar.multiselect(
    "Pilih Jenis Konten:",
    options=sorted(df["type"].dropna().unique()),
    default=sorted(df["type"].dropna().unique())
)

# Filter tahun rilis
min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())

selected_year = st.sidebar.slider(
    "Pilih Rentang Tahun Rilis:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Menerapkan filter
filtered_df = df[
    (df["type"].isin(selected_types)) &
    (df["release_year"].between(
        selected_year[0],
        selected_year[1]
    ))
].copy()


# ==========================================
# 5. KPI CARDS
# ==========================================

st.subheader("📊 Ringkasan Konten Netflix")

total_content = len(filtered_df)

total_movies = len(
    filtered_df[filtered_df["type"] == "Movie"]
)

total_tv_shows = len(
    filtered_df[filtered_df["type"] == "TV Show"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Content", f"{total_content:,}")

with col2:
    st.metric("Movies", f"{total_movies:,}")

with col3:
    st.metric("TV Shows", f"{total_tv_shows:,}")

st.divider()


# ==========================================
# 6. VISUALISASI DATA
# ==========================================

st.subheader("📈 Visualisasi Data Netflix")

if filtered_df.empty:

    st.warning(
        "Tidak ada data yang sesuai dengan filter yang dipilih."
    )

else:

    # --------------------------------------
    # GRAFIK 1: DISTRIBUSI MOVIE DAN TV SHOW
    # --------------------------------------

    type_data = filtered_df["type"].value_counts().reset_index()
    type_data.columns = ["type", "total"]

    fig1 = px.bar(
        type_data,
        x="type",
        y="total",
        color="type",
        title="Distribusi Movies dan TV Shows",
        labels={
            "type": "Jenis Konten",
            "total": "Jumlah Konten"
        },
        text="total"
    )

    fig1.update_traces(textposition="outside")

    st.plotly_chart(
        fig1,
        width="stretch"
    )


    # --------------------------------------
    # GRAFIK 2: TREN KONTEN BERDASARKAN TAHUN
    # --------------------------------------

    year_data = (
        filtered_df.groupby("release_year")
        .size()
        .reset_index(name="total")
        .sort_values("release_year")
    )

    fig2 = px.line(
        year_data,
        x="release_year",
        y="total",
        markers=True,
        title="Tren Konten Berdasarkan Tahun Rilis",
        labels={
            "release_year": "Tahun Rilis",
            "total": "Jumlah Konten"
        }
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )


    # --------------------------------------
    # GRAFIK 3: TOP 10 NEGARA PRODUKSI
    # --------------------------------------

    country_data = (
        filtered_df["country"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
    )

    country_data = country_data[
        ~country_data.isin(["Unknown", ""])
    ]

    top_countries = (
        country_data.value_counts()
        .head(10)
        .reset_index()
    )

    top_countries.columns = ["country", "total"]

    if not top_countries.empty:

        fig3 = px.bar(
            top_countries,
            x="total",
            y="country",
            orientation="h",
            title="10 Negara dengan Konten Terbanyak",
            labels={
                "country": "Negara",
                "total": "Jumlah Konten"
            }
        )

        fig3.update_layout(
            yaxis={"categoryorder": "total ascending"}
        )

        st.plotly_chart(
            fig3,
            width="stretch"
        )


    # --------------------------------------
    # GRAFIK 4: DISTRIBUSI RATING
    # --------------------------------------

    rating_data = (
        filtered_df["rating"]
        .fillna("Not Rated")
        .value_counts()
        .head(8)
        .reset_index()
    )

    rating_data.columns = ["rating", "total"]

    fig4 = px.pie(
        rating_data,
        names="rating",
        values="total",
        hole=0.4,
        title="Distribusi Rating Konten Netflix"
    )

    st.plotly_chart(
        fig4,
        width="stretch"
    )


    # --------------------------------------
    # GRAFIK 5: DISTRIBUSI GENRE
    # --------------------------------------

    genre_data = (
        filtered_df["listed_in"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
    )

    genre_data = genre_data[
        ~genre_data.isin(["Unknown", ""])
    ]

    top_genres = (
        genre_data.value_counts()
        .head(10)
        .reset_index()
    )

    top_genres.columns = ["genre", "total"]

    if not top_genres.empty:

        fig5 = px.treemap(
            top_genres,
            path=["genre"],
            values="total",
            title="10 Genre Konten Netflix Terpopuler"
        )

        st.plotly_chart(
            fig5,
            width="stretch"
        )


# ==========================================
# 7. INSIGHT DAN KESIMPULAN
# ==========================================

st.divider()

st.subheader("💡 Insight dan Temuan Data")

if not filtered_df.empty:

    most_common_type = filtered_df["type"].value_counts().idxmax()

    most_common_year = (
        filtered_df["release_year"]
        .value_counts()
        .idxmax()
    )

    st.markdown(f"""
    Berdasarkan hasil analisis dataset Netflix:

    1. Jenis konten dengan jumlah terbanyak adalah **{most_common_type}**.

    2. Tahun rilis dengan jumlah konten terbanyak adalah
       **{int(most_common_year)}**.

    3. Dashboard menunjukkan distribusi konten berdasarkan
       jenis, tahun rilis, negara produksi, rating, dan genre.

    4. Pengguna dapat menggunakan filter untuk melihat
       hasil analisis berdasarkan jenis konten dan rentang tahun rilis.
    """)

else:

    st.info(
        "Insight belum tersedia karena tidak ada data yang ditampilkan."
    )


# ==========================================
# 8. FOOTER
# ==========================================

st.divider()

st.caption(
    "Netflix Content Analysis Dashboard | Data Visualization Project 2026"
)