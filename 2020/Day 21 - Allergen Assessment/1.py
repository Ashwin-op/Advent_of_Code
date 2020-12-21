def parse_raw(raw):
    lines = raw.splitlines()
    rv = []
    all_ingredients = set()
    all_allergens = set()
    for line in lines:
        ingredients, allergens = line[:-1].split(" (contains ")
        these_ingredients = set(ingredients.split())
        these_allergens = set(allergens.split(", "))
        all_ingredients |= these_ingredients
        all_allergens |= these_allergens
        rv.append((these_ingredients, these_allergens))
    return rv, all_ingredients, all_allergens


with open("input.txt") as fp:
    foods, ingredients, allergens = parse_raw(fp.read())

allergen_map = {ingredient: allergens.copy() for ingredient in ingredients}
for food_ingredients, food_allergens in foods:
    for ingredient in ingredients - food_ingredients:
        allergen_map[ingredient] -= food_allergens
no_allergens = {k for k, v in allergen_map.items() if len(v) == 0}

print(sum(len(fi & no_allergens) for fi, fa in foods))
