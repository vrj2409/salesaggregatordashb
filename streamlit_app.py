import streamlit as st
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

# Read the HTML file
index_path = Path(__file__).parent / "dist" / "index.html"

if index_path.exists():
    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Display the dashboard
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.error(f"Dashboard not found. Please ensure the dist folder exists with index.html")
