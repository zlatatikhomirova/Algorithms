left = -1
right = n

while right - left > 1:
    middle = (left + right) // 2 # именно такая формула для среднего индекса между left и right
    if a[middle] == 1:
        right = middle # right всегда должна указывать на 1
    else:
        left = middle # left всегда должна указывать на 0
print left, right
print a[left], a[right]

a = [1, 3, 4, 10, 10, 10, 11, 80, 80, 81] # отсортированный массив
def bin_search(a, x):
    n = len(a)
    left = -1
    right = n
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] >= x: # практически единственная строка, которая меняется от задачи к задаче
            right = middle
        else:
            left = middle
    if right != n and a[right] == x: # ответ лежит в right
        return True
    else:
        return False

print (bin_search(a, 1))
print (bin_search(a, 10))
print (bin_search(a, 20))
print (bin_search(a, 79))
print (bin_search(a, 80))
print (bin_search(a, 81)
       
* Найти первое число, равное X в отсортированном массиве, или вывести, что таких чисел нет * Найти последнее число, равное X в отсортированном массиве, или вывести, что таких чисел нет * Посчитать, сколько раз встречается число X в отсортированном массиве (в решении помогают два предыдущих пункта) * Дан массив чисел, первая часть состоит из нечетных чисел, а вторая - из четных. Найти индекс, начиная с которого все числа четные.

Все эти задачи решаются бинарным поиском за . Правда нужно понимать, что в чистом виде такую задачу решать двоичным поиском бессмысленно - ведь чтобы создать массив размера , уже необходимо потратить  операций.
