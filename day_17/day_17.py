


current_pos = 1
step_size = 303
buff = [0]

for i in range(1,2018):
    length = len(buff)
#print(buff)
#print("length: " + str(length))
    current_pos = ((current_pos + step_size) % length) + 1
#print("current_pos: " + str(current_pos))
    buff.insert(current_pos, i)
#print(buff)
#print()

print(buff[current_pos:])
print("Solution part1: " + str(buff[current_pos + 1]))


