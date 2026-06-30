from app.models.data_format import set_expressions
from app.quantitative.optimizer import optimize_problem

if __name__ == "__main__":
    print("=============================================\n")

    print("Bem vindo à resolução com o Método Simplex!")
    print("Vamos iniciar! Preencha as informações seguindo o formato correto.")

    print("\n=============================================\n")

    problem = set_expressions()

    optimize_problem(problem)