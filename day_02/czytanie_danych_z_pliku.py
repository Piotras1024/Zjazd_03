# przeczytać plik
# wyczyścić dane
# znaleźć liczbę słów
# znaleźć liczbę różnych słów
# zapisać ilosć powórzeń każdego słowa

import argparse
from funkcje_do_czytanie_danych_z_pliku import *

parser = argparse.ArgumentParser('Description --- PL')
parser.add_argument('-f', '--filename', help='nazwa pliku bez rozszerzenia, akceptowalne tylko txt', default='U2',
                    required=False, type=str)
parser.add_argument('-now', '--no_of_words', help='Oblicza liczbe słów w pliku', action='store_true')
parser.add_argument('-noue', '--no_of_unique_elements', help='Oblicza liczbe słów w pliku', action='store_true')
parser.add_argument('-reps', '--reps_of_words', help='Oblicza liczbe słów w pliku', action='store_true')

args = parser.parse_args()

file = args.filename + '.txt'

with open(file, 'r') as u2:
    content = u2.read()


content = clear_text(content)
content = make_split(content)

if args.no_of_words:
    print(no_of_words(content))
if args.no_of_unique_elements:
    print(no_of_unique_elements(content))
if args.reps_of_words:
    print(reps_of_words(content))


# print(content)
# print(f'Liczba slow: {no_of_words(content)}')
# print(f'Liczba unikalnych slow: {no_of_unique_elements(content)}')
# print(f'Powtorzenia\n{reps_of_words(content)}')
