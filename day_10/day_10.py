import itertools
import collections

input_test = [3, 4, 1, 5]

puzzle_input = [18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188]
puzzle_input_str = "18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"
#puzzle_input_str = ""

puzzle_end = [17, 31, 73, 47, 23]

puzzle_input_ascii = map(ord, puzzle_input_str)
puzzle_input_ascii.extend(puzzle_end)

print(puzzle_input_ascii)


# Read the input file
#matrix = []
#with open("input.txt", "r") as f:
#for line in f:
#print(line)
#tmp = int(line)
#matrix.append(tmp)
#tmp = list(line)
#tmp[-1] = tmp[-1].strip()
#tmp = map(int, tmp)
#matrix.append(tmp)
#
#print(matrix)


#def reverse_sublist(input_list, idx, sub_len):
#length = len(input_list)
#input_list[idx : (idx+sub_len)%length] = input_list[idx : (idx+sub_len)%length][::-1] 
#return input_list


#def reverse_sublist(input_list, idx, sub_len):
#length = len(input_list)
#
#sub_list = input_list[idx : ((idx + sub_len) % length)]
#sub_list.reverse()
#del input_list[idx : ((idx + sub_len) % length)]
#print(sub_list)
#input_list.insert(idx, sub_list)
#print(input_list)
#
#return input_list

def reverse_sublist(input_list, idx, sub_len):
    length = len(input_list)
    start = idx
    end = idx + sub_len 
    
    sub_list = []

    for x in range(start, end):
        sub_list.append(input_list[x % length])
    sub_list.reverse()

    for x in range(start, end):
        input_list[x%length] = sub_list.pop(0)

    return input_list


def single_round(sub_len_list):
    idx = 0
    offset = 0
    elements = range(256)

    for group_len in sub_len_list:
        elements = reverse_sublist(elements, idx, group_len)
        idx += group_len + offset
        offset += 1
    return elements[0] * elements[1]

def sparse_hash(sub_len_list):
    idx = 0
    offset = 0
    elements = range(256)

    for i in range(64):
        for group_len in sub_len_list:
            elements = reverse_sublist(elements, idx, group_len)
            idx += group_len + offset
            offset += 1
    return elements


# Fix: Two digits 0x00 - 0xFF
def dense_hash(sparse_hash):
    n = 16
    dense = []

    chunks = [sparse_hash[i:i+n] for i in range(0, len(sparse_hash), n)]

    for chunk in chunks:
        xored = reduce(lambda x, y: x ^ y, chunk)
        dense.append(xored)
    print(dense)
    hash_string = map(hex, dense)
    print(hash_string)
    hash_string = [element[2:] for element in hash_string]
    hash_string = "".join(hash_string)
    print(hash_string)
    return hash_string
    
    
# main #####################

    

print(single_round(puzzle_input))
#print(single_round(input_test))
tmp = sparse_hash(puzzle_input_ascii)
print(dense_hash(tmp))
