import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình giao diện Web
st.set_page_config(page_title="Quản Lý Điểm Sinh Viên", layout="wide")

# 1. Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")

# Dữ liệu 10 sinh viên
data = {
    'Họ tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [9.0, 8.0, 7.5, 9.5, 8.5, 7.0, 9.0, 8.0, 8.5, 10.0],
    'Giữa kỳ': [8.0, 7.5, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Cuối kỳ': [8.5, 8.0, 6.0, 8.5, 6.5, 5.5, 8.0, 6.5, 7.5, 9.5]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df['Tổng kết'] = (df['Chuyên cần'] * 0.2 + df['Giữa kỳ'] * 0.3 + df['Cuối kỳ'] * 0.5).round(2)

# Xếp loại
def xep_loai(score):
    if score >= 8.5:
        return 'Giỏi'
    elif score >= 7.0:
        return 'Khá'
    elif score >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 2. Hiển thị bảng điểm của 10 sinh viên
st.subheader("📋 Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# 3. Hiển thị các chỉ số thống kê
st.subheader("📊 Thống kê chung")
dtb = round(df['Tổng kết'].mean(), 2)
max_sv = df.loc[df['Tổng kết'].idxmax()]
min_sv = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình lớp", f"{dtb}")
col2.metric("Điểm cao nhất", f"{max_sv['Họ tên']} ({max_sv['Tổng kết']})")
col3.metric("Điểm thấp nhất", f"{min_sv['Họ tên']} ({min_sv['Tổng kết']})")
col4.metric("Số SV đạt (>=5.0)", f"{so_sv_dat}/{len(df)}")

st.markdown("---")

# 4. Tạo danh sách sổ xuống (Selectbox) để người dùng chọn một sinh viên
st.subheader("🔍 Tra cứu chi tiết sinh viên")
selected_student = st.selectbox("Chọn sinh viên:", df['Họ tên'])

# Khi chọn sinh viên, hiển thị Chuyên cần, Giữa kỳ, Cuối kỳ, Điểm tổng kết và Xếp loại
sv = df[df['Họ tên'] == selected_student].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.write(f"**Chuyên cần:** {sv['Chuyên cần']}")
c2.write(f"**Giữa kỳ:** {sv['Giữa kỳ']}")
c3.write(f"**Cuối kỳ:** {sv['Cuối kỳ']}")
c4.write(f"**Điểm tổng kết:** {sv['Tổng kết']}")
c5.write(f"**Xếp loại:** {sv['Xếp loại']}")

st.markdown("---")

# 5. Hiển thị biểu đồ cột điểm tổng kết
st.subheader("📈 Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(df['Họ tên'], df['Tổng kết'], color='#4a90e2')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Họ tên')
ax.set_title('Thống kê điểm tổng kết')
ax.set_xlim(0, 10)
ax.invert_yaxis()
ax.grid(axis='x', linestyle='--', alpha=0.6)
st.pyplot(fig)
# 6. Hiển thị họ tên và MSSV của người tạo ở cuối trang với kích thước chữ nhỏ
st.markdown("---")
st.caption("<p style='text-align: center; font-size: 12px; color: gray;'>Họ tên sinh viên: <b>Hoàng Quang Trường</b> | MSSV: <b>[064208008876]</b></p>", unsafe_allow_html=True)
