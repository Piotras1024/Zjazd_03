
try:
    x = int(input('Podaj 1sza liczbe: '))
    y = int(input('Podaj 2sza liczbe: '))
    result = x / y
    print('dzielenie ok')
except ZeroDivisionError:
    result = x
    print('Blad, zwracam pierwsza liczbe')
except ValueError:
    result = 0

print(f"Wynik to {result}")
