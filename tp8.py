def demotuple(l):
    # Traitement complexe
    #return (0,100,50)
    return 0, 100, 50

tuple = demotuple([1,2,3,4])
print(tuple[0], tuple[1], tuple[2])

(a,b,c) = demotuple([1,2,3,4])
print(a, b, c)

a,b,c = demotuple([1,2,3,4])
print(a, b, c)

#Faire la fonction min_max_avg(l) qui retourne le mi, max et average en une seule itération codées à la main
#Tester

def min_max_avg(l):
    sum = 0
    min = l[0]
    max = l[0]
    for val in l:
        sum += val
        if val < min:
            min = val
        elif val > max:
            max = val
    return min, max, sum / len(l)

min, max,avg = min_max_avg(range(100))
print(min,max,avg)