#!/usr/bin/env python3
from brain_games import common
import prompt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def game_loop(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = common.generate_number()
        print(f"Question: {number}")
        correct_answer = "yes" if is_prime(number) else "no"
        answer = prompt.string("Your answer: ")
        common.check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def main():
    name = common.welcome_user()
    game_loop(name)


if __name__ == '__main__':
    main()
