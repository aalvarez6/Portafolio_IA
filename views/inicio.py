"""Portada."""

import streamlit as st

import content
import theme
from figures import curva_de_carga

theme.apply_theme()
theme.nav(content.PERFIL["nombre"], content.NAV)

theme.hero(
    title=content.PERFIL["titular"],
    lead=content.PERFIL["lead"],
    stack=content.PERFIL["stack"],
    figure_svg=curva_de_carga(),
    caption=content.PERFIL["pie_figura"],
)

theme.band(
    "Featured projects",
    "Three systems, each solving a different problem. All deployed, open "
    "and usable right now.",
)
theme.project_grid(content.DESTACADAS)

theme.band(
    "Capabilities",
    "Grouped by what they are for, not listed as keywords.",
)
theme.capabilities(content.CAPACIDADES)

if content.OTRAS:
    # Tercer nivel de jerarquía: enlaces sin tarjeta. Mantiene visible la
    # amplitud sin que compita con los tres proyectos destacados.
    st.html(
        "<h3 style='margin:96px 0 4px'>More work</h3>"
        "<p style='font-size:.94rem;margin:0 0 20px'>"
        "Smaller explorations across the applied AI ecosystem.</p>"
    )
    theme.link_list(content.OTRAS)

theme.footer(
    name=content.PERFIL["nombre"],
    note=content.PIE["nota"],
    links=content.PIE["links"],
)
