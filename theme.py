"""
Sistema de diseño del portafolio.

Un solo punto de verdad para color, tipografía y ritmo vertical.
Los componentes devuelven/renderizan HTML en bloques completos: Streamlit
envuelve cada llamada a `st.markdown` en su propio div, así que construir
una grilla requiere emitirla en UNA sola inyección, no card por card.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

import streamlit as st

# --------------------------------------------------------------------------
# Tokens
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Tokens:
    """Paleta y escala. Cambiar aquí propaga a todo el sitio."""

    # Superficies
    bg: str = "#FBFBFD"          # blanco atmosférico, no blanco puro
    surface: str = "#FFFFFF"
    hairline: str = "rgba(0,0,0,0.09)"

    # Tinta
    ink: str = "#1D1D1F"         # texto principal
    ink_soft: str = "#6E7278"    # secundario, ratio 4.7:1 sobre bg
    ink_faint: str = "#9A9DA3"   # metadatos

    # Acento — azul profundo de sondeo atmosférico
    accent: str = "#0B63CE"
    accent_ink: str = "#FFFFFF"
    accent_wash: str = "rgba(11,99,206,0.08)"

    # Rampa de datos (usar en Plotly/Matplotlib para que las figuras
    # pertenezcan a la página en vez de traer sus propios colores)
    ramp: tuple[str, ...] = ("#0B63CE", "#3E8FD9", "#7FB8E6", "#C2571F", "#1D1D1F")

    # Ritmo
    measure: str = "1080px"      # ancho de contenido
    text_measure: str = "68ch"   # longitud de línea legible

    radius: str = "14px"
    radius_sm: str = "10px"


LIGHT = Tokens()


# --------------------------------------------------------------------------
# CSS base
# --------------------------------------------------------------------------


def _css(t: Tokens) -> str:
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

:root {{
  --bg: {t.bg};
  --surface: {t.surface};
  --hairline: {t.hairline};
  --ink: {t.ink};
  --ink-soft: {t.ink_soft};
  --ink-faint: {t.ink_faint};
  --accent: {t.accent};
  --accent-ink: {t.accent_ink};
  --accent-wash: {t.accent_wash};
  --radius: {t.radius};
  --radius-sm: {t.radius_sm};
  --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter",
          "Segoe UI", Roboto, sans-serif;
}}

/* --- 1. Quitar el chrome de Streamlit -------------------------------- */
/* Estos selectores dependen de la versión: por eso requirements.txt fija
   streamlit==1.63.0. Verificados contra esa versión; stDecoration ya no
   existe pero se deja por compatibilidad hacia atrás. Al actualizar
   Streamlit, revisar esta sección primero. */
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu,
footer {{ display: none !important; }}

[data-testid="stAppViewContainer"] {{ background: var(--bg); }}

[data-testid="stMainBlockContainer"],
.block-container {{
  max-width: {t.measure};
  padding: 0 24px 96px;
}}

/* --- 2. Tipografía ---------------------------------------------------- */
html, body, [data-testid="stAppViewContainer"] * {{
  font-family: var(--font);
  -webkit-font-smoothing: antialiased;
}}

body {{ color: var(--ink); }}

/* Escala: 1.333 (cuarta justa), tracking negativo en los tamaños grandes.
   Ese apretado óptico es la firma real del estilo Apple, más que el color. */
h1, .display {{
  font-size: clamp(2.6rem, 6vw, 4.2rem);
  font-weight: 600;
  letter-spacing: -0.033em;
  line-height: 1.06;
  margin: 0;
}}
h2 {{
  font-size: clamp(1.7rem, 3.2vw, 2.35rem);
  font-weight: 600;
  letter-spacing: -0.022em;
  line-height: 1.18;
  margin: 0 0 8px;
}}
h3 {{
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -0.011em;
  margin: 0;
}}
p, li, [data-testid="stMarkdownContainer"] p {{
  font-size: 1.0625rem;
  line-height: 1.62;
  color: var(--ink-soft);
  max-width: {t.text_measure};
}}

/* --- 3. Ritmo vertical ------------------------------------------------ */
.band {{ padding: 104px 0 0; }}
.band--first {{ padding-top: 72px; }}
.band__intro {{ margin-bottom: 40px; }}
@media (max-width: 720px) {{
  .band {{ padding-top: 64px; }}
  [data-testid="stMainBlockContainer"], .block-container {{ padding: 0 20px 64px; }}
}}

/* --- 4. Barra de navegación ------------------------------------------ */
.nav {{
  position: sticky; top: 0; z-index: 90;
  display: flex; align-items: center; gap: 28px;
  padding: 14px 0 13px;
  margin-bottom: 8px;
  border-bottom: 1px solid var(--hairline);
  background: rgba(251,251,253,0.82);
  backdrop-filter: saturate(180%) blur(18px);
  -webkit-backdrop-filter: saturate(180%) blur(18px);
}}
.nav__mark {{
  font-size: 0.95rem; font-weight: 600; color: var(--ink);
  letter-spacing: -0.01em; margin-right: auto; text-decoration: none;
}}
.nav a:not(.nav__mark) {{
  font-size: 0.875rem; color: var(--ink-soft); text-decoration: none;
  transition: color .18s ease;
}}
.nav a:hover {{ color: var(--ink); }}
@media (max-width: 560px) {{ .nav {{ gap: 18px; }} .nav a:not(.nav__mark) {{ font-size: .8rem; }} }}

/* --- 5. Hero ---------------------------------------------------------- */
.hero {{ padding: 88px 0 24px; text-align: center; }}
.hero p {{
  margin: 22px auto 0;
  font-size: 1.28rem; line-height: 1.5; color: var(--ink-soft);
  max-width: 58ch;
}}
.hero__figure {{ margin: 56px 0 0; }}
.hero__caption {{
  margin-top: 14px; font-size: .8125rem; color: var(--ink-faint);
  text-align: center; max-width: none;
}}

/* Un solo momento de movimiento: la entrada del hero al cargar. */
.hero > * {{ animation: rise .7s cubic-bezier(.16,.84,.44,1) backwards; }}
.hero > *:nth-child(2) {{ animation-delay: .08s; }}
.hero > *:nth-child(3) {{ animation-delay: .16s; }}
.hero > *:nth-child(4) {{ animation-delay: .24s; }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(14px); }} }}
@media (prefers-reduced-motion: reduce) {{
  .hero > * {{ animation: none; }}
  * {{ transition: none !important; }}
}}

/* Línea de stack bajo el lead: un solo renglón, separadores medios.
   Comunica alcance sin convertirse en nube de etiquetas. */
.hero__stack {{
  margin: 26px auto 0; font-size: .875rem; color: var(--ink-faint);
  letter-spacing: .01em;
}}

/* --- 5b. Capacidades --------------------------------------------------- */
/* Agrupadas por función, no en lista plana: el agrupamiento es la
   información. Una fila de etiquetas sueltas no dice nada del criterio. */
.caps {{ display: grid; gap: 0; border-top: 1px solid var(--hairline); }}
.caps__row {{
  display: grid; grid-template-columns: 180px 1fr; gap: 24px;
  padding: 18px 2px; border-bottom: 1px solid var(--hairline);
}}
.caps__label {{ font-size: .875rem; color: var(--ink-faint); }}
.caps__items {{ font-size: .96rem; color: var(--ink); }}
@media (max-width: 620px) {{
  .caps__row {{ grid-template-columns: 1fr; gap: 4px; }}
}}

/* --- 6. Tarjetas de proyecto ------------------------------------------ */
.grid {{
  display: grid; gap: 18px;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
}}
.card {{
  display: flex; flex-direction: column;
  background: var(--surface);
  border: 1px solid var(--hairline);
  border-radius: var(--radius);
  padding: 26px 26px 22px;
  text-decoration: none;
  transition: border-color .2s ease;
}}
.card:hover {{ border-color: rgba(11,99,206,0.45); }}
.card:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 3px; }}
.card h3 {{ color: var(--ink); }}
.card__lead {{
  margin: 10px 0 20px; font-size: .96rem; line-height: 1.55;
  color: var(--ink-soft); flex: 1;
}}
/* Los metadatos son información técnica real (modelo, dato, dominio),
   no decoración: por eso van en tabla de definición y no en píldoras. */
.card__meta {{
  display: grid; grid-template-columns: auto 1fr; gap: 4px 16px;
  border-top: 1px solid var(--hairline); padding-top: 16px;
  font-size: .8125rem;
}}
.card__meta dt {{ color: var(--ink-faint); }}
.card__meta dd {{ margin: 0; color: var(--ink); }}
.card__live {{
  display: inline-flex; align-items: center; gap: 7px;
  margin-top: 18px; font-size: .8125rem; font-weight: 500; color: var(--accent);
}}
.card__live::before {{
  content: ""; width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent);
}}

/* --- 7. Widgets de Streamlit ------------------------------------------ */
.stButton > button, .stLinkButton a, .stDownloadButton > button {{
  border-radius: 980px !important;           /* píldora */
  border: 1px solid transparent !important;
  background: var(--accent) !important;
  color: var(--accent-ink) !important;
  font-size: .9375rem !important;
  font-weight: 500 !important;
  padding: 9px 22px !important;
  box-shadow: none !important;
  transition: filter .18s ease;
}}
.stButton > button:hover, .stLinkButton a:hover {{ filter: brightness(1.08); }}
.stButton > button[kind="secondary"] {{
  background: transparent !important;
  color: var(--accent) !important;
  border-color: var(--hairline) !important;
}}

[data-testid="stSidebar"] {{
  background: var(--surface);
  border-right: 1px solid var(--hairline);
}}

[data-baseweb="select"] > div, .stTextInput input, .stNumberInput input {{
  border-radius: var(--radius-sm) !important;
  border-color: var(--hairline) !important;
  background: var(--surface) !important;
}}

[data-testid="stMetric"] {{
  background: var(--surface);
  border: 1px solid var(--hairline);
  border-radius: var(--radius-sm);
  padding: 16px 18px;
}}
[data-testid="stMetricLabel"] p {{ font-size: .8125rem !important; color: var(--ink-faint) !important; }}
[data-testid="stMetricValue"] {{ font-weight: 600; letter-spacing: -0.02em; }}

hr, [data-testid="stMarkdownContainer"] hr {{
  border: 0; border-top: 1px solid var(--hairline); margin: 0;
}}

/* --- 7b. Índice compacto -------------------------------------------- */
/* Segundo nivel de jerarquía: enlaces, no tarjetas. El peso visual
   comunica la diferencia entre trabajo destacado y exploración. */
.indice {{
  display: grid; gap: 0;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  border-top: 1px solid var(--hairline);
}}
.indice a {{
  display: flex; align-items: baseline; gap: 12px;
  padding: 15px 4px;
  border-bottom: 1px solid var(--hairline);
  text-decoration: none;
  transition: padding-left .18s ease;
}}
.indice a:hover {{ padding-left: 10px; }}
.indice__nombre {{ font-size: .96rem; font-weight: 500; color: var(--ink); }}
.indice__que {{ font-size: .84rem; color: var(--ink-faint); margin-left: auto;
               text-align: right; }}
@media (max-width: 560px) {{ .indice__que {{ display: none; }} }}

/* --- 8. Pie ----------------------------------------------------------- */
.foot {{
  margin-top: 104px; padding-top: 28px;
  border-top: 1px solid var(--hairline);
  display: flex; flex-wrap: wrap; gap: 20px; align-items: baseline;
  font-size: .8125rem; color: var(--ink-faint);
}}
.foot a {{ color: var(--ink-soft); text-decoration: none; }}
.foot a:hover {{ color: var(--accent); }}
.foot__spacer {{ margin-left: auto; }}

:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
</style>
"""


