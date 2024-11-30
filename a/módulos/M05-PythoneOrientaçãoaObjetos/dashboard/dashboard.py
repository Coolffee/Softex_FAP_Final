#pip install pandas
#pip install plotly 
#pip install streamlit

#Deixar a pasta do terminal onde está dashboard.py e utilizar o comando "streamlit run dashboard.py"

import pandas as pd
import plotly.express as px
import streamlit as st

def carregar_dados(arquivo_csv):
    """Carrega os dados do arquivo CSV."""
    try:
        df = pd.read_csv(arquivo_csv)
        return df
    except FileNotFoundError:
        st.error(f"Erro: Arquivo '{arquivo_csv}' não encontrado.")
        return None

def criar_dashboard(df):
    """Cria o dashboard com gráficos e estatísticas."""

    st.title("Dashboard de Tendências de Compras")

    #Filtros
    st.sidebar.header("Filtros")
    coluna_selecionada = st.sidebar.selectbox("Selecione uma categoria:", df['Category'].unique())
    df_filtrado = df[df['Category'] == coluna_selecionada]

    #Gráfico 1: Distribuição de gastos por idade
    fig1 = px.histogram(df_filtrado, x="Purchase Amount (USD)", title="Distribuição de Gastos",
                        nbins=20,  # número de barras do histograma
                        labels={"Purchase Amount (USD)": "Valor da Compra (USD)"},
                        color='Season')
    st.plotly_chart(fig1)


    # Gráfico 2: Gastos médios por método de pagamento
    gastos_medios = df_filtrado.groupby('Payment Method')['Purchase Amount (USD)'].mean()
    fig2 = px.bar(x=gastos_medios.index, y=gastos_medios.values, title='Gastos Médios por Método de Pagamento')
    st.plotly_chart(fig2)


    # Estatísticas
    st.subheader("Estatísticas:")
    st.write(df_filtrado.describe())

    # Mais estatísticas personalizadas (exemplo)
    st.subheader("Estatísticas Adicionais:")
    valor_compra_media = df_filtrado['Purchase Amount (USD)'].mean()
    st.write(f"Valor médio das compras: {valor_compra_media:.2f} USD")
    quantidade_compras = len(df_filtrado)
    st.write(f"Número total de compras na categoria {coluna_selecionada}: {quantidade_compras}")

if __name__ == "__main__":
    nome_arquivo = 'shopping_trends.csv'
    df = carregar_dados(nome_arquivo)
    if df is not None:
        criar_dashboard(df)
