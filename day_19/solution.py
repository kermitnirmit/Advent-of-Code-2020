# Bascially copied this one from reddit.. :/
import regex

f = open('input.txt').read().strip().split("\n\n")

rules = f[0].split('\n')
messages = f[1].split("\n")

rules = dict(r.replace('"', "").split(": ", 1) for r in rules)


def solve(rules, messages):
    def expand(value):
        if not value.isdigit(): return value
        return "(?:" + "".join(map(expand, rules[value].split())) + ")"

    r = regex.compile(expand("0"))
    return sum(r.fullmatch(m) is not None for m in messages)

print(solve(rules, messages))

rules["8"] = "42 +"
rules["11"] = "(?P<R> 42 (?&R)? 31 )"

print(solve(rules, messages))