#!/usr/bin/env python3
import operator
import random


def generate_number():
    return random.randint(1, 100)


def generate_expression():
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    num1 = generate_number()
    num2 = generate_number()
    op = random.choice(list(operations.keys()))
    return num1, op, num2, operations[op](num1, num2)
