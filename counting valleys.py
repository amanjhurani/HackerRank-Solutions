n = int(input())
path = input()
path  = path.split()
climbed_up = 'U'
climbed_down = 'D'
valleys = 0
depth = 0
height = 0
for i in range(len(path)):
    if path[i] == climbed_up and height  0:
        height += 1
    else:
        depth -= 1
        height -= 1
    if heigt == 0:
        if depth < 0:
            valleys += 1
