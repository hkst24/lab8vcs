# 1 пункт
# изи лаба
# питон - лучший язык!
print("1 пункт")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
print("Максимальное", max(a, b, c))

# 2 пункт
print("2 пункт")
chisla = list(map(int, input("Введите числа через пробел: ").split()))
print("Положительных", sum(i > 0 for i in chisla))

# 3 пункт
print("3 пункт")
while True:
    a = input("Введите a: ")
    if a.isspace() or a == "":
        print("Почему вы ничего не ввели??? Придется перезапускать прогу...")
    else:
        break
if a.isdigit() == True:
    print("Урааа это цифорка")
elif a.islower() or a.isupper():
    print("БУКВЫ БУКВЫ БУКВЫ")
else:
    print("Эхх это всего лишь знак")

# 4 пункт
print("4 пункт")
a = (input("Введите число: "))
print(a.isdigit())

# 5 пункт
print("5 пункт")
a = float(input("a = "))
while a <= 0:
    print("Не не не, давайте заново")
    a = float(input("a = "))
b = float(input("b = "))
while b <= 0:
    print("Что? Опять??")
    b = float(input("b = "))
c = float(input("c = "))
while c <= 0:
    print("Не, ну вы совсем уже...")
    c = float(input("c = "))
if a + b < c:
    print("Нее, это не треугольник")
elif c + b < a:
    print("Нее, это не треугольник")
elif c + a < b:
    print("Нее, это не треугольник")
else:
    print("Ооо это треугольник, причем периметр которого будет равен: ", a+b+c)

# 6 пункт
print("6 пункт")
a = str(input("Введите a: "))
if a[0]+a[1]+a[2] == a[3]+a[4]+a[5]:
    print("ДААА СЧАСТЛИВЫЙ БИЛЕТ")
else:
    print("Ну, просто билетик")




