import prompt
from brain_games.games import brain_calc
from brain_games.games import brain_even
from brain_games.games import brain_gcd
from brain_games.games import brain_prime
from brain_games.games import brain_progression


number_attempts = 3

# def generate_expression():
#     operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}
#     num1 = generate_number()
#     num2 = generate_number()
#     op = random.choice(list(operations.keys()))
#     return num1, op, num2, operations[op](num1, num2)


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def check_output(answer, name, correct_answer):
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(.\
              Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        exit()


def brain_calc_func():
    name = welcome_user()
    print("What is the result of the expression?")
    for _ in range(number_attempts):
        num1, op, num2, correct_answer = brain_calc.generate_expression()
        print(f"Question: {num1} {op} {num2}")
        answer = prompt.integer('Your answer: ')
        check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def brain_even_func():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(number_attempts):
        number = brain_even.generate_number()
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct_answer = "yes" if brain_even.is_even(number) else "no"
        check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def brain_gcd_func():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for _ in range(number_attempts):
        num1 = brain_gcd.generate_number()
        num2 = brain_gcd.generate_number()
        print(f"Question: {num1} {num2}")
        answer = prompt.integer('Your answer: ')
        correct_answer = brain_gcd.math_gcd(num1, num2)
        check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def brain_prime_func():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(number_attempts):
        number = brain_prime.generate_number()
        print(f"Question: {number}")
        correct_answer = "yes" if brain_prime.is_prime(number) else "no"
        answer = prompt.string("Your answer: ")
        check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def brain_progression_func():
    name = welcome_user()
    print("What number is missing in the progression?")
    for _ in range(number_attempts):
        progression, correct_answer = brain_progression.generate_progression()
        print(f"Question: {' '.join(map(str, progression))}")
        answer = prompt.integer('Your answer: ')
        check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")
