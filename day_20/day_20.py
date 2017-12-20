import pprint
import itertools
import time
start_time = time.time()

# Read the input file
input_lines = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = list(line)
        tmp[-1] = tmp[-1].strip()
        input_lines.append(line.rstrip())
    

#print(input_lines)
#pprint.pprint(input_lines)

def strip_vector(particle):
    particle = "".join([x.replace(' ','') for x in particle])
    tmp = particle.split(',')

    vector = []
    for i in range(0, 8, 3):
        vector.append(int(tmp[i][3:]))
        vector.append(int(tmp[i+1]))
        vector.append(int(tmp[i+2][0:-1]))

    return vector


# Update the velocity and position of particle
def update_vector(vec):
    order = [3,4,5,0,1,2]
    for i in order:
        vec[i] += vec[i+3]

    return vec


# Calculate distance of particle
def calculate_dist(vec):
    s = sum([abs(vec[i]) for i in range(0, 3)])
    return s


def closest(input_vector):
    minimum = 50000000 # Just a random big number
    closest_particle = 0
    for idx, v in enumerate(input_vector):
        v = strip_vector(v)
        for i in range(1000):
            v = update_vector(v)

        dist = calculate_dist(v)

        if dist < minimum:
            minimum = dist
            closest_particle = idx

    print("Solution part 1: "),
    print(closest_particle)
    return closest_particle
        


def collision(input_vector):
    particles = [strip_vector(x) for x in input_vector]

    for abc in range(1000):
#       Update the particles
        for i, v in enumerate(particles):
            particles[i] = update_vector(v)

#       Check for collision and remove
        for a, b in itertools.combinations(particles, 2):
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
                particles[:] = [x for x in particles if x != b]
                particles[:] = [x for x in particles if x != a]
                continue
            

    print("Solution part 2: "),
    print(len(particles))

# main #####################


test_1 = 'p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>' 
test_2 = 'p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>' 
test_3 = 'p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>' 
test_4 = 'p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>' 
tmp = []
tmp.append(test_1)
tmp.append(test_2)
tmp.append(test_3)
tmp.append(test_4)

closest(input_lines)

collision(input_lines)
print("--- %s seconds ---" % (time.time() - start_time))
