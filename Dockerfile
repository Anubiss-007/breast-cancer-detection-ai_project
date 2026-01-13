# ใช้ Python เวอร์ชัน Slim เหมือนเดิม (แต่เดี๋ยวเราจะเติมของที่ขาด)
FROM python:3.10.19-slim

# ตั้งค่าโฟลเดอร์ทำงาน
WORKDIR /app

# 🔥 ส่วนที่เพิ่มใหม่: สั่งติดตั้ง libgomp1 (ตัวช่วยคำนวณ AI)
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# ก๊อปปี้ไฟล์ requirements และติดตั้ง Python Library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ก๊อปปี้ไฟล์ทั้งหมด
COPY . .

# ตั้งค่า Port
ENV PORT=8080

# สั่งรัน Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
