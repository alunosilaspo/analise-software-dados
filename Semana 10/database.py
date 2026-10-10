import sqlite3
import pandas as pd
from typing import Optional


def carregar_dados_sqlite(caminho_db: str) -> Optional[pd.DataFrame]:
  """Carrega a tabela despesas_clean do banco SQLite com tratamento de erros."""
  try:
    conexao = sqlite3.connect(caminho_db)
    query = "SELECT * FROM despesas_clean"
    df = pd.read_sql(query, conexao)
    conexao.close()

    if df.empty:
      return None
    return df
  except Exception as e:
    print(f"Erro ao conectar ou consultar o banco SQLite: {e}")
    return None