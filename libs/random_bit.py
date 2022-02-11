from random import randrange, choice, randint, uniform
import math

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1


def bit_flip(bit):
    bit_new = []
    for bit_ele in bit:
        if bit_ele == '1':
            bit_ele = '0'
        else:
            bit_ele = '1'
        bit_new.append(bit_ele)
    
    bit_new_string = listToString(bit_new)
    return bit_new_string


def random_bit(size):
    bit_25 = []
    bit_25_string = []
    for binary in range(size):
        bit_25.append(randrange(2))
    
    bit_25_string.append(listToString(bit_25))
    return bit_25_string[0]


def random_position(bit):
    position = []
    max_bit = len(bit)
    for round in range(2):
        position.append(randrange(max_bit))

    return position


def Exchange_position(bit, i, j):
    lst = list(bit)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def insert_shift(bit, i , j):
    lst = list(bit)
    lst.insert(j, lst[i])
    lst.remove(lst[i])
    return ''.join(lst)



def random_insert_space(option):
    result_pack = []
    round_impro = 0
    best_impro = None
    worst_impro = 0

    for round in range(50):
        space_size = []
        for round_in in range(50):
            bit_item = random_bit(25)
            position = random_position(bit_item)
            item_new = insert_shift(bit_item, position[0], position[1])
            # item_new = Exchange_position(bit_item, position[0], position[1])
            # item_new = bit_flip(bit_item)
            space_size.append(item_new)

        if option == "hill_climbing":
            bit_init = space_size[0]
            bit_init_int = int(space_size[0], 2)
            first_impro = bit_init
            first_impro_int = bit_init_int

            for item in space_size:
                item_int = int(item, 2)
                if item_int > bit_init_int:
                    if item_int > first_impro_int:
                        first_impro = item
                        first_impro_int = item_int
                        round_impro = space_size.index(item)
            
            if best_impro == None:
                best_impro = round_impro
            if round_impro < best_impro:
                best_impro = round_impro
            if round_impro > worst_impro:
                worst_impro = round_impro
        
    if option == "simulated_annealing":
        bit_init = space_size[0]
        bit_init_int = int(space_size[0], 2)
        first_impro = bit_init
        first_impro_int = bit_init_int
        best_impro = None
        worst_impro = None

        initial_temp = 1000
        final_temp = .1
        alpha = 0.01
        solution_int = 0
        current_temp = initial_temp
        current_state = bit_init_int
        solution = current_state

        while current_temp > final_temp:
            neighbor  = choice(space_size)
            neighbor_int = int(neighbor , 2)
            if current_temp == initial_temp:
                if neighbor_int > current_state:
                    solution = neighbor
                    solution_int = int(solution, 2)
            else:
                if neighbor_int > solution_int:
                    solution = neighbor
                    solution_int = int(solution, 2)

            current_temp -= alpha
        
        first_impro = solution
        first_impro_int = solution_int
    
    result_pack.append(bit_init)
    result_pack.append(bit_init_int)
    result_pack.append(first_impro)
    result_pack.append(first_impro_int)
    result_pack.append(best_impro)
    result_pack.append(worst_impro)

    return result_pack
