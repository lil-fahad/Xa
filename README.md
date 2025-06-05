
# 🛋️ Furniture AI ∞X

نظام ذكي متكامل لتخطيط الأثاث، توليده، وعرضه باستخدام الواقع المعزز. يجمع بين FastAPI وStreamlit وOpenCV.

---

## 📦 مكونات المشروع

- **FastAPI** — واجهات برمجية (`/generate`, `/plan`, `/evaluate`)
- **Streamlit** — واجهة تفاعلية تدعم AR وتحليل المخطط
- **OpenCV** — لاكتشاف الحواف من صورة المخطط
- **model-viewer** — لعرض نماذج ثلاثية الأبعاد

---

## 🚀 طريقة التشغيل

### 1. تشغيل محلي

```bash
pip install -r requirements.txt
uvicorn main:app --reload  # FastAPI
streamlit run ar_module/streamlit_combined_viewer.py  # Streamlit
```

### 2. باستخدام Docker

```bash
docker build -t furniture-ai .
docker run -p 8000:8000 -p 8501:8501 furniture-ai
```

---

## 🧪 نقاط النهاية (API)

### `/generate`
- **POST**: توليد قطعة أثاث بناءً على النمط، الغرفة، والميزانية

### `/plan`
- **POST**: تخطيط توزيع الأثاث داخل غرفة بمساحة معينة

### `/evaluate`
- **POST**: تقييم التخطيط والجماليات

---

## 🖼️ Streamlit واجهة
- تحميل صورة مخطط
- تحليل الحواف تلقائيًا
- توليد وتوزيع وتقييم أثاث
- عرض ثلاثي الأبعاد تفاعلي لكل قطعة أثاث

---

## 📂 هيكل المشروع

```
furniture_ai_vx_6/
├── main.py
├── launch_streamlit.py
├── Dockerfile
├── launch.sh
├── requirements.txt
├── ar_module/
├── generator/
├── planner/
├── evaluator/
└── ...
```

---

## 🧠 فكرة مستقبلية

- استخدام YOLO أو Detectron2 لتحليل الغرف الحقيقية
- توليد ثلاثي الأبعاد ديناميكي
- توصية ذكية بالأثاث

---

تم التطوير بواسطة AI بالتعاون مع المستخدم 💡
