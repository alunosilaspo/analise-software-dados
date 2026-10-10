import joblib
import pandas as pd
from typing import Any


def carregar_modelo_ml(caminho_modelo: str) -> Any:
  """Carrega o artefato .joblib do modelo treinado."""
  try:
    modelo = joblib.load(caminho_modelo)
    return modelo
  except Exception as e:
    print(f"Erro ao carregar o modelo de Machine Learning: {e}")
    return None


def prever_proxima_despesa(
    modelo: Any, media_anterior: float, categoria: str, categorias_possiveis: list
) -> float:
  """Realiza a predição da próxima despesa utilizando o modelo serializado."""
  dados_entrada = {"media_gastos_anteriores": [media_anterior]}

  for cat in categorias_possiveis:
    col_name = f"categoria_{cat}"
    dados_entrada[col_name] = [1 if categoria == cat else 0]

  X_pred = pd.DataFrame(dados_entrada)
  predicao = modelo.predict(X_pred)[0]
  return float(predicao)