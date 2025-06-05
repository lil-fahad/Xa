import streamlit as st

models = {
    "كنبة": "https://modelviewer.dev/shared-assets/models/Sofa.glb",
    "سرير": "https://modelviewer.dev/shared-assets/models/RobotExpressive.glb",
    "طاولة": "https://modelviewer.dev/shared-assets/models/Chair.glb",
    "كراسي": "https://modelviewer.dev/shared-assets/models/Chair.glb",
    "مكتب": "https://modelviewer.dev/shared-assets/models/Desk.glb",
    "دولاب": "https://modelviewer.dev/shared-assets/models/ShopifyModels/Shoe.glb",
    "مرآة": "https://modelviewer.dev/shared-assets/models/NeilArmstrong.glb"
}

st.set_page_config(page_title="AR Furniture Viewer", layout="centered")
st.title("🪑 عرض الأثاث بالواقع المعزز – WebXR")

room_type = st.selectbox("اختر نوع الغرفة:", [
    "غرفة نوم", "غرفة معيشة", "مكتب", "غرفة طعام", "شرفة خارجية"
])

selected_items = st.multiselect("اختر القطع لعرضها بالـ AR:", list(models.keys()))

if st.button("عرض"):
    if not selected_items:
        st.warning("يرجى اختيار قطعة واحدة على الأقل.")
    else:
        for item in selected_items:
            st.markdown(f"### 🔹 {item}")
            st.components.v1.html(f"""
                <model-viewer src="{models[item]}" alt="{item}" auto-rotate camera-controls ar 
                style='width: 100%; height: 400px; background: #f0f0f0;'></model-viewer>
                <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
            """, height=420)
            st.markdown("---")
