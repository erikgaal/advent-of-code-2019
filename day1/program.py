def calculate_fuel(mass: int) -> int:
    return mass // 3 - 2


def calculate_fuel_recursive(mass: int) -> int:
    fuel = max(0, calculate_fuel(mass))
    if fuel > 0:
        fuel += calculate_fuel_recursive(fuel)

    return fuel


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print('Answer 1: {}'.format(sum([calculate_fuel(int(x)) for x in lines])))
        print('Answer 2: {}'.format(sum([calculate_fuel_recursive(int(x)) for x in lines])))
