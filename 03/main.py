import re


def read_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def remove_disabled_input_from_data(data: str) -> str:
    result = re.sub(r"don't\(\).*?do\(\)", "", data, flags=re.DOTALL)
    return result


def read_mul_instructions(data: str) -> list[tuple[int, int]]:
    results = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

    return results


def calc_isntructions(muls: list[tuple[int, int]]) -> int:
    return sum([int(a) * int(b) for a, b in muls])


def main():
    input = read_input("03/input1.txt")
    instructions = read_mul_instructions(input)
    result = calc_isntructions(instructions)
    print(f"Result: {result}")

    input = remove_disabled_input_from_data(input)
    instructions = read_mul_instructions(input)
    result = calc_isntructions(instructions)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
