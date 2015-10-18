# https://www.hackerrank.com/challenges/itertools-product

from itertools import product

list_a = list(map(int, raw_input().split(" ")))

list_b = list(map(int, raw_input().split(" ")))

product_list = list(product(list_a, list_b))

print " ".join(str(x) for x in product_list)
