#!/usr/bin/env python3
from brain_games import common
import prompt


def game_loop(name):
    print("What is the result of the expression?")
    for _ in range(3):
        num1, op, num2, correct_answer = common.generate_expression()
        print(f"Question: {num1} {op} {num2}")
        answer = prompt.integer('Your answer: ')

        common.check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def main():
    name = common.welcome_user()
    game_loop(name)


if __name__ == '__main__':
    main()
