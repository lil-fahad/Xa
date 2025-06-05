import streamlit as st
from PIL import Image

def process_plan_image(image_bytes):
    return {
        "Living Room": {"suggested_items": ["كنبة", "طاولة", "سجاد"], "dimensions": "5x4m"},
        "Bedroom": {"suggested_items": ["سرير", "مرآة", "كومود"], "dimensions": "4x4m"}
    }

models = {
    "كنبة": "https://free3d.com/3d-model/sofa-12345.glb",
    "سرير": "https://free3d.com/3d-model/modern-bed-67890.glb",
    "طاولة": "https://free3d.com/3d-model/coffee-table-13579.glb",
    "مرآة": "https://free3d.com/3d-model/wall-mirror-24680.glb",
    "كومود": "https://free3d.com/3d-model/drawer-cabinet-11223.glb",
    "مكتب": "https://free3d.com/3d-model/office-desk-33445.glb",
    "دولاب": "https://free3d.com/3d-model/wardrobe-55667.glb"
}

st.set_page_config(page_title="تحليل المخطط + AR", layout="centered")
st.title("🏡 تحليل مخطط البيت + عرض الأثاث بالواقع المعزز")

uploaded_image = st.file_uploader("📷 ارفع صورة المخطط", type=["png", "jpg", "jpeg"])
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="مخطط البيت", use_column_width=True)
    if st.button("ابدأ التحليل والعرض"):
        result = process_plan_image(uploaded_image.read())
        for room, info in result.items():
            st.subheader(f"🛋 {room}")
            st.markdown(f"📏 {info['dimensions']}")
            for item in info["suggested_items"]:
                st.markdown(f"- {item}")
                if item in models:
                    st.components.v1.html(f"""
                        <model-viewer src="{models[item]}" alt="{item}" auto-rotate camera-controls ar 
                        style='width: 100%; height: 400px; background: #f0f0f0;'></model-viewer>
                        <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
                    """, height=420)
