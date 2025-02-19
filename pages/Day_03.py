import streamlit as st

st.set_page_config(
    page_title="Día 03",
    page_icon="3️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("3️⃣ Día 03")

st.header("st.button")

st.write("""
Una simple aplicación que imprime condicionalmente diferentes mensajes dependiendo si el botón fue presionado o no.

**Comportamiento de la aplicación:**
1. Por defecto, la aplicación imprime `Goodbye`
2. Una vez que se hace click sobre el botón, la aplicación imprime `Why hello there`
""")

# Configurar pestañas en Streamlit
tab1, tab2 = st.tabs(["🚀 App", "💡 Explicación"])

with tab1:
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

with tab2:
    st.header("Código completo")
    
    st.code("""
import streamlit as st

st.header("st.button")

st.write(\"\"\"
Una simple aplicación que imprime condicionalmente diferentes mensajes dependiendo si el botón fue presionado o no.

**Comportamiento de la aplicación:**
1. Por defecto, la aplicación imprime `Goodbye`
2. Una vez que se hace click sobre el botón, la aplicación imprime `Why hello there`
\"\"\")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
    """, language="python")

    st.header("Explicación del código")

    st.write("""
    Lo primero que tenemos que hacer cuando creamos una aplicación de Streamlit es comenzar importando la librería `streamlit` de la siguiente manera:
    """)
    st.code("import streamlit as st", language="python")

    st.write("""
    Luego, creamos un encabezado de texto para la aplicación:
    """)
    st.code("st.header('st.button')", language="python")

    st.write("""
    A continuación, agregamos una descripción con `st.write` para explicar el propósito de la aplicación:
    """)
    st.code("""
st.write(\"\"\"
Una simple aplicación que imprime condicionalmente diferentes mensajes dependiendo si el botón fue presionado o no.

**Comportamiento de la aplicación:**
1. Por defecto, la aplicación imprime `Goodbye`
2. Una vez que se hace click sobre el botón, la aplicación imprime `Why hello there`
\"\"\")
    """, language="python")

    st.write("""
    Finalmente, usamos `st.button` y condicionales `if` y `else` para mostrar diferentes mensajes dependiendo de si el botón ha sido presionado o no.
    """)
    st.code("""
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
    """, language="python")

    st.write("""
    - `st.button('Say hello')`: Crea un botón con el texto "Say hello".
    - Si el botón es presionado, `st.write('Why hello there')` imprimirá "Why hello there".
    - Si el botón no ha sido presionado, `st.write('Goodbye')` imprimirá "Goodbye".

    El comando `st.write` se usa para mostrar mensajes condicionales en función de si el botón fue presionado o no.
    """)

    st.write("""
    Para más información, consulta la documentación oficial de [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button).
    """)

css = '''
    <style>
        /* Ajusta el tamaño del texto en las pestañas (Tabs) */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.5rem; /* Tamaño del texto en las pestañas */
        }

        /* Opción adicional: Ajusta el tamaño de los encabezados dentro de los expanders */
        .st-expander h1, .st-expander h2, .st-expander h3 {
            font-size: 4rem; /* Tamaño de los encabezados dentro de los expanders */
        }

        /* Ajustar el tamaño del texto del selectbox en el sidebar */
        .sidebar .stSelectbox label {
            font-size: 1.5rem; /* Ajusta este valor para cambiar el tamaño del texto */
        }

    </style>
    '''

st.markdown(css, unsafe_allow_html=True)