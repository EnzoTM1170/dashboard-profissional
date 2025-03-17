import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Dashboard Profissional - Enzo Teles de Moura",
    page_icon="🚀",
    layout="wide"
)

# Função para carregar o CSS corretamente
def local_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:  
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Arquivo CSS não encontrado: {file_name}")
    except UnicodeDecodeError:
        st.error(f"Erro ao decodificar o arquivo {file_name}. Verifique a codificação (deve ser UTF-8).")


# Caminho para o arquivo CSS
local_css("style.css")

# Título estilizado
st.markdown('''
<div style="text-align: center;">
    <h1 style="font-size: 36px; color: #4F8BF9;">🚀 Dashboard Profissional - Enzo Teles de Moura</h1>
</div>
''', unsafe_allow_html=True)

# Divisor visual
st.markdown("---")

# Mensagem de boas-vindas
st.write('''
Bem-vindo ao meu dashboard interativo! Aqui você encontrará informações sobre meu perfil profissional, habilidades, formação, experiências e uma análise de dados aplicada ao setor financeiro, com foco no **Banco Safra**.
''')

# Instruções de navegação
st.markdown('''
### Como navegar:
- Use o **menu lateral** para acessar as diferentes seções do dashboard.
- Na página **Home**, você encontrará uma introdução sobre mim e meu objetivo profissional.
- Na página **Formação e Experiências**, veja detalhes sobre minha trajetória acadêmica e profissional.
- Na página **Skills**, confira minhas habilidades técnicas e soft skills.
- Na página **Análise de Dados**, explore uma análise de dados aplicada ao setor financeiro.
''')

# Divisor visual
st.markdown("---")

# Rodapé
st.markdown('''
<div style="text-align: center; font-size: 14px; color: #666;">
    Desenvolvido por Enzo Teles de Moura | Contato: enzotm117@gmail.com
</div>
''', unsafe_allow_html=True)

# Carregando o Excel
df = pd.read_excel(st.secrets["caminhos"]["excel"])

# Carregando o CSS
def local_css(file_name):
    try:
        with open(st.secrets["caminhos"]["css"], "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Arquivo CSS não encontrado!")



# Carregando o PDF
with open(st.secrets["caminhos"]["pdf"], "rb") as pdf_file:
    PDFbyte = pdf_file.read()