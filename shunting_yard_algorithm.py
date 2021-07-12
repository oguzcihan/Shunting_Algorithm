import sys


def order(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/' or operator=='^':
        return 2
    return 0


def operatorAccept(x, y, operator):
    if operator == '+': return x + y
    if operator == '-': return x - y
    if operator == '*': return x * y
    if operator == '/': return x // y
    if operator == '^': return x ** y


def calculate(expressions):
    values = []
    operators = []
    z = 0
    while z < len(expressions):

        if expressions[z] == ' ':
            z += 1
            continue

        elif expressions[z] == '(':
            operators.append(expressions[z])

        elif expressions[z].isdigit():
            val = 0
            while (z < len(expressions) and
                   expressions[z].isdigit()):
                val = (val * 10) + int(expressions[z])
                z += 1

            values.append(val)
            z -= 1

        elif expressions[z] == ')':

            while len(operators) != 0 and operators[-1] != '(':
                values2 = values.pop()
                values1 = values.pop()
                op = operators.pop()

                values.append(operatorAccept(values1, values2, op))

            operators.pop()

        else:
            while (len(operators) != 0 and
                   order(operators[-1]) >=
                   order(expressions[z])):
                values2 = values.pop()
                values1 = values.pop()
                op = operators.pop()
                values.append(operatorAccept(values1, values2, op))
            operators.append(expressions[z])
        z += 1

    while len(operators) != 0:
        values2 = values.pop()
        values1 = values.pop()
        ope = operators.pop()
        values.append(operatorAccept(values1, values2, ope))
    return values[-1]


if __name__ == "__main__":

    while True:
        try:

            exp=input("Enter Expression =>")
            if exp.lower() == "q":
                sys.exit(0)
            else:
                print(calculate(str(exp)))

        except BaseException as ex:
            print(ex)