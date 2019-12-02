from copy import copy


def run(program: [int]) -> [int]:
    pc = 0

    while program[pc] != 99:

        op = program[pc]
        if op == 1:
            program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
        elif op == 2:
            program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]

        pc += 4

    return program


def find_inputs(program: [int], result: int) -> (int, int):
    for i in range(0, 100):
        for j in range(0, 100):
            clone = copy(program)
            clone[1] = i
            clone[2] = j
            if run(clone)[0] == result:
                return i, j

    raise Exception('Could not find input pair that results in {}'.format(result))


if __name__ == '__main__':
    with open('input.txt') as f:
        program = [int(x) for x in str.split(f.read(), ',')]
        program[1] = 12
        program[2] = 2
        result = run(copy(program))

        print('Answer 1: {}'.format(result[0]))

        noun, verb = find_inputs(copy(program), 19690720)
        result = 100 * noun + verb

        print('Answer 2: {}'.format(result))
