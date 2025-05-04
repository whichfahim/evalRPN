import operator

def evalRPN(tokens):
    postFix = []
    operators = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv } # etc.

    for op in tokens:
        if op in operators:
            #and stack is not empty
            oper1 = postFix.pop()
            oper2 = postFix.pop()
            res = int(operators[op](oper2,oper1))
            postFix.append(res)
        else:
            postFix.append(int(op))
    return postFix[-1]

tokens=["18"]
print(evalRPN(tokens))
# Output: 18


tokens = ["1","2","+","3","*","4","-"]
print(evalRPN(tokens))
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
# Output: 22

# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

