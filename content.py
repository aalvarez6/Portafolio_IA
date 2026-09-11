"""
Contenido del sitio. Aquí editas texto y herramientas sin tocar el CSS.

=====================================================================
AVISO: las descripciones se dedujeron del nombre de cada app, porque
Streamlit bloquea el acceso automatizado y no se pudo verificar qué
hace cada una. Reemplaza cada línea marcada con # VERIFICAR.
=====================================================================
"""

PERFIL = {
    "nombre": "Alejandra Álvarez",
    "titular": "Ingeniería eléctrica, con IA que sí se usa.",
    "lead": (
        "Ingeniera eléctrica. Construyo herramientas de inteligencia "
        "artificial para problemas concretos de energía, datos y "
        "automatización. Todas están desplegadas y abiertas: no son "
        "capturas de pantalla, se pueden usar ahora mismo."
    ),
    "pie_figura": (
        "Demanda diaria, generación solar y la carga neta resultante."
    ),
}

NAV = {
    "Herramientas": "#herramientas",
    "Cómo trabajo": "#cómo-trabajo",
    "Contacto": "mailto:TU-CORREO@ejemplo.com",
}


# ---------------------------------------------------------------------
# NIVEL 1 — Tarjeta completa. Máximo seis.
# ---------------------------------------------------------------------
# Criterio de selección: las que demuestran criterio de ingeniería, no
# integración de una API. Si crees que otra merece estar aquí, cámbiala:
# lo único que importa es que sean pocas.

DESTACADAS = [
    {
        "title": "Pronóstico de generación solar",
        # VERIFICAR: ¿qué predice exactamente y con qué horizonte?
        "lead": (
            "Estima la generación de un sistema fotovoltaico a partir de "
            "variables meteorológicas, para anticipar el aporte al sistema "
            "y dimensionar el respaldo."
        ),
        "meta": {
            "Dominio": "Sistemas fotovoltaicos",   # VERIFICAR
            "Entrada": "Series meteorológicas",     # VERIFICAR
            "Salida": "Curva de generación",        # VERIFICAR
        },
        "href": "https://sowi-energy-forecast.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "Agente de análisis de datos",
        # VERIFICAR
        "lead": (
            "Sube un conjunto de datos y pregúntale en lenguaje natural. "
            "El agente escribe y ejecuta el análisis, y devuelve resultado "
            "y código."
        ),
        "meta": {
            "Modelo": "LLM con ejecución de código",
            "Entrada": "CSV o Excel",
            "Salida": "Análisis y gráficos",
        },
        "href": "https://dataagentt.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "Consulta de documentos PDF",
        # VERIFICAR
        "lead": (
            "Preguntas en lenguaje natural sobre documentos largos: normas, "
            "manuales, informes técnicos. Responde citando la fuente."
        ),
        "meta": {
            "Técnica": "RAG con búsqueda semántica",
            "Entrada": "PDF",
            "Salida": "Respuesta con referencia",
        },
        "href": "https://chatpdefe.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "Detección de objetos con YOLO",
        # VERIFICAR: ¿detecta algo específico o es de propósito general?
        "lead": (
            "Identifica y localiza objetos en imágenes en tiempo real, con "
            "umbral de confianza ajustable."
        ),
        "meta": {
            "Modelo": "YOLOv5",
            "Entrada": "Imagen o cámara",
            "Salida": "Cajas y clases detectadas",
        },
        "href": "https://yolov55.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "Lectura de texto en imágenes a voz",
        # VERIFICAR
        "lead": (
            "Extrae el texto de una imagen y lo convierte en audio. Pensado "
            "para accesibilidad y para digitalizar documentos impresos."
        ),
        "meta": {
            "Técnica": "OCR y síntesis de voz",
            "Entrada": "Imagen",
            "Salida": "Texto y audio",
        },
        "href": "https://ocr-audioo.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "Convoluciones, paso a paso",
        # VERIFICAR: ¿es herramienta didáctica?
        "lead": (
            "Visualiza cómo un kernel recorre una imagen y qué produce cada "
            "filtro. Hecho para enseñar la operación que sostiene toda la "
            "visión por computador."
        ),
        "meta": {
            "Tipo": "Herramienta didáctica",
            "Entrada": "Imagen y kernel",
            "Salida": "Mapa de activación",
        },
        "href": "https://convoluciones.streamlit.app/",
        "externa": True,
        "live": True,
    },
]


# ---------------------------------------------------------------------
# NIVEL 2 — Índice compacto. Sin tarjeta, solo enlace.
# ---------------------------------------------------------------------
# "que" debe caber en 3 o 4 palabras: es una etiqueta, no una descripción.

OTRAS = [
    {"title": "Visión por computador", "que": "Clasificación de imágenes",
     "href": "https://visionn.streamlit.app/"},                    # VERIFICAR
    {"title": "Traductor", "que": "Traducción automática",
     "href": "https://traductore.streamlit.app/"},
    {"title": "Generador de texto", "que": "Generación con LLM",
     "href": "https://textgeneratoor.streamlit.app/"},
    {"title": "Análisis de sentimientos", "que": "Clasificación de opinión",
     "href": "https://sentimientos-1.streamlit.app/"},
    {"title": "Chatbot con Claude", "que": "Asistente conversacional",
     "href": "https://chatbot-antropic.streamlit.app/"},
    {"title": "Explorando la API de GPT", "que": "Banco de pruebas",
     "href": "https://chatgptexploring.streamlit.app/"},
    {"title": "Texto a voz", "que": "Síntesis de voz",
     "href": "https://text-to-voic.streamlit.app/"},
    {"title": "OCR", "que": "Extracción de texto",
     "href": "https://opticalcr.streamlit.app/"},
    {"title": "Nube de palabras", "que": "Visualización de frecuencias",
     "href": "https://wordcloud-1.streamlit.app/"},
    {"title": "Clasificador de posturas", "que": "Teachable Machine",
     "href": "https://teachablem-yogi.streamlit.app/"},            # VERIFICAR
    {"title": "TL Flores", "que": "Transfer learning",
     "href": "https://tlflores.streamlit.app/"},                   # VERIFICAR
    # Esta app conserva el subdominio autogenerado. Renómbrala en Streamlit
    # Cloud (Settings > General > Custom subdomain) antes de publicar.
    {"title": "Sin nombre", "que": "Renombrar el subdominio",
     "href": "https://hzwi7bwfepy6scpu7pradh.streamlit.app/"},     # VERIFICAR
]


METODOS = {
    "lead": (
        "Cómo construyo estas herramientas. Sin esto, una demo de IA es "
        "solo un truco que funciona una vez."
    ),
    "items": [
        ("Ingeniería eléctrica",
         "El dominio va primero: la herramienta parte del problema real, no del modelo disponible."),
        ("Modelos",
         "LLMs, visión por computador y aprendizaje supervisado, según lo que el problema pida."),
        ("Producto",
         "Python y Streamlit, con repositorio propio y despliegue continuo. Lo que no se puede abrir no existe."),
        ("Alcance declarado",
         "Cada herramienta dice qué asume y dónde deja de ser confiable."),
    ],
}

PIE = {
    "nota": "Medellín, Colombia",
    "links": {
        "GitHub": "https://github.com/aalvarez6",
        "LinkedIn": "https://linkedin.com/in/TU-PERFIL",
        "Correo": "mailto:TU-CORREO@ejemplo.com",
    },
}
