import os
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st
from database import carregar_dados_sqlite
from models import carregar_modelo_ml, prever_proxima_despesa

# Configuração da Página
st.set_page_config(
    page_title="Fintech Acadêmica - Painel Preditivo",
    page_icon="💰",
    layout="wide",
)

st.title("📊 Painel Executivo e Preditivo da Fintech Acadêmica")
st.markdown(
    "Aplicativo *Full-stack* de dados desenvolvido para gestão financeira de"
    " estudantes e predição de despesas."
)

# Mapeamento robusto do diretório utilizando Pathlib para compatibilidade total com o Streamlit Cloud
DIRETORIO_ATUAL = Path(__file__).parent

CAMINHO_DB = DIRETORIO_ATUAL / "fintech_integrada.db"
CAMINHO_MODELO = DIRETORIO_ATUAL / "modelo_despesas.joblib"

df = carregar_dados_sqlite(str(CAMINHO_DB))
modelo = carregar_modelo_ml(str(CAMINHO_MODELO))

if df is not None and modelo is not None:
  st.sidebar.header("Filtros de Navegação")
  categorias_disponiveis = df["categoria"].unique().tolist()
  categoria_selecionada = st.sidebar.selectbox(
      "Selecione a Categoria", categorias_disponiveis
  )

  df_filtrado = df[df["categoria"] == categoria_selecionada]

  aba1, aba2 = st.tabs(
      ["📈 Visão Geral & KPIs", "🤖 Simulador Preditivo de Despesas"]
  )

  with aba1:
    st.subheader(f"Métricas para a categoria: {categoria_selecionada}")
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Total Gasto",
        f"R$ {df_filtrado['valor'].sum():,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", "."),
    )
    col2.metric("Número de Registros", len(df_filtrado))
    col3.metric(
        "Média por Lançamento",
        f"R$ {df_filtrado['valor'].mean():,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", "."),
    )

    st.markdown("### Amostra de Dados Limpos")
    st.dataframe(df_filtrado.head(10), use_container_width=True)

  with aba2:
    st.subheader("Simulação de Predição de Gastos Futuros")
    media_anterior_input = st.number_input(
        "Média de Gastos Anteriores (R$)",
        min_value=0.0,
        value=float(df["valor"].mean()),
        step=10.0,
    )

    categorias_encoded_cols = [
        col.replace("categoria_", "")
        for col in modelo.feature_names_in_
        if col.startswith("categoria_")
    ]

    if st.button("Calcular Predição"):
      try:
        valor_previsto = prever_proxima_despesa(
            modelo,
            media_anterior_input,
            categoria_selecionada,
            categorias_encoded_cols,
        )
        st.success(
            f"✨ O valor estimado para a próxima despesa em"
            f" **{categoria_selecionada}** é de: **R$"
            f" {valor_previsto:,.2f}**"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
      except Exception as ex:
        st.error(f"Erro ao processar a predição: {ex}")
else:
  st.warning(
      f"⚠️ O banco de dados (`fintech_integrada.db`) ou o modelo"
      f" (`modelo_despesas.joblib`) não foram encontrados no diretório"
      f" especificado:\n- Caminho testado: `{DIRETORIO_ATUAL}`"
  )