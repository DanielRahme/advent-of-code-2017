import itertools

case_1 = ["aa", "bb", "cc", "dd", "ee"]
case_2 = ["aa", "bb", "cc", "dd", "aa"]
case_3 = ["aa", "bb", "cc", "dd", "aaa"]

case_matrix = []
case_matrix.append(case_1)
case_matrix.append(case_2)
case_matrix.append(case_3)


# Read the input file
matrix = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = line.split(' ')
        tmp[-1] = tmp[-1].strip()
#tmp = map(int, tmp)
        matrix.append(tmp)
#
print(matrix)


def passphrase_check(matrix_input):
    dupes_found = 0
    valids = 0
    for line in matrix_input:
        for a, b in itertools.combinations(line, 2):
            if (a == b):
                dupes_found += 1
        if (dupes_found == 0):
            valids += 1
        dupes_found = 0

    return valids

def passphrase_check_2(matrix_input):
    dupes_found = 0
    valids = 0
    for line in matrix_input:
        for a, b in itertools.combinations(line, 2):
            if (sorted(a) == sorted(b)):
                dupes_found += 1
        if (dupes_found == 0):
            valids += 1
        dupes_found = 0

    return valids

# main #####################

print(passphrase_check(matrix))
print(passphrase_check_2(matrix))
