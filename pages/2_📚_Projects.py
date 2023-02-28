import streamlit as st

st.set_page_config(
    page_title= "Projects",
    page_icon= ":green_book:"
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

"""
# Projetos
"""

st.header("Aqui será listado meus projetos realizados em python \n \n \n")
st.markdown("***")

st.subheader("1° Project \n Sales record system with mysql")

button1 = st.button("See the project photos (imgur)")

st.markdown("***")

st.subheader("2° Project \n this portifolio")

button2 = st.button("Here is the project photos (imgur)")

st.markdown("***")

