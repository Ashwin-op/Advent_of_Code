with open("input.txt") as fp:
    rule_section, test_section = fp.read().split('\n\n')
    test_section = test_section.strip().split('\n')


def make_rules(rule_section):
    rules = {}
    for rule in rule_section.strip().split('\n'):
        key, value = rule.split(': ')
        if value[0] == '"':
            value = value[1:-1]
        else:
            value = [[int(r) for r in v.split()] for v in value.split('|')]
        rules[int(key)] = value
    return rules


def check_expression(expression, rule):
    # base
    if len(expression) < len(rule):
        return False
    if len(expression) == 0 or len(rule) == 0:
        return len(expression) == 0 and len(rule) == 0

    current = rule.pop(0)
    if type(current) == str:
        if current == expression[0]:
            return check_expression(expression[1:], rule.copy())
    else:
        for r in rules[current]:
            if check_expression(expression, list(r) + rule.copy()):
                return True
    return False


def count_valid(rules, expressions):
    count = 0
    for expression in expressions:
        start_rule = rules[0][0].copy()
        if check_expression(expression, start_rule):
            count += 1
    return count


rules = make_rules(rule_section)

print(count_valid(rules, test_section))
