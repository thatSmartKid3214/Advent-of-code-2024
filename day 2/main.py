import os
from copy import deepcopy

filename = "input.txt"
with open(filename, "r") as file:
    data = file.read(os.path.getsize(filename))
    file.close()

data = data.split('\n')


def part1():
    total_safe = 0
    for i, line in enumerate(data):
        line = [int(x) for x in line.split(" ")]
        safe = True
        if line[1] < line[0]: # Decreasing
            for j in range(len(line)):
                if j > 0:
                    if not ((line[j] - line[j-1]) in [-1, -2, -3]):
                        safe = False
                        break
        elif line[1] > line[0]: # Increasing
            for j in range(len(line)):
                if j > 0:
                    if not ((line[j] - line[j-1]) in [1, 2, 3]):
                        safe = False
                        break
        else: # This means that the second and first number are the same
            safe = False 
        

        if safe:
            total_safe += 1
            #print("line", i+1, "is safe")

    print("part 1:", total_safe)

def test(l, index):
    # Brute force it
    for i in range(len(l)):
        line = deepcopy(l)
        line.pop(i)

        safe = True
        if line[1] < line[0]: # Decreasing
            for j in range(len(line)):
                if j > 0:
                    if not ((line[j] - line[j-1]) in [-1, -2, -3]):
                        safe = False
                        break
            if safe == True:
                return True
        elif line[1] > line[0]: # Increasing
            for j in range(len(line)):
                if j > 0:
                    if not ((line[j] - line[j-1]) in [1, 2, 3]):
                        safe = False
                        break
            if safe == True:
                return True
        else: # This means that the second and first number are the same
            continue
    

def part2():
    total_safe = 0
    problems = []
    problem_indexes = []
    for i, line in enumerate(data):
        line = [int(x) for x in line.split(" ")]
        problem_count = 0
        problem_indexes.append([])

        if line[1] < line[0]: # Decreasing
            for j in range(len(line)):
                if j > 0:
                    if not ((line[j] - line[j-1]) in [-1, -2, -3]):
                        problem_count += 1
                        problem_indexes[i].append(j)
        elif line[1] > line[0]: # Increasing
            for j in range(len(line)):
                if j > 0:
                    if not ((line[j] - line[j-1]) in [1, 2, 3]):
                        problem_count += 1
                        problem_indexes[i].append(j)
        else: # This means that the second and first number are the same
            problem_count += 1
            problem_indexes[i].append(0)
            if line[2] < line[1]: # Decreasing
                for j in range(len(line)):
                    if j > 1:
                        if not ((line[j] - line[j-1]) in [-1, -2, -3]):
                            problem_count += 1
                            problem_indexes[i].append(j)
            elif line[2] > line[1]: # Increasing
                for j in range(len(line)):
                    if j > 1:
                        if not ((line[j] - line[j-1]) in [1, 2, 3]):
                            problem_count += 1
                            problem_indexes[i].append(j)
            else:
                problem_count += 1
                problem_indexes[i].append(1)

        problems.append(problem_count)

    print(problems)
    for i in range(len(problems)):
        if problems[i] == 0:
            total_safe += 1
        else:
            line = [int(x) for x in data[i].split(" ")]
            if test(line, problem_indexes[i][0]):
                total_safe += 1
        

    print("part 2:", total_safe)
        

part1()
part2()


