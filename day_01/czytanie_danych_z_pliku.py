# przeczytać plik
# wyczyścić dane
# znaleźć liczbę słów
# znaleźć liczbę różnych słów
# zapisać ilosć powórzeń każdego słowa

with open('U2.txt', 'r') as u2:
    content = u2.read()


from funkcje_do_czytanie_danych_z_pliku import *

content = clear_text(content)
content = make_split(content)
print(content)

print(counting_words_in_list(content))
print(counting_unique_words_in_string(content))
print(reps_of_word(content))
