"""
Contenido del sitio. Separado de `theme.py` a propósito: aquí editas texto
y proyectos sin tocar una línea de CSS.

Los proyectos de abajo son un punto de partida basado en tu trabajo real.
Revisa cifras y alcance antes de publicar.
"""

PERFIL = {
    "nombre": "Valeria",
    "titular": "Pronóstico atmosférico, medido contra la realidad.",
    "lead": (
        "Ingeniera ambiental. Construyo y evalúo sistemas de pronóstico "
        "numérico para el Valle de Aburrá y la cuenca del Orinoco. "
        "Cada proyecto de esta página corre en vivo: puedes cambiar los "
        "parámetros y ver cómo responde el modelo."
    ),
    "pie_figura": (
        "Ensamble de pronóstico: 16 miembros que parten de condiciones "
        "iniciales perturbadas. La dispersión es la incertidumbre."
    ),
}

NAV = {
    "Proyectos": "#proyectos",
    "Métodos": "#métodos",
    "Contacto": "mailto:tu@correo.com",
}

PROYECTOS = [
    {
        "title": "Sensibilidad de ensambles WRF",
        "lead": (
            "Cuánto cambia el pronóstico de precipitación al perturbar las "
            "condiciones iniciales. Ajusta el número de miembros y el "
            "horizonte, y compara la dispersión contra lo observado."
        ),
        "meta": {
            "Modelo": "WRF, convección explícita",
            "Dominio": "Valle de Aburrá, 1 km",
            "Validación": "Red pluviométrica SIATA",
        },
        "href": "/ensamble",
        "live": True,
    },
    {
        "title": "Pronóstico probabilístico a 15 días",
        "lead": (
            "Pipeline que descarga el ensamble del ECMWF, calcula umbrales "
            "de excedencia y genera los mapas operativos para Antioquia."
        ),
        "meta": {
            "Fuente": "ECMWF IFS-ENS",
            "Frecuencia": "2 corridas diarias",
            "Salida": "Mapas y series por municipio",
        },
        "href": "/ecmwf",
        "live": True,
    },
    {
        "title": "Propagación de sequía en el Orinoco",
        "lead": (
            "Cómo una anomalía de precipitación se convierte en déficit de "
            "humedad del suelo y luego en caudal. Explora la cascada por "
            "subcuenca y escala temporal."
        ),
        "meta": {
            "Índices": "SPI, SSMI, SRI",
            "Periodo": "1981–2023",
            "Datos": "CHIRPS, GLEAM, ERA5",
        },
        "href": "/sequia",
        "live": True,
    },
]

METODOS = {
    "lead": (
        "Lo que hay debajo de cada demo: el modelo, los datos y cómo se "
        "verifica. Sin esto, un pronóstico es solo una opinión con mapa."
    ),
    "items": [
        ("Modelación numérica", "WRF, asimilación por nudging observacional (FDDA), diseño de ensambles."),
        ("Datos", "ERA5, ECMWF IFS-ENS, CHIRPS, GLEAM, redes de estaciones en superficie."),
        ("Verificación", "CRPS, Brier, diagramas de confiabilidad. Nada se publica sin métrica."),
        ("Ingeniería", "Python, xarray, Dask. Pipelines automatizados en servidor propio."),
    ],
}

PIE = {
    "nota": "Medellín, Colombia",
    "links": {
        "GitHub": "https://github.com/tu-usuario",
        "LinkedIn": "https://linkedin.com/in/tu-perfil",
        "Correo": "mailto:tu@correo.com",
    },
}
