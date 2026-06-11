# 📊 E-Commerce Executive Performance Dashboard

Dashboard analitik berbentuk **Executive Control Tower** siap pakai yang dibangun menggunakan **Python, Streamlit, dan Plotly**. Aplikasi ini menyulap data transaksi e-commerce yang mentah (*raw data*) menjadi visualisasi *high-fidelity*, membantu jajaran C-Level mengambil keputusan strategis secara cepat dan berbasis data.

## 🚀 Fitur Utama
* **High-Level KPI Scorecards:** Memberikan gambaran kilat performa Revenue, Profit, Margin, hingga kecepatan proses logistik.
* **Interactive Control Center:** *Filter* dinamis multi-sektoral (*Region, Product Category, Segment*) dengan pemrosesan *in-memory* tanpa latensi.
* **Core Business Insights:** Visualisasi tren musiman (*seasonality*) dan perbandingan performa profitabilitas kategori produk.
* **Leakage Profit Monitor:** Sistem peringatan dini dengan *Conditional Heatmap Rendering* untuk langsung mendeteksi 10 kombinasi produk dan wilayah paling rugi (boncos).

## 🛠️ Tech Stack & Arsitektur
* **Frontend/UI:** Streamlit (Komponen UI yang reaktif)
* **Visuals/Charts:** Plotly Express & Graph Objects (Rendering grafik dinamis)
* **Data Engine:** Pandas (Proses *ingestion in-memory*, *regex-based data sanitization*, dan pencarian berbasis *boolean masking*)
* **Optimization:** Menggunakan dekorator asli `@st.cache_data` untuk memangkas beban proses I/O yang berat.

## 💻 Quick Start

1. *Clone* repositori ini:
   ```bash
   git clone [https://github.com/username/repo-name.git](https://github.com/username/repo-name.git)
