import streamlit as st

st.set_page_config(layout="wide", page_title="Jogadores")

df_data = st.session_state["data"]
clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox("Selecione o clube", clubes)

df_players = df_data[df_data["Club"] == clube]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Selecione o jogador", players)

player_stats = df_players[df_players["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")
st.image(player_stats['Flag'])

st.markdown(f"Clube: **{player_stats['Club']}**")
st.markdown(f"Posição: **{player_stats['Position']}**")


col1, col2, col3 = st.columns(3)
col1.markdown(f"Idade: **{player_stats['Age']}**")
col2.markdown(f"Altura: **{player_stats['Height']}**")
col3.markdown(f"Peso: **{player_stats['Weight']}**")

st.divider()
st.subheader(f"Atributos | Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de Mercado", value=f"{player_stats['Value']}")
col2.metric(label="Salário", value=f"{player_stats['Wage']}")
col3.metric(label="Perna Boa", value=f"{player_stats['Preferred Foot']}")
