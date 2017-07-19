# Select the elements from the dictionary such that the elements are a member of the set 'keylist'.
def dict2list(dct, keylist): return [dct[k] for k in keylist]

# Cartesian product from two sets returned as a dictionary.
def list2dict(L, keylist): return { k:v for (k,v) in zip(keylist, L) }

# Select the elements from the set and return this as a dictionary with incremented index.
def listrange2dict(L): return {k:L[k] for k in range(len(L))}