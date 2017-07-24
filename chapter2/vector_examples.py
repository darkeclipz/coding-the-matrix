from plotting import plot
L = [[2,2],[3,2],[1.75,1],[2,1],[2.25,1],[2.5,1],[2.75,1],[3,1],[3.25,1]]
plot(L, 4)

def add2(v,w):
    return [v[0]+w[0], v[1]+w[1]]

print( add2([4,4], [1,2]) )
print( add2([-4,-4], [1,2]) )

def addn(v,w):
    return [x+y for (x,y) in zip(v,w)]

V1 = [2,4]
V2 = [5,2]

print( addn(V1,V2) )

def scalar_vector_mult(alpha, v):
    return [alpha*v[i] for i in range(len(v))]

print( scalar_vector_mult(2, V1) )

plot( [scalar_vector_mult(0.5, z) for z in L] )
plot( [scalar_vector_mult(-0.5, z) for z in L] )

V3 = [1,2,3]
V4 = [10,20,30]

print( addn( scalar_vector_mult(2, V3), V4) )

alpha = 1
beta = 0.5
v = [5,2]

is_equal = scalar_vector_mult(alpha, scalar_vector_mult(beta, v)) == scalar_vector_mult(alpha * beta, v)
print(is_equal)

v = [3,2]
plot([scalar_vector_mult(i/10, v) for i in range(11)], 5)
plot([scalar_vector_mult(i/100, v) for i in range(101)], 5)

plot([add2(scalar_vector_mult(i/100., [3,2]), [0.5,1]) for i in range(101)])

u = [2,3]
v = [5,7]

def sub2(v,w):
    return [v[0]-w[0], v[1]-w[1]]

w = sub2(v,u)

plot( [add2(scalar_vector_mult(i/25., w), u) for i in range(26)], 7)

def segment(pt1, pt2):
    return [add2(scalar_vector_mult(z/100., pt2), scalar_vector_mult(1-z/100., pt1)) for z in range(101)]

plot( segment([3.5,3], [0.5,1]) )


