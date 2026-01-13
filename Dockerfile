# ใช้ Python เวอร์ชันเดียวกับที่คุณใช้พัฒนา (ตัวอย่างเป็น 3.9)
FROM python:3.10.19-slim

# ตั้งค่าโฟลเดอร์ทำงานใน Container
WORKDIR /app

# ก๊อปปี้ไฟล์ requirements.txt เข้าไปก่อน เพื่อติดตั้ง library
COPY requirements.txt .

# สั่งติดตั้ง library ตามที่ระบุไว้
RUN pip install --no-cache-dir -r requirements.txt

# ก๊อปปี้ไฟล์โค้ดและโมเดลทั้งหมดเข้าไป (. คือไฟล์ทั้งหมดในโฟลเดอร์ปัจจุบัน)
COPY . .

# กำหนด Port ที่จะให้ Container เปิดรอรับ (Cloud Run ชอบ Port 8080)
ENV PORT=8080

# หรือถ้าใช้ Streamlit (ยอดฮิตสำหรับงาน Data):
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]