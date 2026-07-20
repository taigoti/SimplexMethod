from pulp import *

from app.models.web_view import show_results
from app.quantitative.exceptions import *
from app.models.problem_builder import BuildProblem

def optimize_problem(problem_dict):
    problem = BuildProblem(problem_dict) # Build do problema (variáveis, ganhos, restrições, função objetivo)
    prob = problem.get_problem() # Associa o problema à variàvel

    prob += problem.get_objective_function() # Função objetivo

    constraints = problem.get_constraints()
    for constraint in constraints.values():
        prob += constraint

    status = prob.solve()  # Resolve o problema
    problem_status = LpStatus[status]  # Verifica o status do problema
    check_status(problem_status)  # Verifica as exceções

    show_results(problem_status, problem.get_objective_function(), problem.get_vars(), value(prob.objective))
    print("=========================================================")

    print(f"Status do Algoritmo: {problem_status}")
    print(f"Função Objetivo: L = {problem.get_objective_function()}")

    for x in problem.get_vars():
        print(f"Quantidade Ótima do {x}: {value(problem.get_vars()[x])}")

    print(f"Lucro Máximo Possível: R$ {value(prob.objective)}")

    print("=========================================================")

def check_status(status):
    if status == "Infeasible":
        # Se o PuLP disser que é inviável, lança exceção
        raise SolucaoInviavelError()

    if status == "Unbounded":
        # Se o PuLP disser que é ilimitado, lança exceção
        raise SolucaoIlimitadaError()

    if status != "Optimal":
        # Qualquer outro erro
        raise ModelizacaoError(f"O solver falhou com o status: {status}")