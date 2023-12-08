# Importando as Bibliotecas

import streamlit as st
import pandas as pd
import webbrowser
from PIL import Image

# Configurando a página
st.set_page_config(
    page_title="Início", 
    layout="wide")

# Carregando os dados
if "data" not in st.session_state:
    df_data = pd.read_csv("FIFA23_official_data.csv", index_col=0, sep=";")
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

# Criando a página
st.write("# FIFA23 OFFICIAL DATASET!")
logo = Image.open("logo.png")
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown("Baseado no Projeto do ASIMOV ACADEMY")

# Criando o botão e a descrição
botao = st.button("Acesse os dados no Kaggle")
if botao:
    webbrowser.open("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")
    
st.markdown(
    """
    Conjunto de dados com informações de jogadores de futebol do FIFA 23, com dados como idade, nacionalidade, clube, salário, valor de mercado, etc. 
    """
)
