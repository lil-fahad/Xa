import streamlit as st
import json

# روابط افتراضية لنماذج 3D – يمكن ربطها بـ AR Viewer حقيقي مثل WebXR لاحقًا
models = {
    "كنبة": "https://example.com/models/sofa.glb",
    "سرير": "https://example.com/models/bed.glb",
    "طاولة": "https://example.com/models/table.glb",
    "كراسي": "https://example.com/models/chair.glb",
    "مكتب": "https://example.com/models/desk.glb",
    "دولاب": "https://example.com/models/closet.glb",
    "مرآة": "https://example.com/models/mirror.glb"
}

# إعداد واجهة Streamlit
st.set_page_config(page_title="AR Furniture Viewer", layout="centered")
st.title("🪑 عرض الأثاث بالواقع المعزز")

# اختيار نوع الغرفة
room_type = st.selectbox("اختر نوع الغرفة:", [
    "غرفة نوم", "غرفة معيشة", "مكتب", "غرفة طعام", "شرفة خارجية"
])

# اختيار قطع الأثاث
selected_items = st.multiselect("اختر القطع لعرضها بالـ AR:", list(models.keys()))

# زر التنفيذ
if st.button("عرض"):
    if not selected_items:
        st.warning("يرجى اختيار قطعة واحدة على الأقل.")
    else:
        st.success("روابط العرض الثلاثي الأبعاد:")
        for item in selected_items:
            st.markdown(f"🔹 **{item}**")
            st.markdown(f"[👓 عرض بتقنية AR]({models[item]})", unsafe_allow_html=True)
            st.markdown("---")
