# pages/4_📊_Analise_Dados.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, poisson, binom, shapiro

# Carregando os dados
df = pd.read_excel(st.secrets["caminhos"]["excel"])

# Título da página
st.title("Análise de Dados Financeiros - Banco Safra 📊")

# ==============================================================================
# 1. Apresentação dos Dados e Tipos de Variáveis
# ==============================================================================
st.header("📝 Explicação sobre a Análise de Dados")
st.markdown('''
Nesta seção, estamos analisando dados financeiros de clientes do **Banco Safra**. Esses dados incluem informações como idade, saldo médio na conta, renda mensal, pontuação de crédito, quantidade de transações, valor total movimentado, categoria de cliente (baixa, média ou alta renda), se o cliente possui investimentos e se já teve atrasos no pagamento.

O objetivo é entender o comportamento dos clientes e identificar padrões que possam ajudar o banco a tomar decisões mais informadas. Por exemplo:

1. **Distribuição de Renda**: Verificamos como a renda dos clientes está distribuída.
2. **Relação entre Score de Crédito e Saldo Médio**: Analisamos se clientes com maior pontuação de crédito tendem a ter um saldo médio mais alto.
3. **Probabilidade de Atrasos**: Calculamos a probabilidade de um cliente ter atrasos no pagamento.
4. **Distribuição de Transações**: Verificamos como as transações estão distribuídas entre as diferentes categorias de clientes.
''')

# Análise de Coerência dos Dados
st.header("🔍 Análise de Coerência dos Dados")
st.markdown(f'''
1. **Idade**:  
   - Mínima: {df['Idade'].min()} anos  
   - Máxima: {df['Idade'].max()} anos  
   - Verificação: {"✅" if 18 <= df['Idade'].min() and df['Idade'].max() <= 100 else "❌"} (Intervalo esperado: 18-100 anos)

2. **Saldo Médio e Renda Mensal**:  
   - Saldo mínimo: R$ {df['Saldo_Medio'].min():.2f}  
   - Saldo máximo: R$ {df['Saldo_Medio'].max():.2f}  
   - Renda mínima: R$ {df['Renda_Mensal'].min():.2f}  
   - Renda máxima: R$ {df['Renda_Mensal'].max():.2f}  
   - Verificação: {"✅" if df['Saldo_Medio'].min() >= 0 and df['Renda_Mensal'].min() >= 0 else "❌"} (Valores positivos)

3. **Score de Crédito**:  
   - Mínimo: {df['Score_Credito'].min()}  
   - Máximo: {df['Score_Credito'].max()}  
   - Verificação: {"✅" if 0 <= df['Score_Credito'].min() and df['Score_Credito'].max() <= 1000 else "❌"} (Intervalo esperado: 0-1000)

4. **Quantidade de Transações**:  
   - Mínima: {df['Qtd_Transacoes'].min()}  
   - Máxima: {df['Qtd_Transacoes'].max()}  
   - Verificação: {"✅" if df['Qtd_Transacoes'].min() >= 0 else "❌"} (Valores positivos)

5. **Categoria de Cliente**:  
   - Categorias válidas: {df['Categoria_Cliente'].unique()}  
   - Verificação: {"✅" if set(df['Categoria_Cliente'].unique()).issubset({'Baixa Renda', 'Média Renda', 'Alta Renda'}) else "❌"} (Categorias esperadas)
''')

st.header("1. Apresentação dos Dados e Tipos de Variáveis")
st.subheader("Amostra dos Dados (5 primeiras linhas)")
st.dataframe(df.head())

st.subheader("Tipos de Variáveis")
st.markdown('''
| Variável                | Tipo              | Descrição                          |
|-------------------------|-------------------|------------------------------------|
| ID_Cliente              | Quantitativa      | Identificador único                |
| Idade                   | Quantitativa      | Idade do cliente                   |
| Saldo_Medio             | Quantitativa      | Saldo médio na conta               |
| Renda_Mensal            | Quantitativa      | Renda mensal do cliente            |
| Score_Credito           | Quantitativa      | Pontuação de crédito (0-1000)      |
| Qtd_Transacoes          | Quantitativa      | Número de transações mensais        |
| Valor_Total_Transacoes  | Quantitativa      | Valor total movimentado            |
| Categoria_Cliente       | Qualitativa       | Classificação por renda            |
| Possui_Investimentos    | Binária           | Investimentos ativos (0/1)         |
| Atraso_Pagamento        | Binária           | Histórico de atrasos (0/1)         |
''')

st.subheader("Principais Perguntas de Análise")
st.markdown('''
1. Qual a distribuição de renda dos clientes?
2. Existe relação entre score de crédito e saldo médio?
3. Qual a probabilidade de um cliente ter atrasos?
4. Como as transações se distribuem entre categorias de clientes?
''')

# ==============================================================================
# 2. Medidas Centrais e Dispersão
# ==============================================================================
st.header("2. Medidas Centrais e Dispersão")
var_num = st.selectbox("Selecione a variável para análise:", 
                      ['Saldo_Medio', 'Renda_Mensal', 'Score_Credito', 'Qtd_Transacoes'])

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Média", f"R$ {df[var_num].mean()/1000:.2f} mil")
with col2:
    st.metric("Mediana", f"R$ {df[var_num].median()/1000:.2f} mil")
