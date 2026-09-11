"""
Demo de ejemplo. Sirve de plantilla: cualquier app tuya se vuelve parte del
portafolio con las tres primeras líneas (tema + nav) y `plotly_layout()`.

Los datos aquí son sintéticos y así está rotulado en la página. Reemplaza
`simular_ensamble` por tu salida real de WRF antes de publicar.
"""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

import content
import theme

theme.apply_theme()
theme.nav(content.PERFIL["nombre"], content.NAV)

theme.band(
    "Sensibilidad de ensambles WRF",
    "La dispersión entre miembros crece con el horizonte de pronóstico. "
    "Ese crecimiento es la incertidumbre que un pronóstico determinista oculta.",
    first=True,
)


@st.cache_data
def simular_ensamble(miembros: int, horas: int, amplitud: float, semilla: int = 3):
    """
    Sustituto sintético de una corrida de ensamble.

    Cacheado porque el patrón importa: cuando aquí vaya tu WRF real, el
    cache evita releer NetCDF en cada interacción del usuario.
    """
    rng = np.random.default_rng(semilla)
    t = np.arange(horas)
    señal = 3.2 * np.exp(-((t - 14) ** 2) / 40) + 0.8 * np.exp(-((t - 33) ** 2) / 70)
    ruido = rng.normal(0, amplitud, size=(miembros, horas)).cumsum(axis=1)
    crecimiento = (t / horas) ** 1.5
    return t, np.clip(señal + ruido * crecimiento, 0, None)


c1, c2, c3 = st.columns([1, 1, 1], gap="medium")
miembros = c1.slider("Miembros del ensamble", 4, 40, 16)
horas = c2.slider("Horizonte (horas)", 12, 72, 48, step=6)
amplitud = c3.slider("Perturbación inicial", 0.02, 0.30, 0.12, step=0.02)

t, miembros_arr = simular_ensamble(miembros, horas, amplitud)
media = miembros_arr.mean(axis=0)
p10, p90 = np.percentile(miembros_arr, [10, 90], axis=0)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=np.concatenate([t, t[::-1]]),
    y=np.concatenate([p90, p10[::-1]]),
    fill="toself", fillcolor="rgba(11,99,206,0.10)",
    line={"width": 0}, hoverinfo="skip", name="Rango 10–90 %",
))
for m in miembros_arr:
    fig.add_trace(go.Scatter(
        x=t, y=m, mode="lines", showlegend=False, hoverinfo="skip",
        line={"width": 1, "color": "rgba(11,99,206,0.28)"},
    ))
fig.add_trace(go.Scatter(
    x=t, y=media, mode="lines", name="Media del ensamble",
    line={"width": 2.2, "color": "#1D1D1F"},
))
fig.update_layout(height=420, **theme.plotly_layout())
fig.update_xaxes(title_text="Horas desde la inicialización")
fig.update_yaxes(title_text="Precipitación (mm/h)")

st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

m1, m2, m3 = st.columns(3, gap="medium")
m1.metric("Dispersión a 24 h", f"{(p90 - p10)[min(24, horas - 1)]:.2f} mm/h")
m2.metric("Dispersión al final", f"{(p90 - p10)[-1]:.2f} mm/h")
m3.metric("Pico de la media", f"{media.max():.2f} mm/h")

st.html(
    "<p style='font-size:.8125rem;color:var(--ink-faint);margin-top:20px'>"
    "Datos sintéticos, para demostrar la interfaz. La versión con salidas "
    "reales de WRF y validación contra la red SIATA está en preparación.</p>"
)

theme.footer(content.PERFIL["nombre"], content.PIE["nota"], content.PIE["links"])
