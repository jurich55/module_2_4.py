print()
# отработка темы "Циклы". Д.З. module_2_4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, 16):
    is_prime = 0
    j = 2           #"2"- уже простое число, по-этому его сразу исключаем из цикла
    for j in range(1, i):
        if i % j == 0:
            is_prime += 1
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
print()
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)