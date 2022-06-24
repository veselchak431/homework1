import re
import math
import itertools


def domain_name(url):
    for name in re.split(r'http://|https://|www.|[.]+', url):
        if name != '':
            return name


def int32_to_ip(int32):
    full_32_bit_number = bin(int32 + 2 ** 32)
    return '{}.{}.{}.{}'.format(int(full_32_bit_number[3:11], 2),
                                int(full_32_bit_number[11:19], 2),
                                int(full_32_bit_number[19:27], 2),
                                int(full_32_bit_number[27:36], 2))


def zeros(n):
    if n == 0:
        return 0
    k_max = math.floor(math.log(n, 5))
    count_of_zeros = 0
    for k in range(1, k_max + 1):
        count_of_zeros = count_of_zeros + math.floor(n / (5 ** k))
    return count_of_zeros


def bananas(s) -> set:
    result = set()
    for comb in itertools.combinations(range(len(s)), len(s) - len('banana')):
        arr = list(s)
        for i in comb:
            arr[i] = '-'
        intermediate_result = ''.join(arr)
        if intermediate_result.replace('-', '') == 'banana':
            result.add(intermediate_result)
    return result


def count_find_num(primesL, limit):
    minimum_multiply = 1
    for number in primesL:
        minimum_multiply = minimum_multiply * number
    degree_list = []
    for number in primesL:
        degree_list.append(
            [number ** x for x in range(1, math.floor(
                math.log(limit / (minimum_multiply / number), number)) + 1)])
    degree_tuples = list(itertools.product(*degree_list))
    result = []
    for tup in degree_tuples:
        multiply = 1
        for number in tup:
            multiply = multiply * number
        if multiply <= limit:
            result.append(multiply)
    if len(result):
        return [len(result), max(result)]
    return []
