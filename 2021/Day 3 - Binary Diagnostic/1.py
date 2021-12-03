from collections import Counter


# Find most and least repeating bit in given index
def repeating_bits(n: list[str], index: int) -> tuple:
    """
    Find most and least repeating bit in given index
    :param n: list of numbers as strings
    :param index: index of bit to find
    :return: tuple of most and least repeating bit
    """
    bits = [int(i[index]) for i in n]
    c = Counter(bits)
    return c.most_common()[0][0], c.most_common()[-1][0]


with open("input.txt") as fp:
    binary_numbers = [line.strip() for line in fp.readlines()]

    # For each index, find most and least repeating bit
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(binary_numbers[0])):
        most, least = repeating_bits(binary_numbers, i)
        gamma_rate += str(most)
        epsilon_rate += str(least)

    # Multiply gamma and epsilon rates
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print(gamma_rate * epsilon_rate)
