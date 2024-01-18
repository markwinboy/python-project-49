#!/usr/bin/env python3
from brain_games import common
import prompt


def game_loop(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = common.generate_number()
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct_answer = "yes" if common.is_even(number) else "no"
        common.check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def main():
    name = common.welcome_user()
    game_loop(name)


if __name__ == '__main__':
    main()
