import streamlit as st
from datetime import datetime, time
from contrato import Vendas
from pydantic import ValidationError

def main():

    st.title("Sistema de CRM e Vendas da Zapflow")
    email = st.text_input("Campo de texto para inserção o email do vendedor")
    data = st.date_input("data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9,0)) # valor padrão 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1,step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido",options=["ZapFlow com gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"])

    if st.button ("Salvar"):

            try:
                data_hora = datetime.combine(data, hora)

                venda = Vendas(
                    email = email,
                    data = data,
                    valor = valor,
                    quantidade = quantidade,
                    produto = produto
                )

                data_hora = datetime.combine(data, hora)
                st.write("**Dados da venda:**")
                st.write(f"Email do vendedor: {email}")
                st.write(f"Data e hora da compra: {data_hora}")
                st.write(f"Valor da venda: R$ {valor:.2f}")
                st.write(f"Quantidade de produtos: {quantidade}")
                st.write(f"Produto: {produto}")
                st.write(venda)
            except ValidationError as e:
                st.error(f"Deu erro{e}")
        

if __name__ == "__main__":
    main()