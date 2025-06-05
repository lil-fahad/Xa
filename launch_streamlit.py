import subprocess
import os

print("🚀 Launching Streamlit app from ar_module...")
os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
subprocess.run(["streamlit", "run", "ar_module/streamlit_ar_app.py"])
