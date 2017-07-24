from vec import *

def list_dot(u, v): return sum([a*b for (a,b) in zip(u,v)])

D = {'hops', 'malt', 'water', 'yeast'}

cost = Vec(D, {'hops': 2.50, 'malt': 1.50, 'water': 0.006, 'yeast': 0.45})
quantity = Vec(D, {'hops': 6, 'malt': 14, 'water': 7, 'yeast': 11})
value = Vec(D, {'hops': 0, 'malt': 0, 'water': 0, 'yeast': 3.25})

total_cost = list_dot([cost.f[d] for d in cost.D], [quantity.f[d] for d in quantity.D])
print('total cost: ' + str(total_cost) + 'W')

total_calories = list_dot([value.f[d] for d in value.D], [quantity.f[d] for d in quantity.D])
print('total calories: ' + str(total_calories) + 'Cal')

def dot_product_list(needle, haystack):
    s = len(needle)
    return [list_dot(needle, haystack[i:i+s]) for i in range(len(haystack)-s)]

h = [2, -1, 5, -4, 7, -3, -5, 3, 7, -5, -2, -5, 2, 2, 2, -6, 4, -2, -9, -2, 5, 2]
n = [3, 7, -5]
result = dot_product_list(n,h)
print('dot-product-list:')
print(result)

def dpl_max(dpl):
    current = 0
    index = 0
    for x in dpl:
        current = x
        break
    for (x,y) in list(enumerate(dpl)):
        if y > current:
            current = y
            index = x
    return (index, current)

print('best result at (index, value):')
print( dpl_max(result) )
