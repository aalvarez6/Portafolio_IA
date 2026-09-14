"""
Contenido del sitio. Un solo archivo para todo el texto.

=====================================================================
IDIOMA: el sitio está en inglés porque tu posicionamiento profesional
ya lo está (AI Engineer, GenAI, RAG, Agents) y porque ese es el idioma
del mercado al que apuntas. Para pasarlo a español, solo se traducen
las cadenas de ESTE archivo — no hay texto en ningún otro lado.

VERIFICAR: las descripciones de los proyectos son deducciones; no se
pudo abrir ninguna app. Revísalas antes de publicar.
=====================================================================
"""

PERFIL = {
    "nombre": "Alejandra Álvarez",
    "titular": "AI Engineer",
    "lead": (
        "Electrical engineer building artificial intelligence systems for "
        "real problems in energy, data and automation."
    ),
    "stack": "Python · GenAI · LLM · RAG · AI Agents · ML",
    "pie_figura": "Daily demand, solar generation and the resulting net load.",
}

NAV = {
    "Projects": "#featured-projects",
    "Capabilities": "#capabilities",
    "Contact": "mailto:TU-CORREO@ejemplo.com",
}


# ---------------------------------------------------------------------
# FEATURED PROJECTS — tres, y solo tres.
# ---------------------------------------------------------------------

DESTACADAS = [
    {
        "title": "AI Data Analyst",
        # VERIFICAR: ¿qué formatos acepta y qué devuelve exactamente?
        "lead": (
            "Upload a dataset and ask questions in plain language. The agent "
            "writes and runs the analysis, then returns both the result and "
            "the code behind it."
        ),
        "meta": {
            "Approach": "Agent with code execution",
            "Input": "CSV, Excel",
            "Output": "Analysis, charts, source code",
        },
        "href": "https://dataagentt.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "RAG Document Assistant",
        # VERIFICAR: ¿qué modelo de embeddings y qué vector store?
        "lead": (
            "Ask questions across long technical documents — standards, "
            "manuals, reports — and get answers grounded in the source, "
            "with the passage they came from."
        ),
        "meta": {
            "Approach": "RAG with vector search",
            "Input": "PDF",
            "Output": "Answer with citation",
        },
        "href": "https://chatpdefe.streamlit.app/",
        "externa": True,
        "live": True,
    },
    {
        "title": "Energy Forecasting",
        # VERIFICAR: esta es la más importante. ¿Qué predice, con qué
        # horizonte, con qué datos y contra qué se valida?
        "lead": (
            "Forecasts photovoltaic generation from meteorological inputs, "
            "so operators can anticipate supply and size the backup they "
            "actually need."
        ),
        "meta": {
            "Approach": "ML / DL on time series",
            "Input": "Meteorological series",
            "Output": "Generation curve",
        },
        "href": "https://sowi-energy-forecast.streamlit.app/",
        "externa": True,
        "live": True,
    },
]


# ---------------------------------------------------------------------
# AI ENGINEERING — agrupado por función, no en lista plana.
# ---------------------------------------------------------------------

CAPACIDADES = {
    "Generative AI": ["LLMs", "RAG", "AI Agents", "Prompt engineering"],
    "Machine learning": ["Time series", "Computer vision", "Deep learning"],
    "Engineering": ["Python", "FastAPI", "MCP", "REST APIs"],
    "Delivery": ["Docker", "Cloud deployment", "CI/CD"],
}


# ---------------------------------------------------------------------
# MORE WORK — índice compacto.
# ---------------------------------------------------------------------
# Si prefieres la versión estricta (solo tres proyectos, nada más),
# deja esta lista vacía: la sección desaparece sola.

OTRAS = [
    {"title": "Object detection", "que": "YOLOv5",
     "href": "https://yolov55.streamlit.app/"},
    {"title": "Image OCR to speech", "que": "OCR + TTS",
     "href": "https://ocr-audioo.streamlit.app/"},
    {"title": "Convolution explorer", "que": "Teaching tool",
     "href": "https://convoluciones.streamlit.app/"},
    {"title": "Image classification", "que": "Computer vision",
     "href": "https://visionn.streamlit.app/"},                    # VERIFICAR
    {"title": "Claude chatbot", "que": "Anthropic API",
     "href": "https://chatbot-antropic.streamlit.app/"},
    {"title": "GPT API sandbox", "que": "OpenAI API",
     "href": "https://chatgptexploring.streamlit.app/"},
    {"title": "Text generation", "que": "LLM",
     "href": "https://textgeneratoor.streamlit.app/"},
    {"title": "Sentiment analysis", "que": "NLP",
     "href": "https://sentimientos-1.streamlit.app/"},
    {"title": "Machine translation", "que": "NLP",
     "href": "https://traductore.streamlit.app/"},
    {"title": "Text to speech", "que": "Speech synthesis",
     "href": "https://text-to-voic.streamlit.app/"},
    {"title": "Optical character recognition", "que": "OCR",
     "href": "https://opticalcr.streamlit.app/"},
    {"title": "Word cloud", "que": "Text visualization",
     "href": "https://wordcloud-1.streamlit.app/"},
    {"title": "Pose classifier", "que": "Teachable Machine",
     "href": "https://teachablem-yogi.streamlit.app/"},            # VERIFICAR
    {"title": "Transfer learning", "que": "Image classification",
     "href": "https://tlflores.streamlit.app/"},                   # VERIFICAR
    # Subdominio autogenerado: renómbralo en Streamlit Cloud
    # (Settings > General) o retira esta entrada.
    {"title": "Untitled", "que": "Rename subdomain",
     "href": "https://hzwi7bwfepy6scpu7pradh.streamlit.app/"},     # VERIFICAR
]


PIE = {
    "nota": "Medellín, Colombia",
    "links": {
        "GitHub": "https://github.com/aalvarez6",
        "LinkedIn": "https://linkedin.com/in/TU-PERFIL",
        "Contact": "mailto:TU-CORREO@ejemplo.com",
    },
}
