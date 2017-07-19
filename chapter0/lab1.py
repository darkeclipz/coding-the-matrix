# Using existing modules
import math

# print(help(math))

print( math.sqrt(3) ** 2 )

from random import randint
print( {randint(0,10) for _ in range(10)} )

# Creating your own modules
import dictutil
print( dictutil.dict2list({'a':'A', 'b':'B', 'c':'C'}, ['b', 'c', 'a']) )
print( dictutil.list2dict(['A', 'B', 'C'], ['a', 'b', 'c']) )
print( dictutil.listrange2dict(['A', 'B', 'C']) )

# Loops and Conditional statements
for x in {1,2,3}: print(x)
#while v[i] == 0: i = i+1
x = 2
if x > 0: print('positive')

# Grouping in Python using Indentation
for x in [1,2,3]:
    y = x*x
    print(y)

def quadratic(a,b,c):
    discriminant = math.sqrt(b*b - 4*a*c)
    return ((-b + discriminant)/(2*a), (-b - discriminant)/(2*a))

def print_greater_quadratic(L):
    for a, b, c in L:
        plus, minus = quadratic(a, b, c)
        if plus > minus:
            print(plus)
        else:
            print(minus)

# Breaking out of a Loops
s = "There is no spoon."
for i in range(len(s)):
    if s[i] == 'n':
        break

print(i)

# Reading from a file
f = open('stories_big.txt')
for line in f:
    print(line)

f = open('stories_small.txt')
stories = list(f)
print(len(stories))

# Mini search engine
mystr = 'Ask not what you can do for your country.'
print(mystr.split())

print(list(enumerate(['A', 'B', 'C'])))

print( [i*x for (i,x) in enumerate([10,20,30,40,50])] )
print( [i*s for (i,s) in enumerate(['A', 'B', 'C', 'D', 'E'])] )

def makeInverseIndex(strlist): return { k:v for (k,v) in list(enumerate(strlist.split())) }
def orSearch(inverseIndex, query): return { k:v for (k,v) in inverseIndex.items() if v in query.split() }

def andSearch(inverseIndex, query): 
    result = orSearch(makeInverseIndex(mystr), query)
    return result if len({x for x in query.split()} & {x for x in result.values()}) == len(query.split()) else []

print( makeInverseIndex(mystr) )
print( orSearch(makeInverseIndex(mystr), 'not for') )
print( andSearch(makeInverseIndex(mystr), 'what country.'))

