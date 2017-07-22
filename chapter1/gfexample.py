from GF2 import one

# brute forcing the flawed one-time pad encryption with a 5 bit pad.
secret_message = [[1,0,1,0,1], [0,0,1,0,0], [1,0,1,0,1], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,1,1], [0,1,0,1,1], [1,0,1,0,1], [1,0,1,0,1], [0,0,1,0,0], [1,1,0,0,1], [1,1,0,1,0]]
base=2
digits=set(range(base))
pads = { a*(base**4)+b*(base**3)+x*(base**2)+y*base+z:[a,b,x,y,z] for a in digits for b in digits for x in digits for y in digits for z in digits }

def bin2dec(z): 
    return z[0]*16+z[1]*8+z[2]*4+z[3]*2+z[4]*1

def dec2chr(z): 
    return " " if z == 26 else chr(z+65)

for pad in pads.values():
    msg = ""
    for s in secret_message:
        r = [pad[x] ^ s[x] for x in range(5)]
        msg=msg+dec2chr(bin2dec(r))
    print(msg)

# finding the pad by assuming the most used bit sequence is the letter e.
print('Finding path by assuming most used combo is e:')
most_used = [1,0,1,0,1]
letter_e = [0,0,1,0,0]
xor = [most_used[x] ^ letter_e[x] for x in range(5)]
print('Found pad:')
print(xor)

# network encoding with GF(2)
b1 = 0
b2 = 1
print('transmit:')
print(b1)
print(b2)

# calc GF(2) for bit1 and bit2 and send the each of the customers 1 bit + the GF(2).
gfb1 = one if b1 == 1 else 0
gfb2 = one if b2 == 1 else 0
gf = gfb1 + gfb2
print('GF(2):')
print(gf)

# c1 calculates b2 with b1 and GF(2)
print('customer 1:')
print(b1)
print(b1 + gf)

# c2 calculates b1 with b2 and GF(2)
print('customer 2:')
print(b2 + gf)
print(b2)
