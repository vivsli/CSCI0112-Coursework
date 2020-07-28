import pytest

from math_problem import *


def test_random_number_generator():
    # normal case: it's random so I called it a couple times and asserted each time that it't within its given range
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    random_number = random_number_generator()
    random_number1 = random_number_generator()
    random_number2 = random_number_generator()
    assert random_number in num_list
    assert random_number1 in num_list
    assert random_number2 in num_list


def test_init_math_problem():
    # normal case: passing in arguments and asserting that they are the same
    problem1 = MathProblem(4, 5, operator.mul)
    assert problem1.number1 == 4
    assert problem1.number2 == 5
    assert problem1.operation == operator.mul
    assert problem1.answer == 20

    # edge case: passing in an operation that isn't add, sub, mul, truediv
    with pytest.raises(ValueError):
        assert MathProblem(20, 5, operator.floordiv)

    # edge case: trying to divide by zero, in my code I change the 0 denominator to a 1
    problem2 = MathProblem(2, 0, operator.truediv)
    assert problem2.number2 == 1

    # edge case: answer is a fraction: I handled this potential issue by checking first to see if the answer would be
    # fraction, and if so I would decrement the second number by one until the answer was no longer a fraction
    problem3 = MathProblem(10, 6, operator.truediv)
    assert problem3.answer == 2


def test_print_problem():
    # normal case: print exactly as according to its arguments
    problem = MathProblem(2, 7, operator.add)
    assert MathProblem.print_problem(problem) == "2 + 7"
    problem1 = MathProblem(4, 5, operator.mul)
    assert MathProblem.print_problem(problem1) == "4 x 5"


def test_random_problem_generator():
    # normal case: operation corresponds with argument, numbers range from 0 to 20
    problem = random_problem_generator(operator.sub)
    assert problem.operation == operator.sub
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert (problem.number1 in num_list) and (problem.number2 in num_list)

    # edge case: any invalid operation will throw Value Error
    with pytest.raises(ValueError):
        assert random_problem_generator(operator.countOf)


def test_diagnostic_test_generator():
    # normal case: the returned problem set is composed of problem objects
    # length is right, same number of add, sub, mul, and div problems
    diagnostic_test = diagnostic_test_generator()
    operation_count_dictionary = {operator.add: 0, operator.sub: 0, operator.mul: 0, operator.truediv: 0}
    # this dictionary will count the number of problems in the test under each operation
    for problem in diagnostic_test:
        assert type(problem) == MathProblem
        operation_count_dictionary[problem.operation] += 1
    operation_list = [operator.add, operator.sub, operator.mul, operator.truediv]
    for operation in operation_list:
        assert operation_count_dictionary[operation] == 3
    assert len(diagnostic_test) == 12


def test_personalized_test_generator():
    # normal case: uses operation incorrect dictionary correctly (right number of problems for each operation)
    operation_incorrect_dictionary = {operator.add: 3, operator.sub: 0, operator.mul: 2, operator.truediv: 6}
    personalized_test = personalized_test_generator(operation_incorrect_dictionary)
    operation_count_dictionary = {operator.add: 0, operator.sub: 0, operator.mul: 0, operator.truediv: 0}
    for problem in personalized_test:
        assert type(problem) == MathProblem
        operation_count_dictionary[problem.operation] += 1
    assert operation_count_dictionary == operation_incorrect_dictionary

    # edge case: empty dictionary
    operation_incorrect_dictionary2 = {}
    assert personalized_test_generator(operation_incorrect_dictionary2) == []





