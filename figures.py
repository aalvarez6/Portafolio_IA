"""
Figuras del sitio, generadas como SVG inline.

Inline y no PNG: pesa poco, no agrega una petición al servidor, escala sin
pixelarse y hereda los colores del tema vía variables CSS. Nada de eso lo
da una imagen exportada.
"""

from __future__ import annotations

import math


def curva_de_carga(width: int = 1080, height: int = 240) -> str:
    """
    Curva de demanda diaria contra generación solar, y la carga neta que
    resulta de restarlas. Es el gráfico que define el problema de operar
    una red con renovables: el hueco del mediodía y la rampa del atardecer.

    Determinística: no cambia entre recargas.
    """
    pad_y = 24
    h = height - 2 * pad_y
    pasos = 96  # 15 minutos por paso

    def demanda(t: float) -> float:
        """Dos picos: mañana y noche. t en [0,1] equivale a 24 horas."""
        manana = math.exp(-(((t - 0.32) * 6.5) ** 2)) * 0.55
        noche = math.exp(-(((t - 0.79) * 5.0) ** 2)) * 0.92
        return 0.34 + manana + noche

    def solar(t: float) -> float:
        """Campana diurna, cero fuera de las horas de sol."""
        if t < 0.26 or t > 0.76:
            return 0.0
        return math.sin((t - 0.26) / 0.50 * math.pi) ** 1.4 * 0.78

    def a_puntos(fn) -> list[tuple[float, float]]:
        pts = []
        for i in range(pasos + 1):
            t = i / pasos
            y = pad_y + h * (1 - fn(t) / 1.55)
            pts.append((t * width, max(pad_y, min(height - pad_y, y))))
        return pts

    def to_d(pts: list[tuple[float, float]]) -> str:
        return f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(
            f"L {x:.1f} {y:.1f}" for x, y in pts[1:]
        )

    dem = a_puntos(demanda)
    neta = a_puntos(lambda t: demanda(t) - solar(t))

    # El área entre demanda y carga neta es la energía solar que la red no
    # tuvo que despachar. Por eso se sombrea: es la única parte del gráfico
    # que carga un significado, no una decoración.
    area = (
        to_d(dem)
        + " L "
        + " L ".join(f"{x:.1f} {y:.1f}" for x, y in reversed(neta))
        + " Z"
    )

    return f"""
<svg viewBox="0 0 {width} {height}" width="100%" height="{height}"
     role="img" aria-label="Curva de demanda diaria, generacion solar y
     carga neta resultante a lo largo de 24 horas"
     xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
  <path d="{area}" fill="var(--accent)" fill-opacity="0.10"/>
  <path d="{to_d(dem)}" fill="none" stroke="var(--ink-faint)"
        stroke-width="1.2" stroke-dasharray="3 4" stroke-linecap="round"/>
  <path d="{to_d(neta)}" fill="none" stroke="var(--ink)"
        stroke-width="1.8" stroke-linecap="round"/>
</svg>
""".strip()


def ensemble_fan(
    width: int = 1080, height: int = 260, members: int = 16, seed: int = 7
) -> str:
    """Abanico de ensamble. Se conserva por si alguna vista lo necesita."""
    import random

    rng = random.Random(seed)
    pad_y = 26
    usable_h = height - 2 * pad_y
    steps = 60

    def trend(t: float) -> float:
        return math.sin(t * math.pi * 1.15 - 0.4) * 0.26 + math.sin(t * 5.1) * 0.04

    paths = []
    for _ in range(members):
        drift, pts = 0.0, []
        for i in range(steps + 1):
            t = i / steps
            drift += rng.gauss(0, 0.03)
            value = trend(t) + drift * (t ** 1.6) * 2.4
            y = pad_y + usable_h * (0.5 - value * 0.5)
            pts.append((t * width, max(pad_y, min(height - pad_y, y))))
        paths.append(pts)

    def to_d(pts):
        return f"M {pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(
            f"L {x:.1f} {y:.1f}" for x, y in pts[1:]
        )

    miembros = "".join(
        f'<path d="{to_d(p)}" fill="none" stroke="var(--accent)" '
        f'stroke-width="1" stroke-opacity="0.30" stroke-linecap="round"/>'
        for p in paths
    )
    xs = [p[0] for p in paths[0]]
    media = [(xs[i], sum(p[i][1] for p in paths) / members) for i in range(steps + 1)]

    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" '
        f'role="img" aria-label="Trayectorias de un ensamble que divergen" '
        f'xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">'
        f'{miembros}<path d="{to_d(media)}" fill="none" stroke="var(--ink)" '
        f'stroke-width="1.6" stroke-linecap="round"/></svg>'
    )
