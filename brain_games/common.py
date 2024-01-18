import prompt
import random
import operator


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    progression = [start + step * i for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, correct_answer


def generate_expression():
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    num1 = generate_number()
    num2 = generate_number()
    op = random.choice(list(operations.keys()))
    return num1, op, num2, operations[op](num1, num2)


def generate_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def check_output(answer, name, correct_answer):
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. \
              Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        exit()
