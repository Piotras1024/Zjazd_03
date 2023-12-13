
try:
    x = int(input('Podaj 1sza liczbe: '))
    y = int(input('Podaj 2ga liczbe: '))
    result = x / y
except ZeroDivisionError:
    print('Wyskoczyl blad')
    raise ZeroDivisionError
except ValueError:
    raise ValueError
else:
    print('Udalo sie')
finally:
    print('Zbieram logi')

# finally i tak zostanie wykonane !
# raise podnosi problem i go wyświetla