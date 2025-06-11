# import re

# # Làm làm sạch ký tự không phải chữ cái và số
# def clean_non_alphabetic(text):
#     text = re.sub(r'[,?.!/\\|_{}+=~@#$%^&*()]', '', text)
#     return text

# # Hàm làm sạch
# def clean(text):
#     text = text.lower()  # Viết thường
#     text = clean_non_alphabetic(text)  # Bỏ ký tự đặc biệt
#     text = re.sub(r'\s+', ' ', text)  # Loại bỏ khoảng cách thừa
#     return text

# # Hàm tách từ trong câu
# def tokenize(text):
#     words = text.split(' ')
#     return words

# # Hàm đếm từ
# def count_word(words):
#     freq = {}
#     for word in words:
#         if word in freq:
#             freq[word] = freq[word] + 1
#         else:
#             freq[word] = 1
#     return freq

# # Dữ liệu huấn luyện
# train_spam = 'Nhanh tay nhận ngay khuyến mãi cực lớn! Hôm nay duy nhất, giảm giá tới 70% cho hàng ngàn sản phẩm hot nhất thị trường. Cơ hội chỉ đến một lần, đừng bỏ lỡ! Truy cập ngay http://khuyenmai-sieusieu.vn để nhận ưu đãi cực sốc. Số lượng có hạn, ai nhanh tay người đó được!'
# train_not_spam = 'Chào bạn, mình gửi thông báo về cuộc họp nhóm vào 9h sáng ngày mai tại phòng họp B2. Nội dung họp gồm: cập nhật tiến độ dự án, phân chia công việc tuần tới và thông nhất kế hoạch báo cáo. Bạn vui lòng cho biết kế hoạch trình bày cá nhân và đến đúng giờ. Cảm ơn và hẹn gặp lại!'

# # Huấn luyện dữ liệu spam
# clean_spam = clean(train_spam)
# spam_words = tokenize(clean_spam)
# total_spam_words = len(spam_words)
# spam_freq = count_word(spam_words)

# # Huấn luyện dữ liệu not spam
# clean_not_spam = clean(train_not_spam)
# not_spam_words = tokenize(clean_not_spam)
# total_not_spam_words = len(not_spam_words)
# not_spam_freq = count_word(not_spam_words)

# # Danh sách phân biệt các từ trong 2 bộ dữ liệu
# vocab = []
# vocab.extend(spam_words)
# vocab.extend(not_spam_words)
# vocab = set(vocab)
# total_vocab = len(vocab)

# # Hàm dự đoán
# def predict(text):
#     text = clean(text)
#     words = tokenize(text)
#     prob_spam = 0.5
#     prob_not_spam = 0.5

#     # Tính xác suất spam
#     for word in words:
#         f_spam = spam_freq.get(word, 0)  # Nếu không có thì gán giá trị 0
#         p_spam = (f_spam + 1) / (total_spam_words + total_vocab)
#         prob_spam = prob_spam * p_spam

#         f_not_spam = not_spam_freq.get(word, 0)
#         p_not_spam = (f_not_spam + 1) / (total_not_spam_words + total_vocab)
#         prob_not_spam = prob_not_spam * p_not_spam

#     if prob_spam >= prob_not_spam:
#         print('Spam')
#     else:
#         print('Not spam')

# # Chạy ví dụ
# predict('Nhận ưu đãi cực sốc hôm nay')

import streamlit as st
import re

st.title("Phân loại văn bản spam hay không spam")

# ---- Các hàm xử lý văn bản ----
def lam_sach(text):
    text = text.lower()
    text = re.sub(r'[,?.!/\\|_{}+=~@#$%^&*()]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def tach_tu(text):
    return text.split(' ')

def dem_tu(words):
    tan_suat = {}
    for tu in words:
        if tu in tan_suat:
            tan_suat[tu] += 1
        else:
            tan_suat[tu] = 1
    return tan_suat

# ---- Dữ liệu mẫu để huấn luyện ----
spam = "Nhanh tay nhận ngay khuyến mãi cực lớn! Hôm nay duy nhất, giảm giá tới 70% cho hàng ngàn sản phẩm hot nhất thị trường."
not_spam = "Chào bạn, mình gửi thông báo về cuộc họp nhóm vào 9h sáng mai tại phòng B2. Nhớ đến đúng giờ nhé!"

# ---- Làm sạch và tách từ ----
spam = lam_sach(spam)
not_spam = lam_sach(not_spam)

ds_spam = tach_tu(spam)
ds_not_spam = tach_tu(not_spam)

ts_spam = dem_tu(ds_spam)
ts_not_spam = dem_tu(ds_not_spam)

tong_spam = len(ds_spam)
tong_not_spam = len(ds_not_spam)

tu_vung = list(set(ds_spam + ds_not_spam))
tong_tu = len(tu_vung)

# ---- Hàm phân loại ----
def du_doan(text):
    text = lam_sach(text)
    ds_tu = tach_tu(text)
    
    xs_spam = 0.5
    xs_khong = 0.5

    for tu in ds_tu:
        f_spam = ts_spam.get(tu, 0)
        p_spam = (f_spam + 1) / (tong_spam + tong_tu)
        xs_spam *= p_spam

        f_not = ts_not_spam.get(tu, 0)
        p_not = (f_not + 1) / (tong_not_spam + tong_tu)
        xs_khong *= p_not

    if xs_spam > xs_khong:
        return "Spam"
    else:
        return "Không spam"

test_cau = "Nhận ưu đãi cực sốc hôm nay"

ket_qua = du_doan(test_cau)

st.write(f"Nội dung:{test_cau}")
st.write(f"Kết quả:{ket_qua}")