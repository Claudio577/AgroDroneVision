import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="AgroDrone Vision", layout="wide")
st.title("🌾 AgroDrone Vision — NDVI Viewer")

st.markdown("Mapa NDVI gerado com imagens Sentinel-2 (GEE + Colab)")

# Criar mapa base
m = folium.Map(location=[-23.55, -51.25], zoom_start=13)
folium.TileLayer('CartoDB positron').add_to(m)
st_folium(m, width=800, height=600)
