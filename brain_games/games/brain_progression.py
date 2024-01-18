#!/usr/bin/env python3
from brain_games import engine
import prompt


def game_loop(name):
    print("What number is missing in the progression?")
    for _ in range(3):
        progression, correct_answer = engine.generate_progression()
        print(f"Question: {' '.join(map(str, progression))}")
        answer = prompt.integer('Your answer: ')
        engine.check_output(answer, name, correct_answer)
    print(f"Congratulations, {name}!")


def main():
    name = engine.welcome_user()
    game_loop(name)


if __name__ == '__main__':
    main()
