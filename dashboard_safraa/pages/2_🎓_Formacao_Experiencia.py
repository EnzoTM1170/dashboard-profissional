# pages/2_🎓_Formacao_Experiencia.py
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Formação e Experiência - Enzo Teles de Moura", layout="wide")

# Título da página
st.title("Formação e Experiências 🎓")

# Formação
st.header("🎓 Formação")
st.markdown('''
<div style="padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0;">
    <p style="font-size: 16px;">
        <strong>Engenharia de Software</strong> - FIAP (Ago/2023 - Jun/2027)  
        <em>Período: Manhã (com flexibilidade de troca de período)</em>  
        <em>Semestre atual: 4º semestre</em>
    </p>
    <p style="font-size: 16px;">
        <strong>Ensino Médio Completo</strong>  
        <em>Colégio Marupiara - Concluído em 12/2022</em>
    </p>
</div>
''', unsafe_allow_html=True)

# Experiências
st.header("💼 Experiências Profissionais")
st.markdown('''
<div style="padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0;">
    <p style="font-size: 16px;">
        <strong>Projeto do Hospital das Clínicas:</strong>  
        Desenvolvimento de uma plataforma web acessível para o Instituto da Criança e do Adolescente.  
        <em>Tecnologias: HTML/CSS, JavaScript, Design Thinking.</em>
    </p>
    <p style="font-size: 16px;">
        <strong>Análise da Matriz Energética no Brasil:</strong>  
        Projeto de análise de dados utilizando informações do IBGE.  
        <em>Métricas: média, mediana, desvio padrão.</em>
    </p>
    <p style="font-size: 16px;">
        <strong>Análise de Dados de Pesquisa de Satisfação Empresarial:</strong>  
        Identificação de problemas críticos e proposição de melhorias com base em dados.
    </p>
    <p style="font-size: 16px;">
        <strong>Projeto Pessoal - Análise de Pesquisa de Satisfação Organizacional:</strong>  
        Realizei a análise de uma pesquisa de satisfação organizacional, identificando problemas críticos da empresa.  
        Desenvolvi diferentes formas de avaliação para cada questão identificada, auxiliando na compreensão dos desafios e na proposição de melhorias para o ambiente corporativo.
    </p>
</div>
''', unsafe_allow_html=True)

# Certificados
st.header("📜 Certificados")
st.markdown('''
- Design Thinking - FIAP
- Cybersecurity - FIAP
- MySQL - ALURA
- Social e Sustentabilidade - FIAP
- Dados com Python - DIO
- Power BI - ALURA
- Linguagem M - ALURA
''')