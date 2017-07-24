class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

def zero_vec(D):
    return Vec(D, {})

def setitem(v, d, val):
    v.f[d] = val
    
def getitem(v, d):
    return v.f[d] if d in v.f else 0

def print_vec(v):
    [print(str(d) + ":" + str(v.f[d])) for d in v.D if d in v.f]
    
def scalar_mul(v, alpha):
    return Vec(v.D, {d:alpha*getitem(v,d) for d in v.D})

def add(u, v):
    return Vec(v.D,{d:getitem(u,d)+getitem(v,d) for d in u.D})

def neg(v):
    return Vec(v.D, {d:-getitem(v,d) for d in v.D})

def copy(v):
    return Vec(v.D, {d:getitem(v,d) for d in v.D})
