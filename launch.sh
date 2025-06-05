
#!/bin/bash
# تشغيل FastAPI في الخلفية
uvicorn main:app --host 0.0.0.0 --port 8000 &

# تشغيل Streamlit في الواجهة الأمامية
streamlit run ar_module/streamlit_combined_viewer.py --server.port 8501 --server.address 0.0.0.0
