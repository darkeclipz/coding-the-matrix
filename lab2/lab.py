f = open('voting_record_dump109.txt')
raw = list(f)

def create_voting_dict(strlist):
    """
    Returns a dictionary with the senators last name as key, and
    a list of integers which represent votes on bills (-1, 0, 1).
    """
    result = {}
    for line in strlist:
        data = line.split()
        bills = [int(b) for b in data[3:len(data)-1]]
        result[data[0]] = bills
    return result

def dot(v,u):
    """
    Returns the dot-product for two lists.
    """
    return sum([a*b for (a,b) in zip(v,u)])

def dot_product_list(needle, haystack):
    """
    Returns a dictionary with the senators last name as key, and
    the value is the dot-product against the needle.
    """
    return {k:dot(needle,haystack[k]) for k in haystack.keys()}

def dict_max(D):
    """
    Returns a tuple (key, value) for the item in the dictionary
    with the highest value. 
    """
    current = 0
    key = ''
    for k in D.keys():
        current = D[k]
        key = k
        break
    for k in D.keys():
        if D[k] > current:
            current = D[k]
            key = k
    return (key, current)

def dict_min(D):
    """
    Returns a tuple (key, value) for the item in the dictionary
    with the lowest value.
    """
    current = 0
    key = ''
    for k in D.keys():
        current = D[k]
        key = k
        break
    for k in D.keys():
        if D[k] < current:
            current = D[k]
            key = k
    return (key, current)

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Returns the dot-product between two senators.
    """
    return dot(voting_dict[sen_a], voting_dict[sen_b])

def most_similar(sen, voting_dict):
    """
    Returns the name of the senator which has the most similarity.
    """
    result = dot_product_list(sen, {k:voting_dict[k] for k in voting_dict.keys() if k != sen})
    return dict_max(result)[0]

def least_similar(sen, voting_dict):
    """
    Returns the name of the senator which has the least similarity.
    """
    result = dot_product_list(sen, {k:voting_dict[k] for k in voting_dict.keys() if k != sen})
    return dict_min(result)[0]

def average_similarity(sen, sen_set, voting_dict):
    """
    Returns the average similarity compared to a set of senators.
    """
    products = dot_product_list(voting_dict[sen], {k:voting_dict[k] for k in sen_set if k != sen})
    return sum([v for v in products.values()]) / len(products)

def set_of_democrats(strlist):
    """
    Returns a list with all the democrats.
    """
    S = [line.split() for line in strlist]
    return [z[0] for z in S if z[1] == 'D']

def greatest_average_similarity(sen_set, voting_dict):
    """
    Returns the name of the senator that has the greatest average
    similarity with the set.
    """
    result = {k:average_similarity(k, sen_set, voting_dict) for k in voting_dict.keys()}
    return dict_max(result)

def find_average_records(sen_set, voting_dict):
    """
    Returns the average for a set of senators as vector.
    """
    length = len(voting_dict[sen_set[0]])
    result = [0 for _ in range(length)]
    for s in sen_set:
        for i in range(length):
            result[i] += voting_dict[s][i]
    return [z / length for z in result]

def bitter_rivals(voting_dict):
    """
    Returns a tuple of senators who disagree the most.
    """
    current = 0
    sen_a = ''
    sen_b = ''
    for a in voting_dict.keys():
        for b in voting_dict.keys():
            compare = policy_compare(a,b, voting_dict)
            if compare < current:
                current = compare
                sen_a = a
                sen_b = b
    return (sen_a, sen_b)

voting_records = create_voting_dict(raw)
democrats = set_of_democrats(raw)

print( policy_compare('Obama', 'Craig', voting_records) )
print( most_similar(voting_records['Chafee'], voting_records) )
print( least_similar(voting_records['Santorum'], voting_records) )
print( average_similarity('Obama', ['Johnson', 'Durbin', 'Kennedy'], voting_records) )
print( greatest_average_similarity(democrats, voting_records) )
print( find_average_records(democrats, voting_records) )
print( most_similar(find_average_records(democrats, voting_records), voting_records) )
print( bitter_rivals(voting_records) )
