import streamlit as st

def initialize_page():
    st.set_page_config(page_title="Simplex Solver", layout="centered")
    st.title("Método Simplex")
    st.write("Vamos iniciar! Preencha as informações seguindo o formato correto.")

def executing():
    pass

def show_results(status, objective, variables, max_gain):
    st.write(status)
    st.write(objective)
    st.write(variables)
    st.write(max_gain)