def apply_theme(tokens: Tokens = LIGHT) -> None:
    """Inyecta el sistema de diseño. Llamar una vez por página, al inicio."""
    st.html(_css(tokens))


# --------------------------------------------------------------------------
# Componentes
# --------------------------------------------------------------------------


def nav(mark: str, links: dict[str, str]) -> None:
    """Barra superior fija. `links` es {etiqueta: href}."""
    items = "".join(
        f'<a href="{escape(href)}">{escape(label)}</a>' for label, href in links.items()
    )
    st.html(f'<nav class="nav"><a class="nav__mark" href="/">{escape(mark)}</a>{items}</nav>')


def hero(
    title: str,
    lead: str,
    stack: str = "",
    figure_svg: str = "",
    caption: str = "",
) -> None:
    """Encabezado de portada. `figure_svg` debe ser SVG inline, no imagen."""
    fig = (
        f'<div class="hero__figure">{figure_svg}'
        f'<p class="hero__caption">{escape(caption)}</p></div>'
        if figure_svg
        else ""
    )
    stack_html = f'<p class="hero__stack">{escape(stack)}</p>' if stack else ""
    st.html(
        f'<header class="hero"><h1>{escape(title)}</h1>'
        f"<p>{escape(lead)}</p>{stack_html}{fig}</header>"
    )


