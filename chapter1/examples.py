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

# Adding complex numbers
plot({1+2j+z for z in S}, 4)

input('Press a key to exit and delete the plotted html files...')