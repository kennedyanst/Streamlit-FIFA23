import streamlit as st

st.set_page_config(
    page_title="Times", 
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox("Selecione o clube", clubes)

df_filtered = df_data[df_data['Club'] == club].set_index('Name')

st.image(df_filtered.iloc[0]["Club Logo"], width=30)
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall"]


st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                "Photo": st.column_config.ImageColumn("Photo", width=50),
                "Flag": st.column_config.ImageColumn("Flag", width=50)
             }, height=1000, width=1000)