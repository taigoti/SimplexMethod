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
                    input(f"Digite a {k}ª restrição (ex: 3x1 + 0x2 <= 15): "))

                result = re.findall(format, constraint)  #Faz a busca de acordo com a formatação
                constraints.append(
                    [int(num) for num in result])

                k += 1
            break
        except ValueError:
            print("Digite no formato correto!")

    return constraints

def build_data(variables: list, gains: list, constraints: list) -> dict[str, list]:
    data = {
        "variables": variables,
        "gains": gains,
        "constraints": constraints
    }

    return data

def set_expressions() -> dict[str, list]:
    while True:
        try:
            num_variables = int(
                input("Digite quantas variáveis o problema terá (ex: 2 = x1, x2): "))
            variables = set_variables(num_variables)

            gains = set_gains(len(variables))

            num_constraints = int(
                input("Quantas restrições o problema tem? (desconsidere a restrição de não-negatividade)"))
            constraints = set_constraints(num_constraints)

            return build_data(variables, gains, constraints)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")