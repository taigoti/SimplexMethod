from pulp import LpVariable, LpProblem, LpMaximize

def build_vars(data):
    variablesDict = {}
    k = 0

    while k < len(data):
        key = data[k]

        value = LpVariable(data[k], lowBound=0, cat="Continuous")
        variablesDict[key] = value
        k += 1

    return variablesDict

def build_constraints(matrix, x1, x2):
    constraintsDict = {}
    k = 0

    while k < len(matrix):
        key = "y" + str(k + 1)

        value = (matrix[k][0] * x1) + (matrix[k][1] * x2) <= matrix[k][2]
        constraintsDict[key] = value
        k += 1

    return constraintsDict


class BuildProblem():
    def __init__(self, data):
        constraints_matrix = data.get("constraints")
        variables_array = data.get("variables")

        self.variables = build_vars(variables_array)
        self.gains = data.get("gains")
        self.constraints = build_constraints(
            constraints_matrix, self.variables.get("x1"), self.variables.get("x2")
        )
        self.problem = LpProblem("Optimization_Problem", LpMaximize)

    def get_vars(self):
        return self.variables

    def get_gains(self):
        return self.gains

    def get_constraints(self, constraint):
        return self.constraints.get(constraint)

    def get_problem(self):
        return self.problem

    def get_objective_function(self):
        x1 = self.variables.get("x1")
        x2 = self.variables.get("x2")

        return (self.gains[0] * x1) + (self.gains[1] * x2)