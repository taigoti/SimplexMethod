from app.models.data_format import set_expressions
from app.quantitative.optimizer import optimize_problem
from app.models.web_view import initialize_page, executing, input_problem

if __name__ == "__main__":
    initialize_page()
    input_problem()

    #problem = set_expressions()
    #executing(optimize_problem, problem)