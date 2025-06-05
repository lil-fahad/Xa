import streamlit as st
from PIL import Image
from planner.analyze_plan import process_plan_image

st.set_page_config(page_title="تحليل مخطط البيت", layout="centered")
st.title("📐 تحليل مخطط البيت واقتراح أثاث ذكي")

uploaded_image = st.file_uploader("📷 ارفع صورة مخطط البيت (PNG أو JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="مخطط البيت", use_column_width=True)

    if st.button("ابدأ التحليل"):
        with st.spinner("يتم تحليل المخطط..."):
            img_bytes = uploaded_image.read()
            result = process_plan_image(img_bytes)

        st.success("✅ تم التحليل بنجاح!")
        for room, info in result.items():
            st.markdown(f"### 🛋 {room}")
            st.markdown(f"**📏 الأبعاد التقريبية:** {info['dimensions']}")
            st.markdown(f"**🪑 الأثاث المقترح:**")
            for item in info["suggested_items"]:
                st.markdown(f"- {item}")
            st.markdown("---")
