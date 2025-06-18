import streamlit as st
import re

st.title("Phân loại bình luận tích cực / tiêu cực")


def lam_sach(text):
    text = text.lower()
    text = re.sub(r'[,.?/!\|_{}+=~@#$%^&*()]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tach_tu(text):
    return text.split()

def dem_tu(words):
    tan_suat = {}
    for tu in words:
        tan_suat[tu] = tan_suat.get(tu, 0) + 1
    return tan_suat

tich_cuc_vb = "Sản phẩm rất tuyệt vời, tôi rất hài lòng, dịch vụ tốt, giá hợp lý, nhân viên thân thiện, hỗ trợ nhiệt tình, trải nghiệm đáng nhớ, chất lượng vượt mong đợi, đóng gói cẩn thận, giao hàng nhanh chóng, sẽ quay lại mua lần nữa, đáng tiền, giao đúng giờ, sản phẩm chính hãng, cực kỳ ưng ý, tuyệt hảo, không có gì để chê."

tieu_cuc_vb = "Tôi thất vọng, chất lượng kém, phục vụ tệ, không hài lòng chút nào, nhân viên thô lỗ, giao hàng trễ, sản phẩm lỗi, hàng giả, đóng gói sơ sài, giá quá cao, không như quảng cáo, đổi trả phức tạp, thái độ phục vụ kém, không bao giờ mua lại, cực kỳ thất vọng, dịch vụ quá tệ, gọi mãi không nghe, hỗ trợ khách hàng kém."


tich_cuc_ds = tach_tu(lam_sach(tich_cuc_vb))
tieu_cuc_ds = tach_tu(lam_sach(tieu_cuc_vb))

ts_tich_cuc = dem_tu(tich_cuc_ds)
ts_tieu_cuc = dem_tu(tieu_cuc_ds)

tong_tich_cuc = len(tich_cuc_ds)
tong_tieu_cuc = len(tieu_cuc_ds)

tu_vung = list(set(tich_cuc_ds + tieu_cuc_ds))
tong_tu = len(tu_vung)

def du_doan(text):
    text = lam_sach(text)
    ds_tu = tach_tu(text)

    xs_tich = 0.5
    xs_tieu = 0.5

    for tu in ds_tu:
        p_tich = (ts_tich_cuc.get(tu, 0) + 1) / (tong_tich_cuc + tong_tu)
        p_tieu = (ts_tieu_cuc.get(tu, 0) + 1) / (tong_tieu_cuc + tong_tu)

        xs_tich *= p_tich
        xs_tieu *= p_tieu

    if xs_tich > xs_tieu:
        return "Tích cực"
    else:
        return "Tiêu cực"

test_cau = st.text_input("Nhập bình luận cần phân loại:")

if test_cau:
    kq = du_doan(test_cau)
    st.write(f"Nội dung: {test_cau}")
    st.write(f"Kết quả phân loại: {kq}")
