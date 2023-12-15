import argparse
from funkcje_do_czytanie_danych_z_pliku import *

parser = argparse.ArgumentParser('Description --- PL')
parser.add_argument('-f', '--filename', help='nazwa pliku bez rozszerzenia, akceptowalne tylko txt', default='U2',
                    required=False, type=str)
parser.add_argument('-now', '--no_of_words', help='Oblicza liczbe słów w pliku', type=int, default=0, required=False)
parser.add_argument('-noue', '--no_of_unique_elements', help='Oblicza liczbe słów w pliku', type=int, default=0,
                    required=False)
parser.add_argument('-reps', '--reps_of_words', help='Oblicza liczbe słów w pliku', type=int, default=0, required=False)
parser.add_argument('-op', '--operations', help='''1 to uruchomienie operacji, 0 to pominięcie operacji. Znak 1 oznacza,
                    liczenie słów w tekście, znak drugi oznacza liczenie unikalnych słów w tekście, znak trzeci oznacza
                    utworzenie słownika z powtórzeniami słów''', type=str, default='000', required=False)

args = parser.parse_args()

file = args.filename + '.txt'

with open(file, 'r') as u2:
    content = u2.read()


content = clear_text(content)
content = make_split(content)

if args.operations[0] == '1':
    print(no_of_words(content))
if args.operations[1] == '1':
    print(no_of_unique_elements(content))
if args.operations[2] == '1':
    print(reps_of_words(content))

# if args.no_of_words:
#     print(no_of_words(content))
# if args.no_of_unique_elements:
#     print(no_of_unique_elements(content))
# if args.reps_of_words:
#     print(reps_of_words(content))
