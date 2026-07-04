import re

def set_variables(num: int) -> list[str]:
    variables = []
    k = 1

    while True:
        try:
            while k <= num:
                variables.append("x" + str(k))
                k += 1

            break
        except ValueError:
            print("Digite um número inteiro!")

    return variables

def set_gains(variables: int) -> list[float]:
    gains = []
    x = 1

    while True:
        try:
            while x <= variables:
                gain = float(
                    input(f"Digite o ganho da váriàvel x{x} (ex: 7.8): "))
                gains.append(gain)
                x += 1
            break
        except ValueError:
            print("Digite um valor válido!")

    return gains

def set_constraints(num: int) -> list[list]:
    format = r'(?<!x)\d+'  # Este padrão busca números (\d+), mas ignora se tiver um 'x' colado antes dele (Negative Lookbehind)
    constraints = []
    k = 1

    while True:
        try:
            while k <= num:
                constraint = str(
                    input(f"Digite a {k}ª restrição (ex: 3x1 + 0x2 + 1x3 <= 15): "))

                result = re.findall(format, constraint)  #Faz a busca de acordo com a formatação
                constraints.append(
                    [int(num) for num in result])

                k += 1
            break
        except ValueError:
            print("Digite no formato correto!")

    return constraints

def set_objective(objective: str) -> bool:
    objective = objective.strip().lower()

    while objective == "" or objective == "m":
        objective = str(input("Digite um objetivo válido!! (max ou min)"))

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
            variables = int(
                input("Digite quantas variáveis o problema terá (ex: 2 = x1, x2): "))
            variables = set_variables(variables)

            gains = set_gains(len(variables))

            constraints = int(
                input("Quantas restrições o problema tem? (desconsidere a restrição de não-negatividade) "))
            constraints = set_constraints(constraints)

            obj = str(input("Você quer maximizar ou minimizar o problema? "))
            objective = set_objective(obj)

            return build_data(variables, gains, constraints, objective)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")