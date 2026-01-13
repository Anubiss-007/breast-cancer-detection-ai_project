import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_breast_cancer

# 1. โหลดโมเดล
try:
    model = joblib.load('cancer_model.joblib')
except Exception as e:
    st.error(f"ไม่สามารถโหลดโมเดลได้: {e}")
    st.stop()

# 2. โหลดข้อมูลเพื่อเอา "ค่าเฉลี่ยมาตรฐาน" มาใช้ (แทนเลข 0)
data = load_breast_cancer()
mean_values = np.mean(data.data, axis=0)

st.title("🏥 AI ตรวจวินิจฉัยมะเร็งเต้านม (Cloud Version)")
st.write("ระบบใช้งานได้สมบูรณ์แล้วบน Google Cloud Run ☁️")

# 3. ส่วนรับข้อมูล
st.subheader("กรุณากรอกข้อมูลเพื่อวิเคราะห์")
col1, col2 = st.columns(2)
with col1:
    radius = st.slider("Mean Radius (ขนาดก้อนเนื้อ)", 5.0, 30.0, 15.0)
with col2:
    texture = st.slider("Mean Texture (พื้นผิว)", 10.0, 40.0, 20.0)

# 4. เตรียมข้อมูลส่งให้ AI
input_data = mean_values.copy()
input_data[0] = radius
input_data[1] = texture
input_data[2] = 2 * 3.14159 * radius
input_data[3] = 3.14159 * (radius ** 2)

final_input = np.array([input_data])

# 5. ปุ่มทำนาย
if st.button("🔍 ตรวจผลวินิจฉัย"):
    prediction = model.predict(final_input)
    
    if prediction[0] == 0:
        st.error(f"ผลทำนาย: **Malignant (เนื้อร้าย/มีความเสี่ยง)** ⚠️")
        st.write(f"ค่า Radius {radius} มีความสัมพันธ์กับความเสี่ยงสูง")
    else:
        st.success(f"ผลทำนาย: **Benign (เนื้อดี/ปลอดภัย)** ✅")
        st.write(f"ค่า Radius {radius} ยังอยู่ในเกณฑ์ปกติ")
