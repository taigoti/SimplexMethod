from pulp import LpVariable, LpProblem, LpMaximize

def get_vars(data):
    variablesDict = {}
    k = 0

    while k < len(data):
        key = data[k]

        value = LpVariable(data[k], lowBound=0, cat="Continuous")
        variablesDict[key] = value
        k += 1

    return variablesDict


class BuildProblem():
    def __init__(self, data):
        self.variables = get_vars(data.get("variables"))
        self.gains = data.get("gains")
        self.constraints = data.get("constraints")
        self.problem = LpProblem("Optimization_Problem", LpMaximize)

    def get_keys(self):
        return self.variables

    def get_gains(self):
        return self.gains

    def get_constraints(self):
        return self.constraints

    def get_problem(self):
        return self.problem

    def get_objective_function(self):
        x1 = self.variables.get("x1")
        x2 = self.variables.get("x2")

        return (self.gains[0] * x1) + (self.gains[1] * x2)