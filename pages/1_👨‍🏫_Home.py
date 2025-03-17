# -*- coding: utf-8 -*-
import streamlit as st

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

local_css("style.css")

# Adiciona Font Awesome
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

# Título principal
st.markdown('''
<div class="dashboard-title">
    🚀 Dashboard Profissional - Enzo Teles de Moura
</div>
''', unsafe_allow_html=True)

st.markdown("---")

# Seção "Quem sou eu?"
st.markdown("""
<div class="box-terroso" style="text-align: center; margin-top: 40px;">
    <h2>🏠 Quem sou eu?</h2>
</div>
""", unsafe_allow_html=True)

# Adicionando a nova frase abaixo da seção "Quem sou eu?"
st.markdown("""
<div class="box-terroso" style="padding: 20px; margin-top: 20px;">
    <p style="font-size: 16px; text-align: center;">
        Estudante de Engenharia de Software, com interesse em estagiar na área de tecnologia. 
        Experiência em projetos acadêmicos com metodologias ágeis, planejamento e organização. 
        Comunicativo, colaborativo e comprometido com aprendizado contínuo.
    </p>
</div>
""", unsafe_allow_html=True)

# Layout em colunas
col_foto, col_conteudo = st.columns([1, 2], gap="large")

with col_foto:
    st.image(st.secrets["caminhos"]["imagem"], width=300)

with col_conteudo:
    st.markdown('<div class="col-conteudo">', unsafe_allow_html=True)
    
    # Container do botão centralizado
    st.markdown('<div class="botao-download-container">', unsafe_allow_html=True)
    
    with open(st.secrets["caminhos"]["pdf"], "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    st.download_button(
        label="📥 BAIXAR CURRÍCULO COMPLETO",
        data=PDFbyte,
        file_name="curriculo.08.pdf",
        mime="application/octet-stream",
        key="download-cv",
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Objetivo Profissional
st.markdown("""
<div class="objetivo-profissional">
    <h2>🎯 Objetivo Profissional</h2>
    <p style="font-size: 16px;">
        Busco uma vaga de estágio na área de tecnologia, com foco em desenvolvimento de software, análise de dados e soluções inovadoras.
    </p>
</div>
""", unsafe_allow_html=True)

# Seção de Contato
st.markdown("""
<div class="contact-section">
    <h2>📞 Contato</h2>
    <div class="contact-info">
        <p><i class="fas fa-envelope"></i> enzotm117@gmail.com</p>
    </div>
    <div style="text-align: center; margin-top: 30px;">
        <a href="https://github.com/EnzoTM1170/Portifolio" class="btn-contact btn-github" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
        <a href="https://www.linkedin.com/in/enzo-teles-de-moura-64ba49291/" class="btn-contact btn-linkedin" target="_blank">
            <i class="fab fa-linkedin"></i> LinkedIn
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

