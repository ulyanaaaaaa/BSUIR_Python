def foo(a):
    if isinstance(a, int):
        a = str(a)
        print(a[::-1])
    elif isinstance(a, tuple):
        print(len(a))
    elif isinstance(a, list):
        sum = 0
        for num in a:
            if num == 0:
                break
            else:
                sum += num
        print(sum)
    elif isinstance(a, str):
        dict = {}
        max_count = 0
        for l in a:
            if l in dict:
                dict[l] += 1
            else:
                dict[l] = 1

        for l, count in dict.items():
            if count > max_count:
                max_count = count
                max_l = l
        print(f'Самый повторяющейся символ: {max_l}')


        print(f'Количество слов в строке: {a.count(" ") + 1}')

try:
    foo(int(input("Введите целое число: ")))
except:
    print("Неверный ввод")
try:
    foo(tuple(input("Введите кортеж: ")))
except:
    print("Неверный ввод")
try:
    foo(list(input("Введите список: ")))
except:
    print("Неверный ввод")
try:
    foo(str(input("Введите строку: ")))
except:
    print("Неверный ввод")

