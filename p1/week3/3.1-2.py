def modify_list(l):
    lst = l.copy()
    lst = list(filter(lambda x: x % 2 == 0, lst))
    lst = list(map(lambda x: x // 2, lst))
    l.clear()
    l += lst
    return
    #print(lst)

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]