from vec import *

v = Vec({'A', 'B', 'C'}, {'A':1})
setitem(v, 'B', 1)
print_vec(v)
print( getitem(v, 'B') )
print( zero_vec(v) )

v = Vec({'A'}, {'A':10})
u = Vec({'A'}, {'A':5})
u = scalar_mul(u, 2)
w = add(u, v)
print_vec(w)

v = neg(v)
print_vec(v)

from GF2 import one
d = {(x,y) for x in range(4) for y in range(4)}
S = Vec(d, {(x,y): one*0 for x in range(4) for y in range(4)})

print('S:')        
print_vec(S)

s0 = Vec(d, {(0,0):one,(3,1):one,(0,2):one})
print('s0:')
print_vec(s0)

print('adding vectors:')
S = add(S, s0)

print_vec(S)

print('adding another vector:')
s1 = Vec(d, {(1,1):one})
S = add(S, s1)
print_vec(S)

d = range(10)
p = Vec(d, {x:one*0 for x in d})
k = copy(p)

print('--crypto--')
#msg
setitem(p,0,one)
setitem(p,3,one)
setitem(p,4,one)
setitem(p,6,one)
print('--msg')
print_vec(p)

#key
setitem(k,0,one)
setitem(k,7,one)
print('--key')
print_vec(k)

#cypher
print('--cypher')
c = add(p,k)

print_vec(c)

#decrypt
print('--decrypt')
p = add(c,k)
print_vec(p)

