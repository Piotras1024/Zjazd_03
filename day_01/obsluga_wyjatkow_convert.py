def convert(data):
    try:
        data = int(data)
        print("Skonwertowano na int")
        return data
    except ValueError:
        try:
            data = float(data)
            print("Skonwertowano na float")
            return data
        except ValueError:
            print("Zostaje string")
            return data


x = input('Podaj dane: ')
x = convert(x)
print(x)

print('dalsza czesc kodu')
