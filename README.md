📊 E-Commerce Executive Performance Dashboard
Project ini adalah sebuah Executive Analytics Control Tower interaktif yang dibangun menggunakan tech stack Python, Streamlit, dan Plotly. Data product ini dirancang untuk mengubah data transaksional e-commerce yang masih mentah (raw data) menjadi high-fidelity visual insights, sehingga memudahkan jajaran C-Level dan tim lintas divisi untuk mengambil keputusan strategis yang berbasis data (data-driven decision making).

🚀 Overview & Deskripsi Interface
Dashboard ini didesain khusus untuk menjembatani kebutuhan visualisasi tingkat makro (C-Level strategic overview) hingga analisis taktis tingkat mikro (operational deep-dive). Menghindari pendekatan laporan konvensional yang cuma bersifat deskriptif, user interface (UI) aplikasi ini mengusung filosofi "Data-to-Action Blueprint" yang dibagi menjadi 4 zona fungsional:

High-Level Financial & Operational KPIs: Terletak di bagian paling atas halaman untuk memberikan instant situational awareness. Bagian ini nge-highlight core metrics seperti Total Revenue, Total Profit, Profit Margin (%), Volume Sold, Logistics Costs, dan Average Order Processing Time (Aging).

Interactive Control Center: Berupa panel filter dinamis multi-sektoral (Region, Product Category, Segment) yang memungkinkan user untuk melakukan slice and dice ke seluruh dataset secara real-time dengan latensi rendering yang sangat minim.

Core Business Insights Zone: Mengombinasikan visualisasi tingkat lanjut seperti dual-axis combo chart dan horizontal grouped bar chart untuk memetakan tren musiman (seasonality) serta korelasi antara penetrasi pasar dan tingkat profitabilitas produk.

Leakage Profit Monitor (Early Warning System): Sebuah komponen data matrix interaktif yang diperkuat dengan Conditional Heatmap Rendering. Komponen ini secara otomatis akan memunculkan 10 kombinasi produk dan wilayah paling boncos (unprofitable), jadi manajemen bisa langsung mendeteksi kebocoran finansial tanpa harus bongkar data manual.

🛠️ Technical Architecture & Pipeline Process
Aplikasi ini berjalan di atas arsitektur monolitik ringan yang sangat efisien untuk proses on-the-fly analytical processing. Berikut adalah gambaran data pipeline internalnya:

[Raw CSV Dataset] ──> [In-Memory Ingestion] ──> [Data Sanitization] ──> [Dynamic Filtering] ──> [Reactive UI Rendering]
Data Ingestion & Caching: Data di-ingest secara asinkron dari file flat .csv. Optimasi performa dilakukan dengan memanfaatkan built-in decorator @st.cache_data dari Streamlit. Cara ini menjamin operasi I/O yang berat dan proses initial load cuma jalan sekali di awal, sehingga memangkas runtime latency saat user gonta-ganti filter.

Data Sanitization & Type Enforcement: Untuk mengatasi masalah mixed-type column (inkonsistensi tipe data) yang sering ditemui di data transaksi, pipeline ini menjalankan regex cleaning tingkat lanjut untuk menyingkirkan karakter non-angka seperti simbol mata uang ($, ,) dan trailing spaces. Kolom finansial yang krusial dipaksa (type casting) menjadi data type float64 atau int64 untuk menjaga akurasi kalkulasi matematika, ditambah penanganan missing values lewat fungsi .fillna(0.0).

Reactive Filtering Engine: Memanfaatkan operasi boolean masking pada Pandas DataFrame yang di-bind langsung ke stateful widgets milik Streamlit. Hasilnya, visualisasi bisa langsung di-render ulang (reactive re-rendering) di sisi client tanpa perlu page reload penuh.

📐 Metodologi & Framework
Pengembangan analytics tool ini dipandu oleh Actionable Analytics Framework, yang dieksekusi lewat beberapa fase berikut:

KPI Balanced Scorecard Selection: Penentuan metrik diatur agar seimbang antara Financial Health (Sales, Profit, Margin) dan Operational Velocity (Logistics Cost, Aging, Order Priority) untuk menghindari bias saat penarikan kesimpulan.

Calculated Field Engineering: Merancang logika agregasi runtime untuk metrik Profit Margin (%) dan Average Aging. Rumus ini menghitung secara dinamis berdasarkan status filter yang sedang aktif, menghindari jebakan eror kalkulasi rata-rata statis (row-average calculation).

Cognitive Load-Driven Visualization: Pemilihan jenis grafik disesuaikan untuk meminimalkan cognitive load (beban otak) user. Dual-axis combo chart dipakai untuk membandingkan dua skala metrik yang berbeda jauh (skala volume batang vs skala persentase garis), sementara horizontal bar chart dipilih agar label nama produk yang panjang tetap terbaca utuh dengan jelas.

Anomaly & Loss Prioritization: Memanfaatkan teknik Ascending Aggregative Sorting untuk memaksa data-data dengan nilai profit negatif (losses) naik ke baris paling atas pada matriks, didukung visualisasi reverse-red gradient heatmap agar langsung menarik perhatian mata eksekutif.

📈 Key Insights & Kesimpulan Strategis
Dari hasil testing menggunakan prototype dashboard pada dataset transaksi e-commerce ini, ada beberapa kesimpulan kritikal yang bisa diambil untuk kebutuhan corporate strategy:

Isolasi Profit Leakage: Dashboard berhasil mendeteksi anomali di mana ada beberapa produk dengan volume penjualan tinggi (High Sales) tapi justru menghasilkan profit negatif. Setelah di-trace, ini terjadi karena akumulasi pemberian diskon (Discount) yang terlalu agresif di wilayah tertentu yang kebetulan biaya logistiknya (Shipping Cost) juga tinggi.

Audit Operational Bottleneck: Lewat grafik Order Priority vs. Avg Aging, manajemen bisa langsung mengaudit performa operasional gudang untuk memastikan apakah pesanan dengan status Critical benar-benar di-dispatch lebih cepat daripada pesanan berstatus Low.

Diversifikasi Risiko Pasar: Analisis pada porsi segmen memberikan indikasi jelas mengenai ketergantungan revenue pada satu segmen pelanggan saja. Ini menjadi sinyal bagi tim marketing untuk mulai menggeser strategi akuisisi ke segmen B2B (Corporate dan Home Office) yang secara histori punya profit margin lebih stabil.

Kesimpulan Akhir: Data product ini berhasil mengubah fungsi analitik e-commerce yang tadinya cuma sekadar pelaporan historis yang pasif (historical reporting) menjadi sebuah business control tower yang aktif, siap mendorong kelincahan korporasi (corporate agility), dan mengoptimalkan profitabilitas bisnis.
