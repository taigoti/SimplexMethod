import streamlit as st
import time

def initialize_page():
    st.set_page_config(page_title="Simplex Solver", layout="centered")
    st.title("Método Simplex")
    st.write("Vamos iniciar! Preencha as informações seguindo o formato correto.")

def executing(optimize_problem, *args, **kwargs):
    with st.spinner('Executando...'):
        time.sleep(1)
        optimize_problem(*args, **kwargs)

def variables_num():
    return st.number_input(
        "Digite quantas variáveis o problema terá (ex: 2 = x1, x2): ")

def constraints_num():
    return st.number_input(
        "Quantas restrições o problema tem? (desconsidere a restrição de não-negatividade) ")

def define_gains(x_gain):
    return st.number_input(f"Digite o ganho da váriàvel x{x_gain} (ex: 7.8): ")

def define_objective():
    return st.text_input("Você quer maximizar ou minimizar o problema? ")

def show_results(status, objective, variables, max_gain):
    st.write(status)
    st.write(objective)
    st.write(variables)
    st.write(max_gain)