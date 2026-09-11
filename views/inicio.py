"""Portada: hero, herramientas en dos niveles, método, pie."""

import streamlit as st

import content
import theme
from figures import curva_de_carga

theme.apply_theme()
theme.nav(content.PERFIL["nombre"], content.NAV)

theme.hero(
    title=content.PERFIL["titular"],
    lead=content.PERFIL["lead"],
    figure_svg=curva_de_carga(),
    caption=content.PERFIL["pie_figura"],
)

theme.band(
    "Herramientas",
    "Cada una resuelve un problema distinto, tiene repositorio propio y "
    "está desplegada y abierta.",
)
theme.project_grid(content.DESTACADAS)

if content.OTRAS:
    # Segundo nivel: mismo contenido, menos peso visual. Evita que el
    # trabajo destacado compita con los experimentos.
    st.html(
        "<h3 style='margin:64px 0 4px'>Otras herramientas</h3>"
        "<p style='font-size:.94rem;margin:0 0 20px'>"
        "Exploraciones más acotadas del ecosistema de IA aplicada.</p>"
    )
    theme.link_list(content.OTRAS)

theme.band("Cómo trabajo", content.METODOS["lead"])
cols = st.columns(2, gap="large")
for i, (titulo, detalle) in enumerate(content.METODOS["items"]):
    with cols[i % 2]:
        st.html(
            f"<h3 style='margin-bottom:6px'>{titulo}</h3>"
            f"<p style='font-size:.96rem;margin:0 0 26px'>{detalle}</p>"
        )

theme.footer(
    name=content.PERFIL["nombre"],
    note=content.PIE["nota"],
    links=content.PIE["links"],
)
