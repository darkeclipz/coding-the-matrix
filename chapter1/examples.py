# Complex numbers in python
print(3j)
print(1+3j)
print((1+3j) + (10+20j))

x=1+3j
print((x-1)**2)

print(x)
print(x.real)
print(x.imag)

# Abstracting over fields
def solve1(a,b,c): return (c-b)/a
print(solve1(10, 5, 30))
print(solve1(10+5j, 5, 20))

# Playing with Complex numbers
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}
from plotting import plot
#plot(S, 4)

# The absolute value of a complex number
print( abs(3+4j) )
print( abs(1+1j) )

print( (3+4j).conjugate() )

# Adding complex numbers (Translating)
plot({1+2j+z for z in S}, 4)

# Multiplying complex numbers by a positive real number (Scaling)
plot({1/2*z for z in S}, 4)

# Multiplying complex numbers by a negative number: rotation of 180 degrees
plot({-1*z for z in S}, 4)

# Multiplying by i: rotation of 90 degrees
plot({1j+z for z in S}, 4)

# Rotate 90 degrees, scale 1/2, and shift down by 1 unit and right 2 units.
plot({1/2*1j*z+2-1j for z in S}, 4)

import image
data = image.file2image('img01.png')
w = len(data[0])
h = len(data)
pts = {complex(x,y) for x in range(w) for y in range(h) if data[y][x][0] < 120}
def f(z): return complex(w,h)-z
plot({f(x) for x in pts}, h)

import math
n=20
pts = {(math.e**(complex(2, math.pi)/n))**i
-1 for i in range(20)}
plot(pts, 8)

input('Press a key to exit and delete the plotted html files...')