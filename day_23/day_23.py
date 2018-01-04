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


registers[find_reg('1')][1] = 1
registers[find_reg('a')][1] = 1         # Set reg 'a' to 1
print(registers)

def decode(instructions):       # Decode the instructions
    pc = 0                      # Program counter
    length = len(instructions)
    counter = 0 

    while pc < length:
#for i in range(30):
        instruct = instructions[pc]
        op = instruct[0]
        reg = instruct[1]
        value = instruct[2]

        if  value.isalpha():
            value = registers[find_reg(value)][1] 
        else:
            value = int(value)
        
        print(str(pc) + ": " + op + "\t" + reg + " " +
                str(registers[find_reg(reg)][1])
                + "\t" + instruct[2] + " " + str(value))

        if op == "set":               # Set register = value
            registers[find_reg(reg)][1] = value

        elif op == "sub":             # Subtract letters
            registers[find_reg(reg)][1] -= value

        elif op == "mul":             # Multiply letters
            registers[find_reg(reg)][1] *= value
            counter += 1

        elif op == "jnz":             # Swap letters
            if registers[find_reg(reg)][1] != 0:
                pc += value
            else:
                pc += 1

        if op != "jnz":
            pc += 1

        if reg == 'h':
            print("Value in reg 'h': " + str(registers[find_reg(reg)][1]))

    print("Multiply instruction invoked: " + str(counter))
    print(registers)
    print(length)
    
    return pc
    


# main #####################

decode(instructions)
