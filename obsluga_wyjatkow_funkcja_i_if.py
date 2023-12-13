def can_be_int(data):
    try:
        data = int(data)
        return True
    except ValueError:
        return False


x = input('Podaj liczbe: ')
if can_be_int(x):
    print('Liczymy dalej ')
else:
    print('Podales zla liczbe')