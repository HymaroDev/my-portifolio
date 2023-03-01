import streamlit as st

st.set_page_config(
    page_title= "Hymaro's Portifolio",
    page_icon= ":rocket:"
)

st.sidebar.success("Selecione uma página acima.")

"""
# Hymaro - Portifolio
"""

code = """
print("Olá! me chamo hymaro! bem vindo ao meu portifolio!")

about-me = print("Tenho 13y, sou desenvolvedor python júnior!")
"""

st.code(code, language='python')

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

st.header("Check my social medias below:")


url = "https://github.com/hymarodev"
st.write(" 💻️ Github [link](%s)" % url)

url2 = "https://twitter.com/amoxerecax"
st.write("💬 Twitter [link](%s)" % url2)
