from pulp import *
from app.quantitative.exceptions import *
from app.quantitative.problem_builder import BuildProblem

def optimize_problem(dict):
    problem = BuildProblem(dict)
    constraints = problem.get_constraints()
    prob = problem.get_problem()
    vars = problem.get_keys()
    x1 = vars.get("x1")
    x2 = vars.get("x2")

    prob += problem.get_objective_function()  # Objective function

    prob += (constraints[0][0] * x1) + (constraints[0][1]) * x2 <= 35  # Constraint 1
    prob += (constraints[1][0]) * x1 + (constraints[1][1] * x2) <= 42  # Constraint 2

    status = prob.solve()
    problem_status = LpStatus[status]  # Solve the problem
    check_status(problem_status)

    print(f"Status do Algoritmo: {problem_status}")

    for x in vars.keys():
        print(f"Quantidade Ótima do {x}: {value(vars[x])}")

    print(f"Lucro Máximo Possível: R$ {value(prob.objective)}")
    print(problem.variables)

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
        "variables": ["x1", "x2"],
        "gains": [3, 5],
        "constraints": [
            [2, 1], [1, 2]
        ]
    }

    optimize_problem(data)  # Exemplo de ganhos para x1 e x2