def band(title: str, lead: str = "", first: bool = False) -> None:
    """Abre una sección con su encabezado y ritmo vertical."""
    cls = "band band--first" if first else "band"
    lead_html = f"<p>{escape(lead)}</p>" if lead else ""
    anchor = title.lower().replace(" ", "-")
    st.html(
        f'<section class="{cls}" id="{escape(anchor)}">'
        f'<div class="band__intro"><h2>{escape(title)}</h2>{lead_html}</div></section>'
    )


def project_grid(projects: list[dict]) -> None:
    """
    Grilla de herramientas. Se emite en una sola inyección para que el CSS
    Grid funcione: si cada tarjeta fuera un `st.html` aparte, Streamlit las
    separaría en contenedores distintos y la grilla se rompería.

    Cada entrada acepta: title, lead, href, meta (dict) y, opcional,
    `externa=True` para abrir en pestaña nueva.
    """
    cards = []
    for p in projects:
        meta = "".join(
            f"<dt>{escape(k)}</dt><dd>{escape(v)}</dd>" for k, v in p["meta"].items()
        )
        live = '<span class="card__live">Abrir herramienta</span>' if p.get("live") else ""
        # rel="noopener" es obligatorio con target="_blank": sin eso la
        # pestaña destino puede manipular la de origen vía window.opener.
        destino = (
            ' target="_blank" rel="noopener noreferrer"' if p.get("externa") else ""
        )
        cards.append(
            f'<a class="card" href="{escape(p["href"])}"{destino}>'
            f'<h3>{escape(p["title"])}</h3>'
            f'<p class="card__lead">{escape(p["lead"])}</p>'
            f'<dl class="card__meta">{meta}</dl>{live}</a>'
        )
    st.html(f'<div class="grid">{"".join(cards)}</div>')


