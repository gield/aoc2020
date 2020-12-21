with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

allergen_dict = {}  # Can't use a defaultdict because we need to do some intersections
for l in lines:
    ingredients_raw, allergens_raw = l[:-1].split(" (contains ")
    ingredients = ingredients_raw.split()
    allergens = allergens_raw.split(", ")
    for allergen in allergens:
        if allergen not in allergen_dict:
            allergen_dict[allergen] = set(ingredients)
        else:
            allergen_dict[allergen] = allergen_dict[allergen].intersection(ingredients)

final_allergen_dict = {}
while allergen_dict:
    for allergen, ingredients in allergen_dict.items():
        if len(ingredients) == 1:
            found_ingredient = next(iter(ingredients))
            final_allergen_dict[allergen] = found_ingredient
            del allergen_dict[allergen]
            for other_ingredients in allergen_dict.values():
                other_ingredients -= {found_ingredient}
            break  # We must break as we're editing allergen_dict while also looping over it

print(",".join(final_allergen_dict[allergen] for allergen in sorted(final_allergen_dict.keys())))
