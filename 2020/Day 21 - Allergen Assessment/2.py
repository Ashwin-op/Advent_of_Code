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
while any(len(fa) > 1 for fa in allergen_map.values()):
    for ingredient, allergen in allergen_map.items():
        if len(allergen) == 1:
            for other_ingredient in ingredients - {ingredient}:
                allergen_map[other_ingredient] -= allergen
cdil = sorted(
    [(fi, next(iter(fa))) for fi, fa in allergen_map.items() if len(fa) == 1],
    key=lambda i: i[1],
)

print(",".join(fi for fi, fa in cdil))
