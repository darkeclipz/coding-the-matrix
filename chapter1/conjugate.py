""" complex number """
c = 3+4j

""" absolute value """
print( abs(c) )
# result: |3+4j| = 5

""" multiplied by conjugate """
print( ( c * c.conjugate() ) ** (1/2) )
# result: (3+4j) * (3-4j) = 25
# sqrt(25) = 5