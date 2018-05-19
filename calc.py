from flask import request

def main():
    num_1 = request.args.get('num_1', '', int)
    num_2 = request.args.get('num_2', '', int)
    operator = request.args.get('operator', '')

    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2

    return str(result)
