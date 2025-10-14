import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="Minha Página Streamlit")

st.title("Meu Site usando o Streamlit")

# 2. Caminho do Arquivo
# Certifique-se de que 'resultados.csv' está no mesmo diretório!
CAMINHO_DO_ARQUIVO = "resultados.csv"

# 3. Função para Carregar os Dados (com cache)
# O decorador @st.cache_data garante que o arquivo só será lido uma vez,
# o que torna seu aplicativo muito mais rápido após a primeira execução.
@st.cache_data
def carregar_dados(caminho):
    """Carrega os dados do arquivo CSV."""
    try:
        # Lê o arquivo CSV usando Pandas
        df = pd.read_csv(caminho)
        return df
    except FileNotFoundError:
        st.error(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return None
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar o arquivo: {e}")
        return None

# 4. Carregar e Exibir os Dados
dados = carregar_dados(CAMINHO_DO_ARQUIVO)

if dados is not None:
    st.header("Visualização dos Dados (resultados.csv)")

    # Exibe o DataFrame de forma interativa (permite ordenar, pesquisar)
    st.dataframe(dados)

    # Opcional: Exibe as primeiras linhas
    if st.checkbox('Mostrar Primeiras 5 Linhas'):
        st.subheader("Amostra dos Dados")
        st.write(dados.head())

    # Opcional: Exibe informações estatísticas
    if st.checkbox('Mostrar Estatísticas Descritivas'):
        st.subheader("Estatísticas")
        st.write(dados.describe())