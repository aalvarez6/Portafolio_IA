# Portafolio — Streamlit con sistema de diseño propio

## Correr en local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Estructura
```
app.py          entrypoint y navegación (st.navigation, sidebar desactivada)
theme.py        sistema de diseño: tokens, CSS y componentes
figures.py      SVG del hero, generado determinísticamente
content.py      textos y proyectos — edita aquí, no en las páginas
pages/          una página por demo
.streamlit/     tokens base para evitar el flash del tema por defecto
```

## Agregar una demo
1. Crea `pages/mi_demo.py` y empieza con:
   ```python
   import content, theme
   theme.apply_theme()
   theme.nav(content.PERFIL["nombre"], content.NAV)
   ```
2. En las figuras de Plotly: `fig.update_layout(**theme.plotly_layout())`.
3. Registra la página en la lista `paginas` de `app.py`.
4. Agrégala a `PROYECTOS` en `content.py` con su `href`.

## Antes de publicar
- Reemplaza los enlaces de `content.PIE` y el correo de `content.NAV`.
- Sustituye los datos sintéticos de `pages/ensamble.py` por salidas reales.
- Revisa que cada proyecto declare sus fuentes de datos y su validación.

## Nota de mantenimiento
El CSS depende de atributos `data-testid` de Streamlit, que cambian entre
versiones. Por eso `requirements.txt` fija `streamlit==1.63.0`. Si actualizas,
revisa la sección 1 de `theme.py` antes que nada.
