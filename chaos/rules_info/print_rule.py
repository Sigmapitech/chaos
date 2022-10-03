import pathlib
import sys

from .rule_spec import RuleSpec


def print_rule(rule):
    c_bin = sys.argv[0]

    path = '/'.join(c_bin.split('/')[:-3]) + '/chaos/rules_info'

    first_char = rule[0]
    content = pathlib.Path(f'{path}/C-{first_char}/C-{rule}.rule_spec').read_text()
    print(parse_rule_spec(content))


def parse_rule_spec(rule_spec):
    data = {}
    for line in rule_spec.split('@'):
        if not line:
            continue

        key, value, *fp = line.split(':')
        if fp:
            value += ':' + ':'.join(fp)

        data[key] = value.strip()

    return RuleSpec(**data)
