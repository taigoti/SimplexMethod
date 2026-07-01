from pulp import *
from app.quantitative.exceptions import *
from app.quantitative.problem_builder import BuildProblem

def optimize_problem(dict):
    problem = BuildProblem(dict) # Build do problema (variáveis, ganhos, restrições, função objetivo)
    prob = problem.get_problem() # Associa o problema à variàvel

    prob += problem.get_objective_function() # Função objetivo

    constraints = problem.get_constraints()
    for constraint in constraints.values():
        prob += constraint

    status = prob.solve()  # Resolve o problema
    problem_status = LpStatus[status]  # Verifica o status do problema
    check_status(problem_status)  # Verifica as exceções

    print("=========================================================")

    print(f"Status do Algoritmo: {problem_status}")
    print(f"Função Objetivo: L_max = {problem.get_objective_function()}")

    for x in problem.get_vars():
        print(f"Quantidade Ótima do {x}: {value(problem.get_vars()[x])}")

    print(f"Lucro Máximo Possível: R$ {value(prob.objective)}")

    print("=========================================================")

def check_status(status):
    if status == "Infeasible":
        # Se o PuLP disser que é inviável, lançamos o nosso erro customizado
        raise SolucaoInviavelError()

    if status == "Unbounded":
        # Se o PuLP disser que é ilimitado, lançamos o nosso erro customizado
        raise SolucaoIlimitadaError()

    if status != "Optimal":
        # Para qualquer outro status de erro genérico do solver
        raise ModelizacaoError(f"O solver falhou com o status: {status}")

if __name__ == "__main__":
    data = {
        "variables": ["x1", "x2", "x3"],
        "gains": [7.8, 8.9, 7.5],
        "constraints": [
            [2, 4, 1, 35], [2, 3, 1, 42], [3, 3, 3, 30]
        ]
    }

    optimize_problem(data)