def find_loop_size(encryption_key):
    value = 1
    subject_number = 7
    loop_size = 0
    while value != encryption_key:
        value = (value * subject_number) % 20201227
        loop_size += 1
    return loop_size


def create(loop_size, subject_number):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


with open("input.txt") as fp:
    data = (int(fp.readline().strip()), int(fp.readline().strip()))

print(create(find_loop_size(data[0]), data[1]))
