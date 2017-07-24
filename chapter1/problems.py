def my_filter(L, num):
    return [l for l in L if l % num != 0]

print( my_filter([1,2,3,4,5,6,7],2) )

def my_lists(L):
    return [[x+1 for x in range(l)] for l in L]

print( my_lists([0]) )
print( my_lists([1,2,4]) )

def my_function_composition(f,g):
    return {k:g[f[k]] for k in f.keys()}

f = {0:'a',1:'b'}
g = {'a':'Hey','b':'Yo'}
print( my_function_composition(f,g) )

def my_sum(L):
    current = 0
    for x in L:
        current += x
    return current

print( my_sum({1,2,3,4,5}) )

def my_product(L):
    current = 1
    for x in L:
        current *= x
    return current

print( my_product({1,2,3,4,5}) )

def my_min(L):
    current = 0
    for x in L:
        current = x
        break
    for x in L:
        if x < current:
            current = x
    return current

print( my_min({1,2,3,4}) )

def my_concat(L):
    current = ""
    for x in L:
        current += x
    return current

print( my_concat(['h', 'i', '!']) )

def my_union(L):
    current = set()
    for x in L:
        for y in x:
            current.add(y)
    return current

print( my_union([{1,2,3},{4,5,6},{5,6,7}]) )

def transform(a,b,L):
    return [a*z+b for z in L]

print( transform(1, 1 + 1j, [(5 + 3j)]) )
print( transform(0, 1 + 1j, [(5 + 3j)]) )
print( transform(1 + 1j, 1 + 1j, [(5 + 3j)]) )
print( transform(2 + 2j, 5 + 5j, [(5 + 3j)]) )
