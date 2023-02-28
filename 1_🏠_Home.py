from bokeh.models.widgets import Div
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

github = st.button("💻️ Github")
twitter = st.button("💬 Twitter")

if github:
    js = "window.open('https://github.com/hymarodev')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

if twitter:
    js = "window.open('https://twitter.com/amoxerecax')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
   
url = "https://github.com/hymarodev"
st.write("Github [link](%s)" % url)
st.markdown("Github [link](%s)" % url)
