from pulp import *
from app.quantitative.exceptions import SolucaoInviavelError, SolucaoIlimitadaError

def optimize_problem(data):
    vars = data.get("variables")
    gains = data.get("gain")
    constraints = data.get("constraints")
    prob = LpProblem("Optimization_Problem", LpMaximize)

    variablesDict = dynamic_vars(vars)
    x1 = variablesDict.get("x1")
    x2 = variablesDict.get("x2")
    prob += (gains[0] * x1) + (gains[1] * x2)  # Objective function

    prob += (constraints[0][0] * x1) + (constraints[0][1]) * x2 <= 35  # Constraint 1
    prob += (constraints[1][0]) * x1 + (constraints[1][1] * x2) <= 42  # Constraint 2

    status = prob.solve()
    problem_status = LpStatus[status]  # Solve the problem
    checkStatus(problem_status)

    print(f"Status do Algoritmo: {problem_status}")

    for x in variablesDict.keys():
        print(f"Quantidade Ótima do {x}: {value(variablesDict[x])}")

    print(f"Lucro Máximo Possível: R$ {value(prob.objective)}")


def checkStatus(status):
    if status == "Infeasible":
        # Se o PuLP disser que é inviável, lançamos o nosso erro customizado
        raise SolucaoInviavelError()

    if status == "Unbounded":
        # Se o PuLP disser que é ilimitado, lançamos o nosso erro customizado
        raise SolucaoIlimitadaError()

    if status != "Optimal":
        # Para qualquer outro status de erro genérico do solver
        from app.quantitative.exceptions import ModelizacaoError
        raise ModelizacaoError(f"O solver falhou com o status: {status}")


def dynamic_vars(vars):
    variablesDict = {}
    k = 0

    while k < len(vars):
        key = vars[k]

        value = LpVariable(vars[k], lowBound=0, cat="Continuous")
        variablesDict[key] = value
        k += 1

    return variablesDict


if __name__ == "__main__":
    data = {
        "variables": ["x1", "x2"],
        "gain": [3, 5],
        "constraints": [
            [2, 1], [1, 2]
        ]
    }

    optimize_problem(data)  # Exemplo de ganhos para x1 e x2