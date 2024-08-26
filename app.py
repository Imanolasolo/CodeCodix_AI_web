import streamlit as st
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.parse
import base64
from home import show_home
from products import show_products_services
from contact import show_contacts

# Configuración de la página
st.set_page_config(page_title="CodeCodix IA", page_icon="🌟", layout="wide")

# Función para obtener el base64 de un archivo binario
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Cargar imagen de fondo
img_base64 = get_base64_of_bin_file('logo_portfolio1.jpg')

# Estilos CSS para el fondo
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
        background-size: auto;
        background-blend-mode: darken;
        
    }}
    
    .footer {{
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: red;
        border-top: 1px solid #ddd;
    }}
    .footer .CodeCodix {{
        color: red;
        font-weight: bold;
    }}

    </style>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns ([1,4])
with col1:
    st.image('CODECODIX_logo.png', width=150)
# Crear un menú superior con opción de cambio de idioma
with col2:
    selected = option_menu(
    menu_title='CodeCodix IA',
    options=["Home", "Projects & Services", "Contact", "Chat with AI"],  # Opciones del menú
    icons=["house", "info-circle", "envelope", "chat"],  # Iconos para las opciones
    menu_icon="cast",  # Icono del menú
    default_index=0,  # Opción seleccionada por defecto
    orientation="horizontal",  # Menú horizontal
    key="main_menu"
)

# Contenido según la selección del menú
if selected == "Home":
    show_home()

elif selected == "Projects & Services":
    # Aquí agregar el contenido que desees para la sección "About"
    show_products_services()

elif selected == "Contact":
    show_contacts()
    

elif selected == "Chat with AI":
    st.write('Chat with our CEO, :red[**Imanol Asolo´s AI**], we will interact with you with our personal chatbot to solve all you questions about :red[CodeCodix] capabilities.')
    # Agregar el botón que abre el enlace en una nueva pestaña
    st.markdown(
        """
        <a href="https://aiprofilevcard.streamlit.app/" target="_blank">
            <button style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #007BFF; color: white; border: none; border-radius: 5px;">
                Chat with my AI
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# Agregar pie de página
st.markdown(
    """
    <div class="footer">
        <p>© 2024 CodeCodix | All rights reserved </p>
    </div>
    """,
    unsafe_allow_html=True
)