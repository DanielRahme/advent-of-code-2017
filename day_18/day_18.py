import pprint

# Read the input file
instructions = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = line.split(' ')
        tmp[-1] = tmp[-1].strip()
        instructions.append(tmp)
    
# Remove \n at the end
#instructions[0][-1] = instructions[0][-1].strip()
# Flatten list
#instructions = [x for sublist in instructions for x in sublist]

pprint.pprint(instructions)

registers = [reg[1] for reg in instructions]
registers = set(registers)
registers = [[reg, 0] for reg in registers]
print(registers)

def find_reg(reg):
    idx = [idx for idx in registers if reg in idx][0]
    return registers.index(idx)


#registers[find_reg('1')][1] = 1
#print(registers)

def decode(instructions):       # Decode the instructions
    pc = 0                      # Program counter
    length = len(instructions)
    recently_played = 0

    while pc < length:
        instruct = instructions[pc]
        op = instruct[0]
        reg = instruct[1]
        print("op: " + instruct[0] + "--- reg: " + instruct[1])
        if len(instruct) > 2:
            if not instruct[2].isalpha():
                value = int(instruct[2])
                print("value: " + str(value))
            else:
                value = registers[find_reg(instruct[2])][1] 
                print("value: " + str(value))
        
        if op == "set":               # Set register = value
            registers[find_reg(reg)][1] = value

        elif op == "add":             # Add reg += value
            registers[find_reg(reg)][1] += value

        elif op == "mul":             # Multiply letters
            registers[find_reg(reg)][1] *= value

        elif op == "snd":             # Swap letters
            recently_played = registers[find_reg(reg)][1] 
            print("played sound: " + str(recently_played))

        elif op == "rcv":             # Swap letters
            if registers[find_reg(reg)][1] != 0:
                if recently_played != 0:
                    print(recently_played)
                    break

        elif op == "jgz":             # Swap letters
            if registers[find_reg(reg)][1] > 0:
                pc += value
            else:
                pc += 1

        elif op == "mod":             # Swap letters
            if registers[find_reg(reg)][1] != 0:
                registers[find_reg(reg)][1] %= value

        if op != "jgz":
            pc += 1

    print("Recently played: " + str(recently_played))
    
    return pc
    


# main #####################

decode(instructions)
