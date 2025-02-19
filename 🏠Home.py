import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="30 Días de Streamlit",
    page_icon="🏠",

)


st.image(Image.open('docs/images/streamlit-logo-secondary-colormark-darktext.png'))
st.title('# 30 Días de Streamlit')

st.markdown('''
    **#30DaysOfStreamlit** es un desafío diseñado para ayudarlo a comenzar a crear aplicaciones Streamlit.
    
    En particular, podrás:
    - Configure un entorno de desarrollo para construir aplicaciones Streamlit
    - Construir tu primer aplicación Streamlit
    - Aprender acerca de todos los sorprendentes componentes para usar en tu aplicación Streamlit
    ''')

# Sidebar
st.sidebar.header('Acerca')
st.sidebar.markdown('[Streamlit](https://streamlit.io) es una librería de Python que permite la creación de aplicaciones web interactivas, basadas en datos de Python .')

st.sidebar.header('Recursos')
st.sidebar.markdown('''
- [Documentacion de Streamlit](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Libro](https://www.amazon.com/dp/180056550X)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/)
''')

st.sidebar.header('Despliegue')
st.sidebar.markdown('Tu puedes desplegar rápidamente aplicaciones Streamlit usando [Streamlit Community Cloud](https://streamlit.io/cloud) en solo algunos clicks.')


