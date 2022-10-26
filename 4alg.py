def summ(n, k):
    s = 0 # объявляем переменную cуммы цифр
    while n > 0: # пока n больше нуля
        s += n % k # прибавляем остаток от деления
        n //= k
    return s


print(summ(int(input()), int(input())))