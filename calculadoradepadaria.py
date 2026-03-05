import streamlit as st

# Título do site
st.title("🍞 Calculadora de Receitas - Padaria")
st.write("Calcule o custo exato das suas receitas para não ter prejuízo.")

st.divider() # Linha para separar as seções

# Criando uma "memória" (session_state) para o site guardar o custo total
if 'custo_total' not in st.session_state:
    st.session_state.custo_total = 0.0

### SEÇÃO 1: ADICIONAR INGREDIENTES ###
st.subheader("1. Adicionar Ingrediente")

nome = st.text_input("Nome do Ingrediente (ex: Farinha, Ovo, Fermento)")
preco = st.number_input("Preço da Embalagem Fechada (R$)", min_value=0.0, format="%.2f")
tamanho = st.number_input("Tamanho da Embalagem (em gramas ou ml)", min_value=1.0)
usado = st.number_input("Quantidade usada na receita (em gramas ou ml)", min_value=0.0)

# Botão para calcular o ingrediente atual
if st.button("Adicionar à Receita"):
    if tamanho > 0:
        custo_item = (preco / tamanho) * usado
        st.session_state.custo_total += custo_item
        st.success(f"Adicionado! O custo de {nome} nesta receita é de R$ {custo_item:.2f}")

st.divider()

### SEÇÃO 2: RESULTADO E PREÇO DE VENDA ###
st.subheader("2. Resumo da Receita")
st.write(f"**Custo Total dos Ingredientes:** R$ {st.session_state.custo_total:.2f}")

# Calcular margem de lucro em cima do custo total
margem_lucro = st.slider("Qual a margem de lucro desejada? (%)", min_value=0, max_value=200, value=100)
preco_venda = st.session_state.custo_total + (st.session_state.custo_total * (margem_lucro / 100))

st.info(f"💰 **Preço Sugerido para Venda:** R$ {preco_venda:.2f}")

# Botão para zerar a calculadora e começar uma nova receita
if st.button("Limpar e Começar Nova Receita"):
    st.session_state.custo_total = 0.0
    st.rerun() # Atualiza a página