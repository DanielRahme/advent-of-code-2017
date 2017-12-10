import itertools

case_1 = [0, 3, 0, 1, -3]


# Read the input file
matrix = []
with open("input.txt", "r") as f:
    for line in f:
#print(line)
        tmp = int(line)
        matrix.append(tmp)
#tmp = list(line)
#tmp[-1] = tmp[-1].strip()
#tmp = map(int, tmp)
#matrix.append(tmp)
#
print(matrix)

def maze_jumps(list_of_jumps):
    jumps = 0
    len_list = len(list_of_jumps)
    idx = 0
    while (idx < len_list):
        tmp = list_of_jumps[idx]
        list_of_jumps[idx] += 1
        idx += tmp
        jumps += 1
    return jumps


def maze_jumps_2(list_of_jumps):
    jumps = 0
    len_list = len(list_of_jumps)
    idx = 0
    while (idx < len_list):
        tmp = list_of_jumps[idx]
        if tmp >= 3:
            list_of_jumps[idx] += -1
        else:
            list_of_jumps[idx] += 1
        idx += tmp
        jumps += 1
    return jumps

# main #####################

#print(maze_jumps(case_1))
matrix_2 = matrix
#print(maze_jumps(matrix))
print(maze_jumps_2(matrix_2))
