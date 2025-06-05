
import streamlit as st
from PIL import Image
import requests
import numpy as np
import cv2
from io import BytesIO

API_BASE = "http://localhost:8000"

models = {
    "كنبة": "https://free3d.com/3d-model/sofa-12345.glb",
    "سرير": "https://free3d.com/3d-model/modern-bed-67890.glb",
    "طاولة": "https://free3d.com/3d-model/coffee-table-13579.glb",
    "مرآة": "https://free3d.com/3d-model/wall-mirror-24680.glb",
    "كومود": "https://free3d.com/3d-model/drawer-cabinet-11223.glb",
    "مكتب": "https://free3d.com/3d-model/office-desk-33445.glb",
    "دولاب": "https://free3d.com/3d-model/wardrobe-55667.glb"
}

def analyze_floorplan(image: Image.Image):
    # تحويل PIL إلى OpenCV
    img_array = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

st.set_page_config(page_title="تحليل المخطط + AR", layout="centered")
st.title("🏡 تحليل مخطط البيت + عرض الأثاث بالواقع المعزز")

uploaded_image = st.file_uploader("📷 ارفع صورة المخطط", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="🧾 المخطط الأصلي", use_column_width=True)

    st.markdown("## ✏️ إعدادات التوليد")
    style = st.selectbox("اختر النمط", ["حديث", "كلاسيكي", "مودرن"])
    room_type = st.selectbox("نوع الغرفة", ["غرفة نوم", "غرفة معيشة"])
    budget = st.slider("الميزانية", 100.0, 2000.0, 500.0)

    if st.button("ابدأ التحليل والعرض"):
        with st.spinner("📊 تحليل الصورة..."):
            edge_result = analyze_floorplan(image)
            st.image(edge_result, caption="🧠 اكتشاف الحواف", use_column_width=True, channels="GRAY")

        with st.spinner("🚀 التخطيط والتوليد والتقييم..."):
            # 1. توليد قطعة أثاث
            gen_res = requests.post(f"{API_BASE}/generate", json={
                "style": style,
                "room_type": room_type,
                "budget": budget
            })
            if gen_res.status_code != 200:
                st.error("فشل في توليد الأثاث")
                st.stop()
            generated_item = gen_res.json()
            st.success(f"✅ تم توليد: {generated_item['name']}")

            # 2. التخطيط
            plan_res = requests.post(f"{API_BASE}/plan", json={
                "width": 5.0,
                "height": 4.0,
                "furniture_items": [generated_item["name"]]
            })
            if plan_res.status_code != 200:
                st.error("فشل في التخطيط")
                st.stop()
            layout = plan_res.json()["layout"]

            # 3. التقييم
            eval_res = requests.post(f"{API_BASE}/evaluate", json={
                "layout_quality": 8,
                "spacing_score": 0.7,
                "aesthetics_score": 0.8
            })
            eval_result = eval_res.json() if eval_res.status_code == 200 else None

            for item_data in layout:
                item = item_data["item"]
                st.subheader(f"{item} 📍")
                st.markdown(f"الموقع (x={item_data['x']}, y={item_data['y']})")
                if item in models:
                    st.components.v1.html(f"""
                        <model-viewer src="{models[item]}" alt="{item}" auto-rotate camera-controls ar 
                        style='width: 100%; height: 400px; background: #f0f0f0;'></model-viewer>
                        <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
                    """, height=420)

            if eval_result:
                st.markdown("## 📊 تقييم التصميم")
                st.metric("النتيجة الإجمالية", eval_result["overall_score"])
                st.success(f"{eval_result['rating']}: {eval_result['feedback']}")
