#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = None
    if len(ingredients) < len(recipe):
            return 0
    if recipe.keys() != ingredients.keys(): #assumption: ingredient and recipe keys are sorted
        return 0


    for (k,v), (k2,v2) in zip(ingredients.items(), recipe.items()):
        if v < v2:
            return 0
        else:
            result = (v / v2)
            if batches == None or result < batches:
                batches = result

    return int(batches)

    # compare values for each key
        # if current ingredient val < current recipe val
            # batches = 0
            # return batches
        # else
            # divide ingredient val by recipe val
            # if result > batches
            # batches = result
            # continue
    # return batches
pass 

recipe1 = { 'milk': 100, 'butter': 50, 'flour': 5 }
recipe2 = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients1 = { 'milk': 132, 'butter': 48 }
ingredients2 = { 'milk': 132, 'eggs': 48, 'flour': 51 }

recipe3 = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients3 = { 'milk': 200, 'butter': 60, 'flour': 51 }

recipe4 = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients4 = { 'milk': 100, 'butter': 50, 'flour': 0 }
recipe5 = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients5 = { 'milk': 100, 'butter': 50, 'flour': 5 }

print(recipe_batches(recipe5, ingredients5))
print(recipe_batches(recipe2, ingredients2))

print(recipe_batches(recipe3, ingredients3))
print(recipe_batches(recipe4, ingredients4))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))