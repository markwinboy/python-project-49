#!/usr/bin/env python3
import prompt
import random


def check_number(number):
    if number%2 == 0:
        return "yes"
    else:
        return "no"


def test_number(name):
    for i in range(3):
        number = random.randint(0, 100)
        print(f"Question: {number}")

        answer = prompt.string('Your answer: ')

        if check_number(number) == answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{check_number(number)}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")



def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    test_number(name)


def main():
    welcome_user()

if __name__ == '__main__':
    main()


