"""
Figuras decorativas del sitio, generadas como SVG inline.

Inline y no PNG por tres razones: pesa ~18 kB sin petición extra al servidor,
escala sin pixelarse y hereda
los colores del tema vía variables CSS. Nada de esto lo da una imagen
exportada.
"""

from __future__ import annotations

import math
import random


def ensemble_fan(
    width: int = 1080,
    height: int = 260,
    members: int = 16,
    seed: int = 7,
) -> str:
    """
    Abanico de ensamble: trayectorias que parten de una condición inicial
    común y divergen con el tiempo. Es la imagen exacta del problema de
    pronóstico probabilístico, así que funciona como portada en lugar de
    un gráfico genérico.

    Determinística por `seed`: el hero no cambia entre recargas.
    """
    rng = random.Random(seed)
    pad_x, pad_y = 0, 26
    usable_h = height - 2 * pad_y
    steps = 60

    def trend(t: float) -> float:
        """Señal común: un ciclo suave sobre el que crece la dispersión."""
        return math.sin(t * math.pi * 1.15 - 0.4) * 0.26 + math.sin(t * 5.1) * 0.04

    paths: list[list[tuple[float, float]]] = []
    for _ in range(members):
        drift = 0.0
        pts: list[tuple[float, float]] = []
        for i in range(steps + 1):
            t = i / steps
            # El error crece con el horizonte: t**1.6 aproxima el
            # crecimiento de la dispersión en un ensamble de corto plazo.
            drift += rng.gauss(0, 0.03)
            value = trend(t) + drift * (t ** 1.6) * 2.4
            x = pad_x + t * (width - 2 * pad_x)
            y = pad_y + usable_h * (0.5 - value * 0.5)
            pts.append((x, max(pad_y, min(height - pad_y, y))))
        paths.append(pts)

    def to_d(pts: list[tuple[float, float]]) -> str:
        head = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
        rest = " ".join(f"L {x:.1f} {y:.1f}" for x, y in pts[1:])
        return f"{head} {rest}"

    # Envolvente: mínimo y máximo del ensamble en cada paso.
    upper = [min(p[i][1] for p in paths) for i in range(steps + 1)]
    lower = [max(p[i][1] for p in paths) for i in range(steps + 1)]
    xs = [p[0] for p in paths[0]]
    envelope = (
        "M "
        + " L ".join(f"{x:.1f} {y:.1f}" for x, y in zip(xs, upper))
        + " L "
        + " L ".join(f"{x:.1f} {y:.1f}" for x, y in zip(reversed(xs), reversed(lower)))
        + " Z"
    )

    members_svg = "".join(
        f'<path d="{to_d(p)}" fill="none" stroke="var(--accent)" '
        f'stroke-width="1" stroke-opacity="0.30" stroke-linecap="round"/>'
        for p in paths
    )

    # La media del ensamble es la única línea con peso: es la que se lee.
    mean_pts = [
        (xs[i], sum(p[i][1] for p in paths) / members) for i in range(steps + 1)
    ]

    return f"""
<svg viewBox="0 0 {width} {height}" width="100%" height="{height}"
     role="img" aria-label="Trayectorias de un ensamble de pronóstico que
     divergen a medida que aumenta el horizonte temporal"
     xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
  <path d="{envelope}" fill="var(--accent)" fill-opacity="0.07"/>
  {members_svg}
  <path d="{to_d(mean_pts)}" fill="none" stroke="var(--ink)"
        stroke-width="1.6" stroke-linecap="round"/>
</svg>
""".strip()
