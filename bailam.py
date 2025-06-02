import streamlit as st


st.title("Phân loại thể loại văn bản")

du_lieu = {
    "Thể thao": [
        "bóng", "đá", "trận", "thủ", "ghi", "bàn", "vô", "địch", "giải", "sân", "cầu", "lưới", "huấn", "luyện", "thể"
    ],
    "Chính trị": [
        "quốc", "hội", "đại", "biểu", "chính", "phủ", "đảng", "nhà", "nước", "dân", "luật", "pháp", "hiến", "cử", "nghị"
    ],
    "Giải trí": [
        "ca", "sĩ", "nhạc", "phim", "chương", "trình", "truyền", "hình", "giải", "trí", "sân", "khấu", "diễn", "hài"
    ],
    "Kinh tế": [
        "thị", "trường", "giá", "vàng", "chứng", "khoán", "đầu", "tư", "lãi", "suất", "lạm", "phát", "kinh", "doanh", "ngân", "hàng"
    ],
    "Giáo dục": [
        "học", "sinh", "giáo", "viên", "trường", "thi", "tốt", "nghiệp", "bài", "kiểm", "tra", "điểm", "lớp", "bằng", "đại", "học"
    ],
    "Công nghệ": [
        "công", "nghệ", "phần", "mềm", "ứng", "dụng", "máy", "tính", "trí", "tuệ", "nhân", "tạo", "AI", "robot", "lập", "trình"
    ],
    "Sức khỏe": [
        "bệnh", "viện", "bác", "sĩ", "thuốc", "sức", "khỏe", "virus", "tiêm", "chủng", "điều", "trị", "phòng", "chống"
    ],
    "Khoa học": [
        "nghiên", "cứu", "thí", "nghiệm", "khoa", "học", "tế", "bào", "phản", "ứng", "hóa", "vật", "lý", "sinh", "học"
    ],
    "Thời tiết": [
        "mưa", "bão", "nắng", "nhiệt", "độ", "khí", "hậu", "áp", "thấp", "dự", "báo", "gió", "ẩm", "nhiệt", "đới"
    ]
}

stop_words = [
    "là", "và", "của", "có", "cho", "với", "các", "những", "được", "đã",
    "trong", "khi", "một", "từ", "rằng", "thì", "này", "ở", "đó", "như", "vì"
]

van_ban = st.text_area("Nhập nội dung văn bản:")

if st.button("kiem tra"):
    if van_ban.strip() == "":
        st.write("Bạn chưa nhập nội dung.")
    else:
        tu_dien = van_ban.replace(",", "").replace(".", "").replace("!", "")
        tu_dien = van_ban.lower().split()
        tu_dien = [tu for tu in tu_dien if tu not in stop_words] 
        dem = {}
        for the_loai, tu_khoa in du_lieu.items():
            dem[the_loai] = sum(1 for tu in tu_dien if tu in tu_khoa)

        ket_qua = max(dem, key=dem.get)
        if all(d == 0 for d in dem.values()):
            st.write("Không xác định được thể loại văn bản.")
        else:
            ket_qua = max(dem, key=dem.get)
            st.write(f"Văn bản thuộc thể loại:{ket_qua}")