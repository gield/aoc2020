with open("input.txt", "r") as f:
    lines = [r.strip() for r in f.readlines()]

raw_instructions = [tuple(line.split()) for line in lines]
instructions = [(op, int(arg)) for op, arg in raw_instructions]


def run(instructions):
    accumulator, pointer = 0, 0
    instructions_ran = set()
    while pointer < len(instructions):
        if pointer in instructions_ran:
            return False
        instructions_ran.add(pointer)
        op, arg = instructions[pointer]
        if op == "acc":
            accumulator += arg
            pointer += 1
        if op == "jmp":
            pointer += arg
        if op == "nop":
            pointer += 1
    return accumulator


for i in range(len(instructions)):
    op, arg = instructions[i]
    if op == "acc":
        continue
    adjusted_instructions = instructions.copy()
    adjusted_instructions[i] = ("jmp" if op == "nop" else "nop", arg)
    output = run(adjusted_instructions)
    if output is not False:
        print(output)
        break
