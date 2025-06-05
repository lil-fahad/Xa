
# ---- مرحلة الأساس ----
FROM python:3.10-slim

# إعداد مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY . /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تثبيت أدوات التشغيل الإضافية
RUN pip install --no-cache-dir uvicorn streamlit

# نسخ ملف الإطلاق الموحد
COPY launch.sh /app/launch.sh
RUN chmod +x /app/launch.sh

# المنفذ الافتراضي
EXPOSE 8000
EXPOSE 8501

# تشغيل FastAPI وStreamlit معًا
CMD ["bash", "launch.sh"]
