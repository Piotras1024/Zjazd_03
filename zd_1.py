available = {'mleko': 3, 'jajko': 25, 'maka': 3, 'cukier': 4, 'maliny': 3}
cake = {'mleko': 1, 'jajko': 12, 'maka': 0.5, 'cukier': 0.3}
cake_extra = {'mleko': 1, 'jajko': 0.5, 'maka': 1, 'maliny': 2.6}
cake_super = {'mleko': 1.2, 'jajko': 1, 'maka': 1.6}


def the_most_critical_ingredient(missing_ingredients: dict) -> str:
    list_of_critical_ingredients = []
    min_amount = min(missing_ingredients.values())
    if min_amount <= 1:
        answer = f"Brakuje {min_amount} jednostki takich artykółów jak :"
    else:
        answer = f"Brakuje {min_amount} jednostek :"

    for ingredient, amount in missing_ingredients.items():
        if amount == min_amount:
            list_of_critical_ingredients.append(ingredient)
    for ingredient in list_of_critical_ingredients:
        answer = answer + f"\n- {ingredient}"
    answer = answer + "."
    return answer


def how_many_cakes_to_use_all_available(available_ingredients: dict, cake_recipe: dict) -> int:
    """
    Oblicza maksymalną liczbę ciast, które można zrobić, wykorzystując całą dostępną ilość każdego
    składnika. Zwraca liczbę ciast opartą na składniku, którego jest najwięcej w stosunku do wymagań
    przepisu.
    """
    dict_cakes_from_ingredient = dict()
    for ingredient in cake_recipe:
        if ingredient in available_ingredients:
            counting = available_ingredients[ingredient] / cake_recipe[ingredient]
            dict_cakes_from_ingredient[ingredient] = counting
        else:
            continue
    return int(max((dict_cakes_from_ingredient.values())))


def missing_ingredients_to_use_all_available(available_ingredients: dict, cake_recipe: dict) -> dict:
    """
    Zwraca brakujące składniki, aby zrobić maksymalną liczbę ciast, które wykorzystują całą dostępną
    ilość każdego składnika.
    """
    max_possible_cakes = how_many_cakes_to_use_all_available(available_ingredients, cake_recipe)
    ingredients_needed_for_max_cakes = {}
    for ingredient, amount in cake_recipe.items():
        total_needed = amount * max_possible_cakes
        if ingredient in available_ingredients:
            needed = round(total_needed - available_ingredients[ingredient], 2)
            if needed > 0:
                ingredients_needed_for_max_cakes[ingredient] = needed
        else:
            ingredients_needed_for_max_cakes[ingredient] = round(total_needed, 2)

    return ingredients_needed_for_max_cakes


def how_many_cakes(available_ingredients: dict, cake_recipe: dict) -> int:
    """
    Zwraca ile ciast można zrobić z dostępnych składników
    """
    dict_cakes_from_ingredient = dict()
    for ingredient in cake_recipe:
        if ingredient in available_ingredients:
            counting = available_ingredients[ingredient] / cake_recipe[ingredient]
            dict_cakes_from_ingredient[ingredient] = counting
        else:
            # Jeśli nie ma składnika, nie można zrobić ciasta
            return 0
    return int(min((dict_cakes_from_ingredient.values())))


def calculate_missing_ingredients(available_ingredients: dict, full_needed_ingredients: dict) -> dict:
    ingredients_missing = {}
    for ingredient, amount in full_needed_ingredients.items():
        if ingredient in available_ingredients:
            needed = round(amount - available_ingredients[ingredient], 2)
            if needed > 0:
                ingredients_missing[ingredient] = needed
        else:
            ingredients_missing[ingredient] = amount
    return ingredients_missing


def missing_ingredients_to_next_cake(available_ingredients: dict, cake_recipe: dict) -> dict:
    """
    Zwraca ile i których składników brakuje, aby zrobić 1 ciasto więcej
    """
    actual_max = how_many_cakes(available_ingredients, cake_recipe)
    full_needed_ingredients = {ingredient: round(amount * (actual_max + 1), 2) for ingredient, amount in cake_recipe.items()}
    ingredients_missing = calculate_missing_ingredients(available_ingredients, full_needed_ingredients)
    return ingredients_missing


def missing_ingredients_to_amount_cake(available_ingredients: dict, cake_recipe: dict, number_cakes: int) -> dict:
    """
    Zwraca ile i których składników brakuje, aby zrobić number_cakes ciast, dowolną liczbe ciast podaną
    jako parametr
    """
    full_needed_ingredients = {ingredient: round(amount * number_cakes, 2) for ingredient, amount in cake_recipe.items()}
    ingredients_missing = calculate_missing_ingredients(available_ingredients, full_needed_ingredients)
    return ingredients_missing


cakes = how_many_cakes(available, cake_extra)
missing_ingr = missing_ingredients_to_next_cake(available, cake_extra)
missing_ingr_amount = missing_ingredients_to_amount_cake(available, cake_extra, 12)
how_many_cakes_to_use_all = how_many_cakes_to_use_all_available(available, cake_extra)
missing_ingr_to_use_all = missing_ingredients_to_use_all_available(available, cake_extra)

print(cakes)
print(missing_ingr)
print(missing_ingr_amount)
print()
print(how_many_cakes_to_use_all)
print(missing_ingr_to_use_all)

print(the_most_critical_ingredient(missing_ingr))
