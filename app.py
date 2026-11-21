"""Publicación de la herramienta interactiva de la Escuela EPI.

El contenido original se conserva en static/escuela.html.
"""
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "static" / "escuela.html"

st.set_page_config(
    page_title="Feminismo de Datos e Indicadores Cotidianos de Paz",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """<style>
    .block-container { max-width: 100%; padding-top: 1rem; padding-bottom: 1rem; }
    </style>""",
    unsafe_allow_html=True,
)

if not HTML_FILE.is_file():
    st.error("No se encontró el archivo static/escuela.html.")
    st.stop()

st.markdown(
    '**Escuela de Feminismo de Datos e Indicadores Cotidianos de Paz**  '
    '· GIZ – FAST · Everyday Peace Indicators'
)
st.markdown(
    '<a href="/app/static/escuela.html" target="_blank" '
    'rel="noopener noreferrer">↗ Abrir herramienta en una pestaña completa</a>',
    unsafe_allow_html=True,
)
# Mantiene activo el JavaScript original dentro de un marco independiente.
# Altura fija: la barra de navegación sticky del HTML funciona al desplazarse.
st.iframe(
    HTML_FILE,
    height=800,
    width="stretch",
    alt="Herramienta interactiva de la Escuela de Feminismo de Datos e Indicadores Cotidianos de Paz",
)
