import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Executive Dashboard E-Commerce", layout="wide")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset-ecommerce - ecommerce.csv")
    
    # 1. Bersihkan nama kolom dari spasi di awal/akhir (jika ada)
    df.columns = df.columns.str.strip()
    
    # 2. Pastikan kolom Aging dan Quantity adalah angka murni
    for num_col in ['Aging', 'Quantity']:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors='coerce').fillna(0)

    # 3. Paksa konversi kolom Finansial dari Teks ke Angka Murni (Float)
    for col in ['Sales', 'Profit', 'Shipping Cost']:
        if col in df.columns:
            # Ubah ke string dulu, hapus karakter non-angka seperti $, koma, atau spasi
            df[col] = df[col].astype(str).str.replace('$', '', regex=False)
            df[col] = df[col].str.replace(',', '', regex=False).str.strip()
            
            # Paksa konversi ke numeric, jika ada baris eror/kosong akan diubah jadi NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Isi data yang kosong (NaN) dengan angka 0 agar tidak merusak perhitungan matematik
            df[col] = df[col].fillna(0.0)
            
    return df

df = load_data()

# ==============================================================================
# BARIS 1: HEADER & KONTROL FILTER
# ==============================================================================
st.title("📊 E-Commerce Executive Performance Dashboard")
st.markdown("---")

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    selected_region = st.multiselect("Filter Region:", options=df['Region'].unique(), default=df['Region'].unique())
with col_f2:
    selected_category = st.multiselect("Filter Category:", options=df['Product Category'].unique(), default=df['Product Category'].unique())
with col_f3:
    selected_segment = st.multiselect("Filter Segment:", options=df['Segment'].unique(), default=df['Segment'].unique())

# Filter Dataset
df_filtered = df[
    (df['Region'].isin(selected_region)) & 
    (df['Product Category'].isin(selected_category)) & 
    (df['Segment'].isin(selected_segment))
]

# ==============================================================================
# BARIS 2 & 3: HIGH-LEVEL FINANCIAL & OPERATIONAL KPI CARDS
# ==============================================================================
st.subheader("📈 High-Level Executive Summary")
total_sales = df_filtered['Sales'].sum()
total_profit = df_filtered['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
total_qty = df_filtered['Quantity'].sum()
total_shipping = df_filtered['Shipping Cost'].sum()
avg_aging = df_filtered['Aging'].mean()

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
kpi1.metric("Total Revenue", f"${total_sales:,.0f}")
kpi2.metric("Total Profit", f"${total_profit:,.0f}")
kpi3.metric("Profit Margin", f"{profit_margin:.1f}%")
kpi4.metric("Volume Terjual", f"{total_qty:,} pcs")
kpi5.metric("Biaya Logistik", f"${total_shipping:,.0f}")
kpi6.metric("Avg Lama Kirim", f"{avg_aging:.1f} Hari")

st.markdown("---")

# ==============================================================================
# BARIS 4 & 5: CORE BUSINESS INSIGHTS
# ==============================================================================
st.subheader("🎯 Core Business Insights")
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    monthly_data = df_filtered.groupby('Months')[['Sales', 'Profit']].sum().reset_index()
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Bar(x=monthly_data['Months'], y=monthly_data['Sales'], name='Revenue'))
    fig_trend.add_trace(go.Scatter(x=monthly_data['Months'], y=monthly_data['Profit'], name='Profit', yaxis='y2', line=dict(color='orange', width=3)))
    fig_trend.update_layout(
        title="Tren Revenue (Batang) vs Profit (Garis) Bulanan",
        yaxis=dict(title="Revenue ($)"),
        yaxis2=dict(title="Profit ($)", overlaying='y', side='right'),
        legend=dict(x=0, y=1.1, orientation="h")
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_chart2:
    cat_data = df_filtered.groupby('Product Category')[['Sales', 'Profit']].sum().reset_index().sort_values(by='Sales', ascending=True)
    fig_cat = px.bar(cat_data, y='Product Category', x=['Sales', 'Profit'], barmode='group',
                     title="Perbandingan Sales vs Profit per Kategori Produk", orientation='h')
    st.plotly_chart(fig_cat, use_container_width=True)

col_chart3, col_chart4 = st.columns(2)

with col_chart3:
    seg_data = df_filtered.groupby('Segment')['Sales'].sum().reset_index()
    fig_seg = px.pie(seg_data, values='Sales', names='Segment', hole=0.4, title="Porsi Penjualan per Segmen Pelanggan")
    st.plotly_chart(fig_seg, use_container_width=True)

with col_chart4:
    reg_data = df_filtered.groupby('Region')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
    fig_reg = px.bar(reg_data, x='Region', y='Sales', title="Total Penjualan per Wilayah (Region)", color='Sales')
    st.plotly_chart(fig_reg, use_container_width=True)

st.markdown("---")

# ==============================================================================
# BARIS 6 & 7: OPERATIONAL & PROBLEM-TO-ACTION MATRIX
# ==============================================================================
st.subheader("⚙️ Operational Efficiency & Action Items")
col_op1, col_op2 = st.columns(2)

with col_op1:
    op_data = df_filtered.groupby('Order Priority')['Aging'].mean().reset_index().sort_values(by='Aging')
    fig_op = px.bar(op_data, x='Order Priority', y='Aging', title="Rata-rata Lama Kirim Berdasarkan Prioritas Pesanan", 
                    labels={'Aging': 'Rata-rata Hari (Aging)'}, color='Aging', color_continuous_scale='Reds')
    st.plotly_chart(fig_op, use_container_width=True)

with col_op2:
    st.markdown("**🔴 Leakage Profit Monitor (Produk & Wilayah Paling Merugi)**")
    # Memastikan kolom 'Product' tersedia sebelum groupby
    target_prod_col = 'Product' if 'Product' in df_filtered.columns else df_filtered.columns[7]
    
    leak_df = df_filtered.groupby([target_prod_col, 'Region'])[['Sales', 'Profit']].sum().reset_index()
    leak_df = leak_df.sort_values(by='Profit', ascending=True).head(10)
    st.dataframe(leak_df.style.format({'Sales': '${:,.2f}', 'Profit': '${:,.2f}'})
                 .background_gradient(subset=['Profit'], cmap='Reds_r'))

# ==============================================================================
# REKOMENDASI STRATEGIS
# ==============================================================================
st.info("💡 **AKSI DAN SARAN STRATEGIS UNTUK EKSEKUTIF & TIM LINTAS DIVISI**")
st.markdown("""
- **Untuk Product & Pricing Manager:** Evaluasi produk-produk teratas pada tabel *Leakage Profit Monitor* di atas. Kurangi porsi diskon pada kombinasi wilayah dan produk yang menghasilkan profit negatif.
- **Untuk Operational & Logistik:** Jika visualisasi menunjukkan *Avg Lama Kirim* pada prioritas 'Critical' lebih tinggi dari 3 hari, tim operasional harus segera mengaudit sistem *sorting* di gudang.
- **Untuk Tim Marketing:** Tingkatkan penetrasi pasar pada segmen di luar *Consumer* (seperti *Corporate* atau *Home Office*) menggunakan strategi *bundling* produk skala besar guna mendiversifikasi risiko pendapatan.
""")