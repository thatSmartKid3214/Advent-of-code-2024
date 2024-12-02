import os

filename = "input.txt"
with open(filename, "r") as file:
    data = file.read(os.path.getsize(filename))
    file.close()

data = data.split("\n")

def part1():
    left_list = sorted([int(x.split(' ')[0]) for x in data])
    right_list = sorted([int(x.split(' ')[-1]) for x in data])

    total_dis = 0

    for i in range(len(left_list)):
        if left_list[i] > right_list[i]:
            dis = left_list[i] - right_list[i]
        else:
            dis = right_list[i] - left_list[i]

        total_dis += dis

    print("part 1:", total_dis)

def part2():
    left_list = [int(x.split(' ')[0]) for x in data]
    right_list = [int(x.split(' ')[-1]) for x in data]

    similarity_score = 0

    for i in range(len(left_list)):
        count = right_list.count(left_list[i])
        score = left_list[i] * count

        similarity_score += score

    print("part 2:", similarity_score)

part1()
part2()


