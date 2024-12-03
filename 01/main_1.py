def parse_data(data: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in data.splitlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    return left, right


def read_input(filename):
    with open(filename) as f:
        return f.read()


def main():
    input = read_input("input1.txt")
    left_list, right_list = parse_data(input)
    disance = calculate_distance(left_list, right_list)
    print(f"Distance: {disance}")

    similarity = calculate_similarity(left_list, right_list)
    print(f"Similarity: {similarity}")


def calculate_similarity(left_list, right_list):
    similarity = 0
    for i in range(len(left_list)):
        left_item = left_list[i]
        similarity += left_item * right_list.count(left_item)

    return similarity


def calculate_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    if len(left_list) != len(right_list):
        raise ValueError("Lists have different length")

    distance = 0
    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])

    return distance


if __name__ == "__main__":
    main()
