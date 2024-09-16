password = ''
n = int(input('Введите число от 3 до 20: '))

for i in range(1, n):
    for k in range(2, n):
        if k <= i:
            continue
        if n % (i + k) == 0:
            password += str(i) + str(k)

print(f'Пароль: {n} - {password}')