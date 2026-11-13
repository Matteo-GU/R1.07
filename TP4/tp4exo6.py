lst = [5, 2, 4, 8, 1, 3]
for i in range(0,len(lst)):
    m=lst[i]
    _id=i
    print(lst)
    for j in range(i+1,len(lst)):
        if lst[j] < m:
            m = lst[j]
            _id = j
    lst[i], lst[_id] = lst[_id], lst[i]