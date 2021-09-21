import numpy as np

from desdeo_problem.problem import MOProblem
from desdeo_problem.problem import Variable
from desdeo_problem.problem import ScalarObjective


def river_pollution_problem():
    def f_1(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)  # This step is to guarantee that the function works when called with a single decision variable vector as well.
        return -4.07 - 2.27*x[:, 0]

    def f_2(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return -2.60 - 0.03*x[:, 0] - 0.02*x[:, 1] - 0.01 / (1.39 - x[:, 0]**2) - 0.30 / (1.39 + x[:, 1]**2)

    def f_3(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return -8.21 + 0.71 / (1.09 - x[:, 0]**2)

    def f_4(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return -0.96 - 0.96 / (1.09 - x[:, 1]**2)

    def f_5(x: np.ndarray) -> np.ndarray:
        return np.max([np.abs(x[:, 0] - 0.65), np.abs(x[:, 1] - 0.65)], axis=0)

    objective_1 = ScalarObjective(name="f_1", evaluator=f_1)
    objective_2 = ScalarObjective(name="f_2", evaluator=f_2)
    objective_3 = ScalarObjective(name="f_3", evaluator=f_3)
    objective_4 = ScalarObjective(name="f_4", evaluator=f_4)
    objective_5 = ScalarObjective(name="f_5", evaluator=f_5)

    objectives = [objective_1, objective_2, objective_3, objective_4, objective_5]

    x_1 = Variable("x_1", 0.5, 0.3, 1.0)
    x_2 = Variable("x_2", 0.5, 0.3, 1.0)

    variables = [x_1, x_2]

    mo_problem = MOProblem(variables=variables, objectives=objectives)

    return mo_problem


if __name__ == "__main__":
    problem = river_pollution_problem()
    print(problem)
    print(problem.evaluate(np.array([0.5, 0.5])))