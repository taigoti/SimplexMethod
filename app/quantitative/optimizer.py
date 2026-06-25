from pulp import *
from app.quantitative.exceptions import SolucaoInviavelError, SolucaoIlimitadaError

def optimize_problem(x1Gain, x2Gain):
    prob = LpProblem("Optimization_Problem", LpMaximize)

    x1 = LpVariable("x1", lowBound=0, cat = "Integer")  # Variable x1
    x2 = LpVariable("x2", lowBound=0, cat = "Continuous")  # Variable x2

    prob += (x1Gain * x1) + (x2Gain * x2)  # Objective function

    prob += 2 *x1 + 4 * x2 <= 35  # Constraint 1
    prob += 4 * x1 + 2 * x2 <= 42  # Constraint 2

    status = prob.solve()
    problem_status = LpStatus[status]  # Solve the problem
    checkStatus(problem_status)

    print(f"Status do Algoritmo: {problem_status}")
    print(f"Quantidade Ótima do Produto A: {value(x1)}")
    print(f"Quantidade Ótima do Produto B: {value(x2)}")
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

if __name__ == "__main__":
    optimize_problem(5, 3)  # Exemplo de ganhos para x1 e x2