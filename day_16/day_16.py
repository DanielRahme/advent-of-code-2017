import itertools
from collections import deque


# Read the input file
matrix = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = line.split(',')
        matrix.append(tmp)
    
# Remove \n at the end
matrix[0][-1] = matrix[0][-1].strip()
# Flatten list
matrix = [x for sublist in matrix for x in sublist]
#print(matrix)

def spin(letters, rotations):       # Rotate test to right
    tmp = deque(letters)
    tmp.rotate(rotations)
    return "".join(tmp)

def swap_pos(letters, pos_a, pos_b):    # Swap by index
    letters_list = list(letters)
    tmp = letters_list[pos_a]
    letters_list[pos_a] = letters_list[pos_b]
    letters_list[pos_b] = tmp
    return "".join(letters_list)
    
def swap_letter(letters, a, b):         # Swap letters
    letters_list = list(letters)
    pos_a = letters_list.index(a)
    pos_b = letters_list.index(b)
    
    return swap_pos(letters, pos_a, pos_b)


def decode(inputs, line):       # Decode the input
    for cmd in inputs:
        cmd = list(cmd) 
        op = cmd.pop(0)
        
        if op == 's':               # Rotate
            cmd = int("".join(cmd))
            line = spin(line, cmd)

        elif op == 'x':             # Swap positions
            cmd = "".join(cmd)
            cmd = cmd.split('/')
            line = swap_pos(line, int(cmd[0]), int(cmd[1]))

        elif op == 'p':             # Swap letters
            cmd = "".join(cmd)
            cmd = cmd.split('/')
            line = swap_letter(line, cmd[0], cmd[1])
    
    return line
    

def check_occurrence(input_line):   # See if there are any periodic patterns
                                    # The line repeats itself every 42nd rev
    revs = []
    list_of_lines = []
    list_of_lines.append(input_line)
    for x in range(100):
        input_line = decode(matrix, input_line)
        list_of_lines.append(list(input_line))

    for i in range(0, len(list_of_lines)):
        tmp = list_of_lines[i]
        for j in range(i+1, len(list_of_lines)):
            if tmp == list_of_lines[j]:
                idx = [i, j]
                revs.append(idx)
                break
            
    diff = [idx[1] - idx[0] for idx in revs]
    print(diff)
    print(revs)

    return int(diff[0])


# main #####################

line = "abcdefghijklmnop"
periodic_occurance = check_occurrence(line)

decodes_needed = 1000000000 % periodic_occurance

for i in range(decodes_needed):
    line = decode(matrix, line)
print(line)

