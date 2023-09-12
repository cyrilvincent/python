import tp_list

def min_max_avg(l):
    return tp_list.min(l), tp_list.max(l), sum(l) / len(l)


l1 = [1,2,3]
a,b,c = min_max_avg(l1)
print(a, b, c)