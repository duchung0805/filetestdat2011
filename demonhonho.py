import streamlit as st
import datetime
st.title("heloo dp202011")
tu = "Kinh tế là hệ thống các hoạt động sản xuất, phân phối và tiêu dùng hàng hóa, dịch vụ nhằm đáp ứng nhu cầu của con người. Nó bao gồm các mối quan hệ giữa người tiêu dùng, doanh nghiệp và nhà nước trong việc sử dụng nguồn lực khan hiếm như lao động, vốn và tài nguyên. Kinh tế"

ds_tu = {}

loc_tu = tu.replace(".","")
tach_tu = loc_tu.split()

for tu in tach_tu :
    if tu not in ds_tu:
        ds_tu[tu] = 1
    else:
        ds_tu[tu] += 1

st.title(ds_tu)

st.header("tinh tuoi")

nam_sinh = st.number_input("moi nhap nam sinh")
if nam_sinh:
    nam_hien_tai = 2025

    tuoi = nam_hien_tai - nam_sinh

    st.title(f"tuoi cua ban la : {tuoi} tuoi")

# tai len file va dem so luong tu

file_tal = st.file_uploader("tai len file van ban")

if file_tal is not None :
    noi_dung =  file_tal.read().decode("utf-8") # doc noi dung file
    do_dai = len(noi_dung)
    st.write(f"file co do dai {do_dai} tu ")