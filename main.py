# 1
film = input()
cinema = input()
time = input()

print(f'Билет на "{film}" в "{cinema}" на {time} забронирован')

# 2
str1 = input()
str2 = input()

if (str1.lower() == 'да' or str1.lower() == 'нет') and (str2.lower() == 'да' or str2.lower() == 'нет'):
    print('Верно')
else:
    print('Неверно')

# 3
login = input()
email = input()

if '@' not in login and '@' in email:
    print('ОК')
else:
    print('Неверный логин или email')

# 4
print(input())

# 5
string = input()

if string == '':
    print('Да')
else:
    print('Нет')

# 6
number_string = input()

max_digit = int(number_string[0])
min_digit = int(number_string[0])

for char in number_string:
    digit = int(char)

    if digit > max_digit:
        max_digit = digit

    if digit < min_digit:
        min_digit = digit

number_string = number_string.replace(str(min_digit), '', 1).replace(str(max_digit), '', 1)

sum_rem = 0
for char in number_string:
    sum_rem += int(char)

if sum_rem == (max_digit + min_digit) / 2:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')

# 7
number = int(input())

first = number % 10
second = number // 10 % 10
third = number // 100 % 10
forth = number // 1000

first, second, third, forth = sorted((first, second, third, forth))

if first == 0:
    if second != 0:
        first, second = second, first
    elif third != 0:
        third, first = first, third
    else:
        first, forth = forth, first

print(first * 1000 + second * 100 + third * 10 + forth)

# 8
count = 0
max_height = 149
min_height = 191
input_height = ''

while True:
    input_height = input()
    if input_height == '!':
        break

    height = int(input_height)

    if 149 < height < 191:
        count += 1

        if height > max_height:
            max_height = height

        if height < min_height:
            min_height = height

print(count)
print(min_height, ' ', max_height)

# 9
while True:
    password = input('Input password: ')
    password_repeat = input('Repeat password: ')

    if len(password) < 8:
        print('Короткий')
        continue
    if '123' in password:
        print('Простой')
        continue
    if password != password_repeat:
        print('Различаются')
        continue

    print('OK')
    break

# 10
while True:
    x = int(input())
    command = input()

    if command == 'x':
        print(x)
        break
    if command == '!':
        fact = 1
        for i in range(1, x + 1):
            fact *= i

        print(fact)
        continue

    y = int(input())

    match command:
        case '+':
            print(x + y)
        case '-':
            print(x - y)
        case '*':
            print(x * y)
        case '/':
            print(x // y)
        case '%':
            print(x % y)
        case _:
            print('Incorrect input')

# 11
height = int(input())

for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)

    print(spaces + stars)

# 12
number = int(input())
cur_num = 1
length = 1

while cur_num <= number:
    for _ in range(length):
        if cur_num > number:
            break

        print(cur_num, end=' ')
        cur_num += 1

    print()
    length += 1

# 13
width = int(input())
length = int(input())
symbol = input()

print(symbol * width)
for i in range(1, length):
    print(f'{symbol}{" " * (width - 2)}{symbol}')
print(symbol * width)