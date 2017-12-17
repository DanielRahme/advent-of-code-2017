#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>


typedef unsigned long long generator_t;

typedef struct pair_s {
    generator_t a;
    generator_t b;
} pair_t;

typedef struct node_s {
    generator_t     value;
    struct node_s   *next;
} node_t;

const generator_t GEN_A_FACTOR = 16807;
const generator_t GEN_B_FACTOR = 48271;

const generator_t gen_a_start_example = 883;
const generator_t gen_b_start_example = 879;

const generator_t DIVISOR = 2147483647;



node_t *insert_node_last(node_t *list, generator_t insert_value)
{
    node_t *new_entry   = malloc(sizeof(*new_entry));
    new_entry->value    = insert_value;
    new_entry->next     = NULL;

    node_t *node = list;
    node_t *prev = NULL;

    if (node == NULL) {     // First entry into the list
        new_entry->next = node;
        return new_entry;
    }

    while (node) {
        prev = node;
        node = node->next;
    }
    prev->next = new_entry;
    return list;
}

generator_t pop(node_t *list)
{
    if (list == NULL)
        return 0;

    return list->value;
}

node_t *remove_first_entry(node_t *list)
{
    node_t *n = list;

    if (n == NULL)
        return NULL;

    list = list->next;
    free(n);
    return list;
}

pair_t generate_pair(pair_t previous_pair)
{
    return (pair_t) {
        .a = (GEN_A_FACTOR * previous_pair.a) % DIVISOR,
        .b = (GEN_B_FACTOR * previous_pair.b) % DIVISOR
    };
}


// Check matching 16 bit LSB
bool check_match(pair_t pair)
{
    return (pair.a & 0xFFFF) == (pair.b & 0xFFFF);
}


// See if number <gen> is a multiple of <multiple>
bool check_multiple(generator_t gen, int multiple)
{
    return gen % multiple == 0;
}


int calc_matches_2(generator_t number_of_pairs_to_check)
{
    generator_t matches_found   = 0;
    generator_t pairs_found     = 0;

    pair_t current_pair     = {gen_a_start_example, gen_b_start_example};
    node_t *a_list          = NULL;
    node_t *b_list          = NULL;

    while (pairs_found < number_of_pairs_to_check) {
        current_pair = generate_pair(current_pair);

        if (check_multiple(current_pair.a, 4)) 
            a_list = insert_node_last(a_list, current_pair.a);
        
        if (check_multiple(current_pair.b, 8)) 
            b_list = insert_node_last(b_list, current_pair.b);
        

        if (a_list != NULL && b_list != NULL) {         // Check when pairs found
            pairs_found++;

            pair_t tmp_pair     = {pop(a_list), pop(b_list)};
            a_list              = remove_first_entry(a_list);
            b_list              = remove_first_entry(b_list);

            if (check_match(tmp_pair)) {
                    printf("A: %d %\t %--- %\t %B: %%d\n", %tmp_pair.a, %tmp_pair.b);
                    matches_found++;
            }
        }
    }
    return matches_found;
}

int main()
{
    printf("Start looking for matches...\n");
    int result = calc_matches_2(5000000);
    printf("found: %d\n", result);

}

