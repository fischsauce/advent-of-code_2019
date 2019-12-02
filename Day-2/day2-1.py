file = open("day2_data", "r")

for i in file:
    list = i.split(",")
    # print(list[3])

for i in range(0, len(list)):
    list[i] = int(list[i])

# Restore Gravity!
list[1] = 12
list[2] = 2

opcodes = list[0::4]
# print(opcodes)

def adding(i):
    x = (list[list[i + 1]] + list[list[i + 2]])
    list[list[i + 3]] = x
    # print(x)

def multiplying(i):
    x = (list[list[i + 1]] * list[list[i + 2]])
    list[list[i + 3]] = x
    # print(x)


for i, v in enumerate(opcodes):
    if v == 1:
        adding(i * 4)
    if v == 2:
        multiplying(i * 4)
    if v == 99:
        print(list[0])
        break
