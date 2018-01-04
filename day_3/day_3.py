

input_val = 361527
#input_val = 1024

# Find which square the input is in
for i in range(1000):
    side_length = i*2 + 1
    largest_corner = side_length ** 2
    print(largest_corner)
    
    if input_val <= largest_corner:
        break


print("input: " + str(input_val) 
        + " closest square: " + str(largest_corner)
        + " side length: " + str(side_length)
        + " shortest possible: " + str(i))

# Check for which side of the square the input is in
for y in range(4):
    tmp_corner = largest_corner - y*(side_length-1)
    if input_val < tmp_corner:
        corner = tmp_corner
        print("Corner: " + str(corner))

# Check midpoint of the side
midpoint = corner - (side_length // 2)
print("midpoint: " + str(midpoint))

for j in range(side_length):
    print("offset j: " + str(j))
    if input_val == (corner - j):
        break

    elif input_val == (corner - side_length + j):
        break

    elif input_val == (midpoint + j):
        break

    elif input_val == (midpoint - j):
        break

print("Shorestest: " + str(i + j))

