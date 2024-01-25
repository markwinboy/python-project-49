#!/usr/bin/env python3
import random


def generate_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0
