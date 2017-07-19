# Simple expressions
44+11*4-6/11
1e16+1
"This is a string"
True and not (5==4)

# Assigment
mynum = 4+1
mynum = 'Brown'

x = 5 + 4
y = 2 * x
print(str(y))
x = 12
print(str(y))

# Conditional expressions (<expr> if <cond> else <expr>)
2**(y+1/2) if x+10<0 else 2**(y-1/2)

# Sets
len({1,2,3})
sum({1,2,3})
S={1,2,3}
2 in S
4 in S
4 not in S

{1,2,3} | {2,3,4}
{1,2,3} & {2,3,4}

S={1,2,3}
S.add(4)
S.remove(2)
print(S)

S.update({4,5,6})
print(S)

S.intersection_update({5,6,7,8,9})
print(S)
T=S
T.remove(5)
print(S)

U=S.copy()
U.add(5)
print(S)

print( {2*x for x in {1,2,3}} )
print( {x*x for x in S | {5,7}} )
print( {x*x for x in S | {5,7} if x > 2 } )
print( {x*y for x in {1,2,3} for y in {2,3,4}} )
print( {x*y for x in {1,2,30} for y in {2,3,4} if x != y} )

# Lists
print( [1,1+1,3,2,3] )
print( [[1,1+1,4-1], {2*2,5,6},"yo"] )
print( len( [1,2,2,3] ))
print( sum([1,2,3], -6) )
[1,2,3] + ["my", "word"]
mylist = [4,8,12]
mylist + ["my", "word"]
print(mylist)

print( sum( [[1,2,3], [4,5,6], [7,8,9]], [] ))

[2*x for x in {2,1,3,4,5}]
[2*x for x in [2,1,3,4,5]]
print( [x*y for x in [1,2,3] for y in [10,20,30]] )
print( [[x,y] for x in ['A', 'B', 'C'] for y in [1,2,3]] )

print( ["in", "the", "CIT"][1] )

L = [x*10 for x in range(10)]
print(L)
print(L[:5])
print(L[5:])
print(L[::2]) # even elements
print(L[1::2]) # odd elements

[x,y,z] = [4*1, 4*2, 4*3]
print(x)

listoflists = [[1,1],[2,4],[3,9]]
print([y for [x,y] in listoflists])

mylist = [30,20,10]
mylist[1] = 0
print(mylist)

# Tuples
(1,1+1,3)
mytuple = ("all", "my", "books")
print( mytuple[1] )
print( (1, {"A", "B"}, 3.14)[2] )

(a,b) = (1,5-3)
a,b = 1,5-3

print( [y for (x,y) in [(1,'A'),(2,'B'),(3,'C')]] )
S = {-4,-2,1,2,5,0}
triples = [(i,j,k) for i in S for j in S for k in S if (i+j+k) == 0 and (i,j,k) != (0,0,0) ]
print(triples)

# Other things to iterate over
(i for i in [1,2,3])

list(range(10))
print(list(zip([1,3,5],[2,4,6])))

L = ['A', 'B', 'C', 'D', 'E']
print(list(zip([0,1,2,3,5], L)))

[x*x for x in reversed([4,5,10])]

# Dictionaries
{4:"four", 3:"three"}[4]
mydict = {'Neo':'Keanu', 'Morpheus':'Laurence', 'Trinity':'Carrie-Anne'}
'Oracle' in mydict
mydict['Oracle'] if 'Oracle' in mydict else 'NOT PRESENT'

print( { k:v for (k,v) in [(3,2),(4,0),(100,1)] } )
print( { (x,y) : x*y for x in [1,2,3] for y in [1,2,3] } )

print( { x:x*x for x in range(100) })
S = {'red', 'white', 'blue'}
print( {s:s for s in S} )

base=5
digits=set(range(base))
print( { x*(base^2)+y*base+z:[x,y,z] for x in digits for y in digits for z in digits } )

[2*x for x in {4:'a',3:'b'}.keys()]
[2*x for x in {4:'a',3:'b'}.values()]

print( [k for k in {'a':1, 'b':2}.keys() |  {'b':3, 'c':4}.keys()] )
print( [k for k in {'a':1, 'b':2}.keys() &  {'b':3, 'c':4}.keys()] )

print( [myitem for myitem in mydict.items()] )
print( [k + " is played by " + v for (k,v) in mydict.items()] )

id2salary = {0:1000, 3:990, 1:1200.50}
names = ['Larry', 'Curly', '', 'Moe']
print( {  names[k]:v for (k,v) in id2salary.items() } )

# Defining one-line procedures
def twice(z): return 2*z
print(twice(2))

def nextInts(L): return [l+1 for l in L]
print(nextInts([1,2,3]))

def cubes(L): return [l*l*l for l in L]
print(cubes([1,2,3]))

def dict2list(dct,keylist): return [dct[k] for k in keylist]
print(dict2list({'a':'A', 'b':'B', 'c':'C'}, ['b', 'c', 'a']))

def list2dict(L, keylist): return { k:v for (k,v) in zip(keylist, L) }
print( list2dict(['A', 'B', 'C'], ['a', 'b', 'c']) )

def all_3_digit_numbers(base, digits): return { i*base*base+j*base+k for i in range(base) for j in range(base) for k in range(base) }
print( all_3_digit_numbers(2, {0,1}) )
print( all_3_digit_numbers(3, {0,1,2}) )
print( all_3_digit_numbers(10, range(10)) )