def capabilities(groups: dict[str, list[str]]) -> None:
    """Capacidades agrupadas por función. `groups` es {etiqueta: [items]}."""
    filas = "".join(
        f'<div class="caps__row"><div class="caps__label">{escape(label)}</div>'
        f'<div class="caps__items">{escape(" · ".join(items))}</div></div>'
        for label, items in groups.items()
    )
    st.html(f'<div class="caps">{filas}</div>')


def link_list(items: list[dict]) -> None:
    """
    Índice compacto de herramientas secundarias. Una sola inyección, por la
    misma razón que project_grid: el CSS Grid necesita un contenedor único.
    """
    filas = "".join(
        f'<a href="{escape(i["href"])}" target="_blank" rel="noopener noreferrer">'
        f'<span class="indice__nombre">{escape(i["title"])}</span>'
        f'<span class="indice__que">{escape(i.get("que", ""))}</span></a>'
        for i in items
    )
    st.html(f'<div class="indice">{filas}</div>')


def footer(name: str, note: str, links: dict[str, str]) -> None:
    items = "".join(
        f'<a href="{escape(href)}">{escape(label)}</a>' for label, href in links.items()
    )
    st.html(
        f'<footer class="foot"><span>{escape(name)}</span>'
        f'<span>{escape(note)}</span><span class="foot__spacer"></span>{items}</footer>'
    )


def plotly_layout(tokens: Tokens = LIGHT) -> dict:
    """
    Layout para que las figuras hereden la página en vez de traer el tema
    por defecto de Plotly. Uso: `fig.update_layout(**plotly_layout())`.
    """
    return {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Inter, -apple-system, sans-serif", "size": 13,
                 "color": tokens.ink_soft},
        "colorway": list(tokens.ramp),
        "margin": {"l": 56, "r": 24, "t": 32, "b": 48},
        "xaxis": {"gridcolor": tokens.hairline, "zeroline": False,
                  "linecolor": tokens.hairline},
        "yaxis": {"gridcolor": tokens.hairline, "zeroline": False,
                  "linecolor": tokens.hairline},
        "legend": {"orientation": "h", "y": -0.22, "x": 0},
        "hoverlabel": {"bgcolor": tokens.surface, "font_size": 12},
    }
