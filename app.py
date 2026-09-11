"""
Entrypoint. `position="hidden"` desactiva la navegación lateral de
Streamlit: la barra superior propia (theme.nav) es la que manda.
"""

import streamlit as st

st.set_page_config(
    page_title="Valeria · Pronóstico atmosférico",
    page_icon="◔",
    layout="wide",                    # el ancho real lo fija el CSS, no Streamlit
    initial_sidebar_state="collapsed",
)

paginas = [
    st.Page("pages/inicio.py", title="Inicio", url_path="inicio", default=True),
    st.Page("pages/ensamble.py", title="Ensamble WRF", url_path="ensamble"),
]

st.navigation(paginas, position="hidden").run()
