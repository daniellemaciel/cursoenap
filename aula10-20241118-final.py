import requests as rq
import pandas as pd
import streamlit as st

#importando os dados das deputadas
url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta_mulheres = rq.get(url_mulheres)
dadosJSONmulheres = resposta_mulheres.json()
df_mulheres = pd.DataFrame(dadosJSONmulheres['dados'])
df_mulheres['sexo'] = 'F'

#importando os dados dos deputados
url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta_homens = rq.get(url_homens)
dadosJSONhomens = resposta_homens.json()
df_homens = pd.DataFrame(dadosJSONhomens['dados'])
df_homens['sexo'] = 'M'

#juntar os dois dfs
df_total = pd.concat([df_mulheres, df_homens])

#Filtrando df por sexo
#inserindo um selectbox
opcao = st.selectbox(
    'Qual o sexo?',
     df_total['sexo'].unique())
dfFiltrado = df_total[df_total['sexo'] == opcao]
st.title('Deputados do sexo ' + opcao)

#item 6
#ocorrencias totais
#procurando no chat GPT: Como calcular a quantidade de deputados por estado?
#value_counts() conta os valores únicos
ocorrencias = dfFiltrado['siglaUf'].value_counts()
dfEstados = pd.DataFrame({
    'siglaUf': ocorrencias.index,
    'quantidade': ocorrencias.values}
    )
