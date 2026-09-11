"""Portada: hero, proyectos, métodos, pie."""

import streamlit as st

import content
import theme
from figures import ensemble_fan

theme.apply_theme()
theme.nav(content.PERFIL["nombre"], content.NAV)

theme.hero(
    title=content.PERFIL["titular"],
    lead=content.PERFIL["lead"],
    figure_svg=ensemble_fan(),
    caption=content.PERFIL["pie_figura"],
)

theme.band(
    "Proyectos",
    "Tres sistemas en producción. Todos se pueden ejecutar desde aquí.",
)
theme.project_grid(content.PROYECTOS)

theme.band("Métodos", content.METODOS["lead"])
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
