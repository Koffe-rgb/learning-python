def update_dictionary(d, k, v):
    if k in d:
        d[k].append(v)
    else:
        if k * 2 in d:
            d[k*2].append(v)
        else:
            d[k*2] = [v]

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}