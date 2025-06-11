# # File huấn luyện
# topic = "giao_duc"

# # B1: Nạp dữ liệu từ file
# with open('giao_duc.txt', mode='r', encoding='utf-8') as f:
#     noi_dung = f.read()

# # B2: Làm sạch (viết thường, loại dấu câu, khoảng trắng)
# noi_dung = noi_dung.lower() # Viết thường

# # Cách loại dấu câu viết dài
# # noi_dung = noi_dung.replace(',','').replace('.','').replace('-','').replace('?','').replace('!','')

# # Cách loại dấu câu viết ngắn - Dùng hàm for
# # for dau_cau in [',','.','-','!','?',':']:
# #    noi_dung = noi_dung.replace(dau_cau,'')

# # Cách loại dấu câu viết ngắn - Dùng regax
# import re
# noi_dung = re.sub(r'[,.?!@#]', '', noi_dung)


# # Loại bỏ khoảng trắng
# noi_dung = noi_dung.replace(' ', ' ')

# # B3: Loại bỏ các từ không lquan(stop words)
# with open('/Users/hungduc/Desktop/thư mục không có tiêu đề 5/chua bai assm/stopwords.txt', mode='r', encoding='utf-8') as f:

#     # stop_words = f.readlines() # Cách này còn dấu '\n' ở cuối câu
#     stop_words = [line.rstrip() for line in f] # Cách này kh còn dấu '\n'
# for word in stop_words:
#     noi_dung = noi_dung.replace(word,'')

# # B4: Tách từ
# ds_tu = noi_dung.split(' ')

# # B5: Đếm số lần xuâts hiện của các từ
# tan_suat = {}
# for tu in ds_tu:
#     if tu not in tan_suat:
#         tan_suat[tu] = 1
#     else:
#         tan_suat[tu] += 1

# # B6: Lưu kqua vào filefile
# file_out = topic + '-f.txt'
# with open(file_out, mode='w',encoding='utf-8') as f:
#     for tu in tan_suat:
#         f.write(f'{tu} : {tan_suat[tu]}\n')

# file: tan_suat_tu_streamlit.py
import streamlit as st
import re
import requests

st.title("Phân tích tần suất từ đơn giản")

# 📌 Tải stopwords từ Google Sheets (dạng CSV)
@st.cache_data
def lay_stopwords_tu_google_sheets():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR5S-EGtFGIN8nKcGFjFaeP3BBCPCjsqv4s5iQUJJKumdaZB31Z4R0gUDLVUOWIPElNRUR64HJ40wXf/pub?output=csv"
    response = requests.get(url)
    response.encoding = "utf-8"
    dong = response.text.splitlines()
    return [tu.strip() for tu in dong if tu.strip()]

stopwords = lay_stopwords_tu_google_sheets()

# B1. Tải tệp văn bản
van_ban_file = st.file_uploader("tải lên tệp văn bản txt", type="txt")

if van_ban_file:
    # B2. Đọc và làm sạch văn bản
    text = van_ban_file.read().decode("utf-8").lower()
    text = re.sub(r"[,.?!@#]", "", text)

    # B3. Loại stopword
    for sw in stopwords:
        text = text.replace(f" {sw} ", " ")

    # B4. Tách từ và đếm
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1

    # Hiển thị bảng kết quả
    st.write("Kết quả tần suất:")
    for w, c in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        st.write(f"{w} : {c}")

    # Cho phép tải về
    ket_qua = "\n".join(f"{w} : {c}" for w, c in freq.items())
    st.download_button("Tải file kết quả", ket_qua,
                       file_name="ket_qua.txt", mime="text/plain")
else:
    st.info(" ")
