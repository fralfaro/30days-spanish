import streamlit as st

st.set_page_config(
    page_title="Día 01",
    page_icon="1️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("1️⃣ Día 01")

st.title("Configurando tu entorno de desarrollo local")

st.write("""
Antes de empezar a desarrollar nuestras aplicaciones, vamos a necesitar primero configurar el entorno de desarrollo.

Comencemos instalando y configurando el entorno Conda.
""")

st.header("Instalar conda")
st.markdown("""
- Para instalar `conda` diríjase a [Miniconda](https://docs.conda.io/en/latest/miniconda.html) y seleccione su sistema operativo (Windows, Mac o Linux).
- Descargue y ejecute el instalador para instalar `conda`.
""")

st.header("Crear un nuevo entorno conda")
st.write("""
Una vez que haz instalado conda, comencemos creando un entorno para gestionar todas las dependencias de la librería Python.

Para crear un nuevo entorno con Python 3.9, ejecute lo siguiente:
""")
st.code("conda create -n stenv python=3.9", language="bash")
st.write("""
donde `create -n stenv` va a crear un entorno conda llamado `stenv` y `python=3.9` va a especificar que se utilice la versión 3.9 de Python en el entorno conda.
""")

st.header("Activar el entorno conda")
st.write("Para utilizar el entorno conda llamado `stenv` que acabamos de crear, ejecute lo siguiente en su terminal:")
st.code("conda activate stenv", language="bash")

st.header("Instalar la librería Streamlit")
st.write("Es tiempo de instalar la librería `streamlit`:")
st.code("pip install streamlit", language="bash")

st.header("Ejecutar la aplicación demo de Streamlit")
st.write("Para ejecutar la aplicación demo (Figura 1) ingrese:")
st.code("streamlit hello", language="bash")
