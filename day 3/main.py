import os
import re

filename = "input.txt"
with open(filename, "r") as file:
    data = file.read(os.path.getsize(filename))
    file.close()


def part1():
    d = data.split('\n')
    total = 0
    regex = re.compile(r"mul(\(\d+,\d+\))")

    for line in d:

        for mul in regex.finditer(line):
            #print(mul.group())
            numbers = mul.group().split(',')
            numbers[0] = int(numbers[0].split("mul(")[-1])
            numbers[1] = int(numbers[1].split(")")[0])

            total += numbers[0]*numbers[1]


    print("part1:", total)

def part2():
    total = 0
    func_re = re.compile(r"do\w*\'*\w*\(\)")
    regex = re.compile(r"mul(\(\d+,\d+\))")

    seq = []

    is_do = False
    new_line = ""
    for i, func in enumerate(func_re.finditer(data)):
        #print(func)
        if func.group() == "do()" and i == 0:
            is_do = True
            new_line += data[0: func.span()[0]]
            seq.append(func)

        if func.group() == "do()" and is_do == False:
            is_do = True
            seq.append(func)
        elif func.group() == "don't()" and is_do == True:
            seq.append(func)
            is_do = False
        
    print(len(seq))

    for i in range(int(len(seq)/2)):
        func1 = seq.pop(0)
        func2 = seq.pop(0)

        #print(func1, func2)

        if func1.group() == "do()" and func2.group() == "don't()":
            span = [func1.span()[0], func2.span()[0]]
            new_line += data[span[0]:span[1]]
    
    #print(new_line)

    
    for mul in regex.finditer(new_line):
        #print(mul.group())
        numbers = mul.group().split(',')
        numbers[0] = int(numbers[0].split("mul(")[-1])
        numbers[1] = int(numbers[1].split(")")[0])

        total += numbers[0]*numbers[1]
        
    print("part2:", total)

part1()
part2()

