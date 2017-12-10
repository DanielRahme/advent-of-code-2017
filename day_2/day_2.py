import itertools

matrix_a = [ (5, 1, 9, 5),
                (7, 5, 3),
                (2, 4, 6, 8)]

# Read the input file
matrix = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = line.split('\t')
        tmp[-1] = tmp[-1].strip()
        tmp = map(int, tmp)
        matrix.append(tmp)

print(matrix)

def sum_of_diffs(matrix_input):
    sum_diff = 0
    for group in matrix_input:
        sum_diff += max(group) - min(group)
    return sum_diff


def sum_of_divs(matrix_input):
    sum_div = 0
    for row in matrix_input:
        for a, b in itertools.combinations(row, 2):
            if (a%b == 0):
                sum_div += a/b
            elif (b%a == 0):
                sum_div += b/a
    return sum_div


# main #####################

print(sum_of_diffs(matrix))
print(sum_of_divs(matrix))
