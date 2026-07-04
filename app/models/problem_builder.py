from pulp import LpVariable, LpProblem, LpMaximize, LpMinimize

def build_vars(data: list) -> dict:
    variablesDict = {}
    k = 0

    while k < len(data):
        key = data[k]

        value = LpVariable(data[k], lowBound=0, cat="Continuous")
        variablesDict[key] = value
        k += 1

    return variablesDict

def build_constraints(matrix: list, variables: dict, objective: bool) -> dict:
    constraintsDict = {}
    variableValue, k, i = 0, 0, 0
    constraint = None

    while k < len(matrix):
        while i < (len(matrix[k]) - 1):
            variableValue += (matrix[k][i] * variables["x" + str(i+1)])
            i += 1

        if objective:
            constraint = (variableValue <= matrix[k][len(matrix[k]) - 1])
        if not objective:
            constraint = (variableValue >= matrix[k][len(matrix[k]) - 1])

        key = "y" + str(k + 1)

        constraintsDict[key] = constraint
        k += 1
        i, variableValue = 0, 0

    return constraintsDict

def build_problem(to_maximize: bool) -> LpProblem:
    if to_maximize:
        return LpProblem("Maximize_Problem", LpMaximize)

    return LpProblem("Minimize_Problem", LpMinimize)


class BuildProblem:
    def __init__(self, data):
        constraints_matrix = data.get("constraints")
        variables_array = data.get("variables")
        gains_array = data.get("gains")
        objective = data.get("toMaximize")

        self.variables = build_vars(variables_array)
        self.gains = gains_array
        self.constraints = build_constraints(constraints_matrix, self.variables, objective)
        self.problem = build_problem(objective)

    def get_vars(self):
        return self.variables

    def get_gains(self):
        return self.gains

    def get_constraints(self):
        return self.constraints

    def get_problem(self):
        return self.problem

    def get_objective_function(self):
        i, objective = 0, 0

        while i < len(self.variables):
            objective += (self.gains[i] *
                          self.variables.get("x" + str(i + 1)))
            i += 1

        return objective