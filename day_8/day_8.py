import pprint
import operator

# Read the input file
instructions = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = line.split(' ')
        tmp[-1] = tmp[-1].strip()
        instructions.append(tmp)
    
pprint.pprint(instructions)

registers = {ins[0]: 0 for ins in instructions}

pprint.pprint(registers)

def check_condition(reg, sign, val):
    if sign == '>':
        return registers[reg] > int(val)
    elif sign == '<':
        return registers[reg] < int(val)
    elif sign == '>=':
        return registers[reg] >= int(val)
    elif sign == '<=':
        return registers[reg] <= int(val)
    elif sign == '==':
        return registers[reg] == int(val)
    elif sign == '!=':
        return registers[reg] != int(val)


def decode(instructions):       # Decode the instructions
    highest_value = 0

    for instruct in instructions:

        reg     = instruct[0]
        op      = instruct[1]
        value   = instruct[2]

        comp_reg    = instruct[4]
        comp_sign   = instruct[5]
        comp_value  = instruct[6]

        if check_condition(comp_reg, comp_sign, comp_value):
            if op == "inc":
                registers[reg] += int(value)
            else:
                registers[reg] -= int(value)

        curr_high = max(registers.iteritems(), key=operator.itemgetter(1))[0]
        if registers[curr_high] > highest_value:
            highest_value = registers[curr_high]
        

    maximum = max(registers.iteritems(), key=operator.itemgetter(1))[0]
    print("part 1 - max value: " + str(registers[maximum]))
    print("part 2 - max value: " + str(highest_value))

# main #####################

decode(instructions)
