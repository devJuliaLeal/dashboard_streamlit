import streamlit_app as st
import pandas as pd
import numpy as np
# import ploty.express as px
# import plotly.graph_objects as go



st.header('Bem vindo à minha Dashboard!')
st.text('''As informações para o dashboard foram coletadas de sites
na área da computação, incluindo as tecnologias necessárias e os níveis 
de proficiência exigidos para os trabalhos. A dashboard fornecerá uma visão 
resumida e compreensível desses requisitos, auxiliando na análise e tomada de 
decisões relacionadas a oportunidades de emprego na área de desenvolvimento.''')

st.sidebar.text('Tecnologias')
st.markdown('Mais informação')
# interactive = st.beta_container()


# Criação do widget de upload de arquivo
# arquivo=st.file_uploader('/data_all_pages.csv', type='csv')

# Leitura do arquivo CSV e armazenamento em um DataFrame
df = pd.read_csv('df_salvo.csv')

# Exibição dos dados em uma tabela
st.write(df)

st.sidebar.markdown('''
---
Created with ❤️ by Julia 
''')

# with interactive:
