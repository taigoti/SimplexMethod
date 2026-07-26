import re
from app.models.web_view import *

def set_constraints(constraints: list) -> list[list]:
    format = r'(?<!x)\d+'  # Este padrão busca números (\d+), mas ignora se tiver um 'x' colado antes dele (Negative Lookbehind)
    coeficients = []

    for i in constraints:
        result = re.findall(format, constraints[i])

        coeficients.append(
            [int(num) for num in result])

    return coeficients


def set_objective(objective: str) -> bool:
    objective = objective.strip().lower()

    while objective == "" or objective == "m":
        objective = str(input(invalid_format()))

    if "maximizar".startswith(objective):
        return True
    if "minimizar".startswith(objective):
        return False
    else:
        return True

def build_data(variables: list, gains: list, constraints: list, objective: bool) -> dict[str, list | bool]:
    data = {
        "variables": variables,
        "gains": gains,
        "constraints": constraints,
        "toMaximize": objective
    }

    return data

def set_expressions() -> dict[str, list | bool]:
    while True:
        try:
            variables, gains, constraints, objective = input_problem()
            constraints = set_constraints(constraints)
            print(constraints)
            return build_data(variables, gains, constraints, objective)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")