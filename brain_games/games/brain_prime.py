#!/usr/bin/env python3
import random


def generate_number():
    return random.randint(1, 100)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
