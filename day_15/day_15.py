
gen_a_factor = 16807
gen_b_factor = 48271

gen_a_start_value = 883
gen_b_start_value = 879

divisor = 2147483647

# Generate a pair, gen A and B
def generate_pair(prev_gen_pair):
    gen_pair = [0, 0]

    gen_pair[0] = (gen_a_factor * prev_gen_pair[0]) % divisor
    gen_pair[1] = (gen_b_factor * prev_gen_pair[1]) % divisor

    return list(gen_pair)


# Compares a pair  
def check_match(pair):
    return (pair[0] & 65535) == (pair[1] & 65535)


def check_multiple(gen, multi):
    return gen % multi == 0


# Calculate matching pairs. A match is same 16 LSB
def calc_matches(n):
    current_pair = [gen_a_start_value, gen_b_start_value]
    count = 0

    for i in range(n):
        current_pair = list(generate_pair(current_pair))
        if check_match(current_pair):
            count += 1

    print count


        
# main #####################

calc_matches(40000000) # Answer = 609
