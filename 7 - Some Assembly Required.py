operation_map = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
    'NOT': lambda x: ~ x
}

circuit = {}
nums_str = set([str(x) for x in xrange(10)] + range(10))


def parse_input(s):
    for line in s.split('\n'):
        line = line.split()
        if not line: 
            continue
        var = line[-1]
        exp = line[:-2]
        circuit[var] = exp
    return circuit


def evaluate(var):
    # 2
    if var[0] in nums_str:
        return int(var)
    
    expression = circuit[var]
    if type(expression) ==  int:
        return expression

    len_expression = len(expression)    
    if len_expression < 2:
        if is_num_str(expression):
            # 'c': ['46']
            circuit[var] = int(expression[0])
        else:
            # 'c': ['lx']
            circuit[var] = evaluate(expression[0])

    # 'cs': ['NOT', 'cr']
    elif len_expression < 3:
        num1 = expression[-1]
        num1 = evaluate(num1)
        circuit[var] = operation_map['NOT'](num1)
    # 'da': ['cz', 'OR', 'cy']
    else:
        num1, num2 = expression[0], expression[2]
        num1, num2 = evaluate(num1), evaluate(num2)
        op = expression[1]
        circuit[var] = operation_map[op](num1, num2)

    return circuit[var]


def is_num_str(expression):
    return expression[0] in nums_str or expression[0][1] in nums_str

from pprint import pprint
# pprint(parse_input(open('input.txt').read()))
parse_input(open('input.txt').read())

print evaluate('a')
# pprint(circuit)
