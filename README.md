# 💰 Fintech Acadêmica - Sistema Full-Stack de Gestão e Predição Financeira

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([Insira aqui o link do seu app])
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Um ecossistema completo de engenharia e ciência de dados desenvolvido para auxiliar estudantes universitários no controle orçamentário e na predição inteligente de despesas futuras.

---

## 🎯 Sobre o Problema e Objetivo
A gestão financeira pessoal é um desafio recorrente na vida acadêmica. O projeto **Fintech Acadêmica** resolve essa dor ao centralizar o histórico de transações, limpar inconsistências de dados e disponibilizar um painel interativo aliado a um modelo de Machine Learning preditivo. 

O objetivo principal é transformar dados brutos e públicos (integrados via APIs e bases estruturadas) em *insights* acionáveis e estimativas precisas de gastos futuros.

---

## 🏗️ Arquitetura e Fluxo de Dados
O projeto segue uma arquitetura modular inspirada nas melhores práticas de desenvolvimento de software (*Clean Code*, *Type Hinting* e tratamento de exceções):

```mermaid
graph TD
    A[API Externa / Dados Brutos] -->|Wrangling & Limpeza| B[Pandas / Python]
    B -->|Persistência| C[(Banco SQLite)]
    B -->|Treinamento & Serialização| D[Scikit-Learn / .joblib]
    C -->|Consulta SQL Segura| E[Streamlit Interface]
    D -->|Predição em Tempo Real| E


⚙️ Tecnologias Utilizadas
•	Linguagem: Python 3.10+
•	Engenharia de Dados & Wrangling: Pandas, NumPy, SQLite
•	Machine Learning: Scikit-Learn (Regressão Linear, One-Hot Encoding, Métricas MAE), Joblib
•	Interface Web & Visualização: Streamlit, Seaborn, Matplotlib
•	Deploy & Versionamento: Git, GitHub, Streamlit Community Cloud
📂 Estrutura do Repositório
Plaintext
analise-software-dados/
│
├── imagens/
│   └── dashboard_executivo.png     # Screenshots do painel
├── Semana 9/
│   └── modelo_despesas.joblib      # Artefato de Machine Learning treinado
├── Semana 10/
│   ├── app.py                      # Aplicação principal (Streamlit)
│   ├── database.py                 # Camada de conexão e consultas SQL
│   ├── models.py                   # Lógica de inferência e predição
│   └── requirements.txt            # Dependências fixas do projeto
├── fintech_integrada.db            # Base de dados relacional consolidada
└── README.md                       # Documentação técnica do projeto
🚀 Como Executar o Projeto Localmente
Siga os passos abaixo para clonar e rodar a aplicação na sua máquina:
1.	Clone o repositório:
git clone [https://github.com/seu-usuario/analise-software-dados.git](https://github.com/seu-usuario/analise-software-dados.git)
cd analise-software-dados
1.	Entre na pasta da aplicação:
Bash
cd "Semana 10"
2.	Instale as dependências:
Bash
pip install -r requirements.txt
3.	Execute o aplicativo Streamlit:
Bash
streamlit run app.py
📊 Demonstração Funcional
•	Painel Executivo: Gráficos dinâmicos segmentados por categorias de despesa, métricas de soma total e ticket médio por lançamento.
•	Simulador Preditivo: Interface interativa onde o usuário insere a sua média histórica de gastos para estimar o valor da próxima despesa com base no modelo de Machine Learning integrado.
🌐 Acesse o aplicativo online: [Clique aqui para testar a Fintech Acadêmica no ar!]([Insira aqui o link do seu app])
👤 Autor
Desenvolvido por Silas
Estudante de Matemática e Administrador de Sistemas Moodle
LinkedIn
| GitHub

---

### Próximos Passos:
1. Cole este conteúdo no seu arquivo `README.md` na raiz do repositório.
2. Faça o `git add`, `git commit` e `git push` para o GitHub.
3. Realize o deploy no **Streamlit Community Cloud** (apontando para `Semana 10/app.py`), copie o URL gerado e insira-o no local indicado do `README.md`.

Com isso, o seu portfólio estará completo, extremamente técnico e pronto para impressionar qualquer recrutador ou avaliador! Se precisar de auxílio com o commit ou com o deploy, é só chamar!

