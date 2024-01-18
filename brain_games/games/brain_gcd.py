#!/usr/bin/env python3
from brain_games import engine
import prompt
import math


def game_loop(name):
    print("Find the greatest common divisor of given numbers.")
    for _ in range(3):
        num1 = engine.generate_number()
        num2 = engine.generate_number()
        print(f"Question: {num1} {num2}")
        answer = prompt.integer('Your answer: ')
        correct_answer = math.gcd(num1, num2)
        engine.check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def main():
    name = engine.welcome_user()
    game_loop(name)


if __name__ == '__main__':
    main()
