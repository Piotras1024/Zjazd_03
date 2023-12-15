def myfuntion(a, b, c):
    return a + b + c


def argfunction(*argv):
    for arg in argv:
        print(arg)
    print(f'koniec,przetworzono {len(argv)} elementow')

def message_to_employee(varialbe,  *ids, profit = 0):
    for id in ids:
        print('Przygotowuje wiadomosc')
        print('tworze plik id.txt')
        print(f'Witaj {id} Zysk w firmie za rok 2023 wynosi {profit}')

my_list = ['Kamil', 'Michal', 'Tomasz', 'Rafal']


message_to_employee(99878, 2343, 32423, 6444, profit=2300000)

def create_member(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

create_member(name='Kamil', surname='Kowalski')
create_member(name='Koronowski', surname='aaa', age=22, hobby='ski')

def draw_lines(start: list, *points: list):
    begin = start
    for point in points:
        print(f'narysu kreske od {begin} do {point}')
        begin = point

def send_email(**member):
    print(f"Witaj {member['name']}, masz {member['wiek']} lat")
    if 'urlop' in member.keys():
        print(f'masz {member["urlop"]} dni urlopu')
        if member["urlop"] > 10:
            print('Wysylam na pryzmusowy urlop')

send_email(name='Kamil', urlop=14, wiek=28)


def total_funcion(pierwszy, drugi,  *args, trzeci=0, czwarty=1, **kwargs):
    pass


total_funcion(3, 4, 5, 6, imie='Kamil', wiek=33, pies='jamnik')
