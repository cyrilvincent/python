# Créer la fonction min_max_avg(l) => Tuple min, max ,avg avec 1 seule boucle
# Tester

def min_max_avg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for value in l:
        sum += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return min, max, sum/len(l)

if __name__ == '__main__':
    l1 = [1, 9, 3, 4, 3, 10, 99, 8, 2, 0]
    min, max, avg = min_max_avg(l1)
    print(min, max, avg)