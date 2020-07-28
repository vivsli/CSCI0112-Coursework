import operator
import random

"""
to add two numbers: operator.add(x,y) = x+y
to subtract: operator.sub(x,y)
multiply: operator.mul(x,y)
divide: operator.truediv(x,y)
"""


def random_number_generator():
    # returns a random number when called
    return random.randint(0, 20)


class MathProblem:
    def __init__(self, number1: int, number2: int, operation):
        if operation == operator.truediv:
            if number2 == 0:
                number2 = 1
            while number1 % number2 != 0:
                number2 -= 1
        self.number1 = number1
        self.number2 = number2
        if (operation != operator.add and operation != operator.sub and operation != operator.mul and
                operation != operator.truediv):
            raise ValueError("invalid operation!")
        self.operation = operation
        self.answer = int(operation(number1, number2))

    def print_problem(self):
        # will take in a problem object and print it
        if self.operation == operator.add:
            operation_string = "+"

        elif self.operation == operator.sub:
            operation_string = "-"

        elif self.operation == operator.mul:
            operation_string = "x"

        elif self.operation == operator.truediv:
            operation_string = "/"

        return str(self.number1) + " " + operation_string + " " + str(self.number2)


def random_problem_generator(operation):
    # will take in a operation and generate a random problem with that operation
    math_problem = MathProblem(random_number_generator(), random_number_generator(), operation)
    return math_problem


def diagnostic_test_generator():
    # returns a list of problem objects
    problem_set = []
    operation_list = [operator.add, operator.sub, operator.mul, operator.truediv]
    for i in range(0, 3):
        for j in operation_list:
            math_problem = random_problem_generator(j)
            problem_set.append(math_problem)
    print("Welcome to your diagnostic math test!")
    return problem_set


def personalized_test_generator(operation_incorrect_dictionary):
    # returns a list of problem objects based off of the operation_incorrect_dictionary
    personal_problem_set = []
    if len(operation_incorrect_dictionary) == 0:
        return personal_problem_set
    print("We will now begin your personalized test!")
    for operation in operation_incorrect_dictionary:
        for i in range(0, operation_incorrect_dictionary[operation]):
            personal_problem_set.append(random_problem_generator(operation))
    return personal_problem_set


def administer_test(problem_set):
    # this function will take in a problem set and administer it and return an operation_incorrect_dictionary
    if len(problem_set) == 0:
        print("you're too smart for my services.")
        print("come back with someone dumber.")
        print("bye-bye!")
        return
    total_incorrect = 0
    operation_incorrect_dictionary = {operator.add: 0, operator.sub: 0, operator.mul: 0, operator.truediv: 0}
    for problem in problem_set:
        user_answer = int(input("please answer the math problem: \n" + MathProblem.print_problem(problem) + " = "))
        if int(user_answer) != int(problem.answer):
            total_incorrect += 1
            operation_incorrect_dictionary[problem.operation] += 1
    total_score = float((len(problem_set) - total_incorrect) / len(problem_set))
    print("Your total score is: " + str(len(problem_set) - total_incorrect) + " / " + str(len(problem_set)))
    if int(total_score) == 1:
        print("Congratulations! You have completed the test session!")
        operation_incorrect_dictionary = {}
    return operation_incorrect_dictionary


def main():
    operation_incorrect_dictionary = administer_test(diagnostic_test_generator())
    personalized_test = personalized_test_generator(operation_incorrect_dictionary)
    administer_test(personalized_test)


if __name__ == '__main__':
    main()
