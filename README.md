# 🧮 Evaluate Reverse Polish Notation (RPN)

This repository contains a Python implementation of a Reverse Polish Notation (RPN) expression evaluator. It parses and evaluates a list of tokens representing a postfix (RPN) expression and returns the result.

## 🔍 Problem Statement

Given an array `tokens` that represents an arithmetic expression in Reverse Polish Notation, evaluate the expression.

**Valid operators** are: `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Division between two integers should truncate toward zero.

## ✅ Features

- Supports all four basic arithmetic operations: addition, subtraction, multiplication, and division.
- Handles negative numbers and complex nested expressions.
- Ensures results are always integers (using `int()` for truncation toward zero).

## 🧠 Code Overview

```python
import operator

def evalRPN(tokens):
    postFix = []
    operators = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv }

    for op in tokens:
        if op in operators:
            oper1 = postFix.pop()
            oper2 = postFix.pop()
            res = int(operators[op](oper2, oper1))
            postFix.append(res)
        else:
            postFix.append(int(op))
    return postFix[-1]
```
## 🧪 Example Usage
```python
tokens = ["18"]
print(evalRPN(tokens))  # Output: 18

tokens = ["1", "2", "+", "3", "*", "4", "-"]
print(evalRPN(tokens))  # Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))  # Output: 22
# Explanation:
# ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 22
```

## ⏱ Time and Space Complexity
Time Complexity: O(n)
Each token is processed exactly once in a single pass through the list.

Space Complexity: O(n)
In the worst case, all tokens are operands, leading to n elements being pushed onto the stack.

## 📂 Files
eval.py: Core implementation of the RPN evaluator.

README.md: Project documentation.

## 🧑‍💻 Author
Fahim Imtiaz <br>
[LinkedIn](https://www.linkedin.com/in/fahim-imtiaz/)
[Github](https://github.com/whichfahim)
