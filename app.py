"""
Entrypoint del portafolio.

Las rutas se resuelven contra la ubicación de ESTE archivo, no contra el
directorio de trabajo. En local suelen coincidir; en Streamlit Cloud no
siempre, y ahí aparece StreamlitPageNotFoundError.
"""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Alejandra Álvarez · Ingeniería eléctrica e IA",
    page_icon="◔",
    layout="wide",                    # el ancho real lo fija el CSS, no Streamlit
    initial_sidebar_state="collapsed",
)

RAIZ = Path(__file__).parent

# Carpeta "views" y no "pages": Streamlit trata `pages/` como directorio
# mágico de multipágina automática, que compite con st.navigation.
VISTAS = RAIZ / "views"

DEFINICION = [
    ("inicio.py", "Inicio", "inicio", True),
]

faltantes = [f for f, *_ in DEFINICION if not (VISTAS / f).is_file()]

if faltantes:
    # Falla ruidosa y útil: en la nube no hay terminal para hacer `ls`,
    # así que la app misma reporta qué llegó al repo.
    st.error(f"No se encontraron estas vistas: {', '.join(faltantes)}")
    encontrados = sorted(p.name for p in VISTAS.glob("*.py")) if VISTAS.is_dir() else []
    st.write(f"Buscando en: `{VISTAS}`")
    st.write("Archivos presentes:", encontrados or "la carpeta no existe")
    st.write("Contenido de la raíz:", sorted(p.name for p in RAIZ.iterdir()))
    st.stop()

paginas = [
    st.Page(VISTAS / archivo, title=titulo, url_path=url, default=por_defecto)
    for archivo, titulo, url, por_defecto in DEFINICION
]

st.navigation(paginas, position="hidden").run()
