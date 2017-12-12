import pprint
import itertools

case_1 = [0, 2, 7, 0]
input_case = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]


def redist(bank):
    idx = bank.index(max(bank))
    max_val = bank[idx] 
    bank[idx] = 0
    length = len(bank)

    while (max_val > 0):
        idx = (idx + 1) % length
        bank[idx] += 1
        max_val -= 1

    return list(bank)



def check_occurrence(bank_input):
    revs = []
    banks = []
    banks.append(list(bank_input))
    for x in range(4100):
        bank_input = list(redist(bank_input))
        banks.append(list(bank_input))

    for i in range(0, len(banks)):
        tmp = banks[i]
        for j in range(i+1, len(banks)):
            if tmp == banks[j]:
                idx = [i, j]
                revs.append(idx)
                break
            
    diff = [idx[1] - idx[0] for idx in revs]
    print(diff)

    print("Part 1 answer:" + str(revs[0][1]))
    print("Part 2 answer:" + str(diff[0]))




# main #####################

check_occurrence(input_case)
