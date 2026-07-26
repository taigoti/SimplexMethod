import streamlit as st
import time

def initialize_page():
    st.set_page_config(page_title="Simplex Solver", layout="centered")
    st.title("Método Simplex")
    st.write("Vamos iniciar! Preencha as informações seguindo o formato correto.")

def executing(optimize_problem, *args, **kwargs):
    with st.spinner('Executando...'):
        time.sleep(2)
        optimize_problem(*args, **kwargs)

def show_results(status, objective, variables, max_gain):
    st.write(status)
    st.write(objective)
    st.write(variables)
    st.write(max_gain)

def input_problem():
    gains_array = []
    cons_array = []

    vars = st.number_input(
        "Digite quantas variáveis o problema terá (ex: 2 = x1, x2): ",
        min_value=2)

    for i in range(vars):
            gains_array.append(
                st.number_input(f"Digite o ganho da váriàvel x{i+1} (ex: 7.8): ",
                                key=f"gain_{i}"))

    if "confirm_gains" not in st.session_state:
        st.session_state.confirm_gains = False

    if st.button("Confirmar Lucro das Variáveis", key="gain"):
        st.session_state.confirm_gains = True

    st.write("---")

    if st.session_state.confirm_gains:
        cons = st.number_input(
                "Quantas restrições o problema tem? (desconsidere a restrição de não-negatividade) ",
                min_value=1)

        for i in range(cons):
            cons_array.append(
                st.text_input(f"Digite a {i+1}ª restrição: ",
                              placeholder=f"ex: {i+1}x1 + {i}x2 + {i+2}x3 <= 15",
                              key=f"cons_{i}"))

        if "confirm_cons" not in st.session_state:
            st.session_state.confirm_cons = False

        if st.button("Confirmar Restrições", key="cons"):
            st.session_state.confirm_cons = True

        st.write("---")

        if st.session_state.confirm_cons:
            obj = st.text_input("Você quer maximizar ou minimizar o problema",
                          placeholder="max/min",
                          key=f"objective")

            if "confirm_obj" not in st.session_state:
                st.session_state.confirm_obj = False

            if st.button("Confirmar Restrições", key="obj"):
                st.session_state.confirm_obj = True

            st.write("---")

            if st.session_state.confirm_obj:
                st.write(vars, cons, cons_array, obj)