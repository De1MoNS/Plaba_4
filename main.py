from math import sqrt
from num2words import num2words


# 3 Задание
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")


triangle(5, 7, 3)


# 4 Задание
def distance(x1, y1, x2, y2):
    print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


distance(0, 0, 5, 4)


# 5 Задание
def number_to_words(n):
    try:
        print(num2words(n, lang='ru'))
    except NotImplementedError:
        print(num2words(n, lang='en'))


number_to_words(int(input()))


# 7 Задание
def palindrome(s):
    st = s.lower().replace(" ", "")
    if st == st[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"


print(palindrome("А роза упала на лапу Азора"))
print(palindrome("Палиндром"))

# 9 Задание
dup = []


def print_without_duplicates(message):
    if message not in dup:
        dup.append(message)
        print(message)


print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")

# 10 Задание
fr = {}


def add_friends(name_of_person, list_of_friends):
    fr[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    if name_of_person1 in fr:
        return name_of_person2 in fr[name_of_person1]


def print_friends(name_of_person):
    if name_of_person in fr:
        friend = sorted(fr[name_of_person])
        print("".join(friend))
    else:
        print("Нет друзей")


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
print_friends("Алла")

# 13 Задание
arr = [5, 3, 7, 8, 2]
arr2 = [5, 3, 7, 8, 2]
s = sorted(arr)  # Создает новый отсортированный список
arr2.sort()  # Сортирует старый список
print(s)
print(arr)
print(arr2)

# 14 Задание
Код
должен
разделить
массив
на
массив
на
четные
и
нечетные
числа
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

# 15 Задание
level = [1, 1]
fractal = [0, level, level, 2]
print(fractal)


# 16 Задание
def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)


sequence = [1, 1, 2, 3]
continue_fibonacci_sequence(sequence, 3)
print(*sequence)


# 17 Задание
def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)
    return arr


arr = [1, 2]
mirror(arr)
print(*arr)


# 18 Задание
def from_string_to_list(string, container):
    c = string.split()
    container.extend(c)


a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)


# 20 Задание
def swap(first, second):
    first[:], second[:] = second[:], first[:]


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)


# 21 Задание
def defractalize(fractal):
    el = []
    for i in fractal:
        if i is not fractal:
            el.append(i)
    fractal[:] = el


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)
