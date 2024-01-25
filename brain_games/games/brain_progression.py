#!/usr/bin/env python3
import random


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    progression = [start + step * i for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, correct_answer
