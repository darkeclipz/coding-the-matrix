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
