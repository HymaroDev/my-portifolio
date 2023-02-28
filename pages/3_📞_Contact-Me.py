from email.message import EmailMessage
import ssl
import smtplib
from discord_webhook import DiscordWebhook, DiscordEmbed
import streamlit as st

st.set_page_config(
    page_title= "Contact-me",
    page_icon= ":telephone_receiver:"
)


"""
# Contact-Me

Neste formulário iremos pegar algumas informações para contato!

* Email
* Qual é o motivo do atendimento?
* Nome
"""

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

email = st.text_input("Email")
problema = st.selectbox(
    'Qual o seu problema?',
    ('Desenvolvimento', 'Atendimento via email', 'Outro')
)
nome = st.text_input("Nome")
SendHookClicked = st.button("Send")

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1080231709196435477/MeUPj9abOIm-On2JM2d_i3CSyWzryZkvnKKlYxp_lvjT0EvvBmM7U7pGcquNeqienNPC', content="@here")

embed = DiscordEmbed(title='New Contact!', description=f' > <:identedade:762631841525923871> **Name:** __{nome}__ \n > ✉️ **Email:** __{email}__ \n > ❔ **Problem:** __{problema}__', color='b30bff')

webhook.add_embed(embed)

if SendHookClicked:
    response = webhook.execute()