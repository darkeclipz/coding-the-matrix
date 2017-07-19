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
print( (1, 1+1, 3) )
