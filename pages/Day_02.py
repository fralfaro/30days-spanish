import streamlit as st

st.set_page_config(
    page_title="Día 02",
    page_icon="2️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("2️⃣ Día 02")

st.title("Construyendo tu primer Streamlit app")

st.header("Enciende tu IDE")
st.write("""
Utiliza tu IDE, ya sea Atom, VS Code o incluso un IDE en la nube como GitPod o GitHub.dev.

Crea un archivo con el nombre `streamlit_app.py`.
""")

st.header("Ingresando tus primeras líneas de código")
st.write("En el archivo recién creado, ingresa las siguientes líneas de código:")
st.code(
    """import streamlit as st

st.write('Hello world!')""",
    language="python"
)
st.write("Guarda el archivo.")

st.header("Enciende tu terminal de línea de comandos")
st.write("En la terminal, ingresa lo siguiente:")
st.code("streamlit run streamlit_app.py", language="bash")

st.write("Una ventana de tu explorador debería abrirse mostrando la Streamlit app recién creada.")

st.success("¡Felicitaciones! Acabas de crear tu primera Streamlit app!")
