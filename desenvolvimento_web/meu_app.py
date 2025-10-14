import streamlit as st
import pandas as pd

st.set_page_config(page_title="Minha Página Streamlit")

with st.container():
    st.subheader("Meu Site usando o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações dos contratos celebrados pela Empresa Y no mês de maio")
    st.write(
        "Site da empresa na B3 [Clique aqui](https://br.tradingview.com/symbols/BMFBOVESPA-GOLL54/?utm_campaign=hotlists&utm_medium=widget&utm_source=www.b3.com.br)"
    )
    
with st.container():
    st.write("---")
    
with st.container():
    dados= pd.read_csv("resultados.csv")
    st.area_chart(dados ,x="Data" , y="Contratos")