with col3:
    st.metric("Desvio Padrão", f"R$ {df[var_num].std()/1000:.2f} mil")
with col4:
    st.metric("Variância", f"R$ {df[var_num].var()/1e6:.2f} milhões")
with col5:
    st.metric("Moda", f"R$ {df[var_num].mode()[0]/1000:.2f} mil")

# Histograma
st.subheader(f"Distribuição de {var_num}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df[var_num], kde=True, bins=20, color='#1d4ed8')
plt.xlabel(var_num)
plt.ylabel('Frequência')
st.pyplot(fig)
plt.close(fig)

# Discussão
st.subheader("Discussão sobre a Distribuição dos Dados")
Q1 = df[var_num].quantile(0.25)
Q3 = df[var_num].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df[var_num] < (Q1 - 1.5 * IQR)) | (df[var_num] > (Q3 + 1.5 * IQR))]
st.markdown(f'''
- **Simetria**: {"Assimétrica positiva" if df[var_num].skew() > 0 else "Assimétrica negativa" if df[var_num].skew() < 0 else "Simétrica"}
- **Outliers**: {len(outliers)} clientes com valores atípicos
- **Moda**: {df[var_num].mode()[0]:.2f} (valor mais frequente)
''')

# ==============================================================================
# 3. Análise de Correlação (Gráfico de Dispersão)
# ==============================================================================
st.header("3. Análise de Correlação (Gráfico de Dispersão)")
var_x = st.selectbox("Selecione a variável para o eixo X:", 
                     ['Saldo_Medio', 'Renda_Mensal', 'Score_Credito', 'Qtd_Transacoes'])
var_y = st.selectbox("Selecione a variável para o eixo Y:", 
                     ['Saldo_Medio', 'Renda_Mensal', 'Score_Credito', 'Qtd_Transacoes'])

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=var_x, y=var_y, data=df, color='#1d4ed8', alpha=0.7)
plt.xlabel(var_x)
plt.ylabel(var_y)
st.pyplot(fig)
plt.close(fig)

# ==============================================================================
# 4. Distribuições Probabilísticas
# ==============================================================================
st.header("4. Distribuições Probabilísticas")

# Distribuição Normal
st.subheader("Distribuição Normal: Score de Crédito")
mu, std = norm.fit(df['Score_Credito'])
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df['Score_Credito'], kde=True, stat='density', color='#4CAF50')
x = np.linspace(df['Score_Credito'].min(), df['Score_Credito'].max(), 100)
plt.plot(x, norm.pdf(x, mu, std), 'r--', linewidth=2)
st.pyplot(fig)
plt.close(fig)

# Distribuição Binomial
st.subheader("Distribuição Binomial: Atrasos de Pagamento")
p = df['Atraso_Pagamento'].mean()
x = np.arange(0, 2)
pmf = binom.pmf(x, n=1, p=p)
fig, ax = plt.subplots(figsize=(8, 6))
plt.bar(x, pmf, color='#FF5722', alpha=0.7)
plt.xticks(x, ['Sem Atraso', 'Com Atraso'])
for i, v in enumerate(pmf):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', va='bottom')
st.pyplot(fig)
plt.close(fig)

# Distribuição de Poisson (CÓDIGO FINAL)
st.subheader("Distribuição de Poisson: Quantidade de Transações")
lambda_ = df['Qtd_Transacoes'].mean()

# Limitar o intervalo de x para focar na região mais relevante
max_x = int(lambda_ + 3 * np.sqrt(lambda_))  # Regra prática: λ ± 3σ
x = np.arange(max(0, int(lambda_ - 3 * np.sqrt(lambda_))), max_x + 1)
pmf = poisson.pmf(x, lambda_)

# Criar o gráfico com tamanho ajustado
fig, ax = plt.subplots(figsize=(16, 6))
bars = plt.bar(x, pmf, color='#9C27B0', alpha=0.7, width=0.8)

# Configurações do gráfico
plt.xlabel('Número de Transações', fontsize=12)
plt.ylabel('Probabilidade', fontsize=12)
plt.xticks(x, rotation=75, fontsize=10, ha='right')  # Rotação mais acentuada
plt.title(f'Distribuição de Poisson (λ = {lambda_:.2f})', fontsize=14)

# Adicionar anotações apenas para probabilidades significativas
for bar in bars:
    height = bar.get_height()
    if height > 0.01:  # Apenas valores acima de 1%
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.001,
            f'{height:.2f}',  # 2 casas decimais
            ha='center',
            va='bottom',
            fontsize=8,
            rotation=45
        )

# Ajustar layout e margens
plt.subplots_adjust(bottom=0.25)  # Mais espaço para os rótulos do eixo X
plt.grid(axis='y', linestyle='--', alpha=0.4)
st.pyplot(fig)
plt.close(fig)
# ==============================================================================
# Análise Complementar
# ==============================================================================
st.header("Análise por Categoria de Cliente")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Categoria_Cliente', y='Saldo_Medio', data=df, palette='Set2')
plt.xticks(rotation=45)
st.pyplot(fig)
plt.close(fig)

st.header("🎯 Conclusão")
st.markdown('''
Essa análise permite ao Banco Safra entender melhor o perfil dos clientes e otimizar estratégias comerciais e de risco.
''')