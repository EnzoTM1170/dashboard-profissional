# pages/3_🛠️_Skills.py
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Skills - Enzo Teles de Moura", layout="wide")

# Título da página
st.title("Skills 🛠️")

# Função para criar uma barra de progresso compacta
def progress_bar(label, value):
    st.markdown(f'''
    <div style="margin-bottom: 10px;">
        <strong>{label}</strong>  
        <div style="background-color: #e0e0e0; border-radius: 5px; padding: 3px;">
            <div style="background-color: #4caf50; width: {value}%; height: 8px; border-radius: 5px;"></div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Habilidades Técnicas
st.header("💻 Habilidades Técnicas")

# Layout em colunas para as habilidades
col1, col2 = st.columns(2)

with col1:
    progress_bar("JavaScript", 60)  # 60% de proficiência
    progress_bar("Python", 60)      # 60% de proficiência
    progress_bar("HTML/CSS", 80)    # 80% de proficiência
    progress_bar("Excel", 80)       # 80% de proficiência

with col2:
    progress_bar("SQL/MySQL", 40)   # 40% de proficiência
    progress_bar("Java", 40)        # 40% de proficiência
    progress_bar("Analytics", 60)   # 60% de proficiência

# Soft Skills
st.header("🤝 Soft Skills")
st.markdown('''
- **Comunicação**
- **Colaboração**
- **Aprendizado contínuo**
- **Resolução de problemas**
''')

# Idiomas
st.header("🌍 Idiomas")
progress_bar("Inglês", 50)  # 50% de proficiência
progress_bar("Espanhol", 30)  # 30% de proficiência