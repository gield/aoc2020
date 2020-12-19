import math


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


def get_parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents).

    Source: https://stackoverflow.com/a/4285211/940918
    """
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])


def solve(s):
    # Solve the parentheses first, from deepest to shallowest
    while p_contents := list(get_parenthetic_contents(s)):
        sorted_p_contents = sorted(p_contents, key=lambda t: -t[0])
        max_depth = sorted_p_contents[0][0]
        for depth, p_content in sorted_p_contents:
            if depth < max_depth:
                continue
            s = s.replace(f"({p_content})", str(solve(p_content)))

    # Solve with + taking precedence over *
    literals = s.split()
    result = [int(literals[0])]
    for lit in literals[1:]:
        if lit == "+":
            take_sum = True
        elif lit == "*":
            take_sum = False
        elif take_sum:
            result[-1] += int(lit)
        else:
            result.append(int(lit))
    return math.prod(result)


print(sum(solve(line) for line in lines))
