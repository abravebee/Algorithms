#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = 0
    if len(ingredients) < len(recipe):
            return batches
    if recipe.keys() != ingredients.keys(): #assumption: ingredient and recipe keys are sorted
        return batches
    i = 0
    k = 0
    for i in range(0, len(recipe)):
        if ingredients[k] < recipe[k]:
            batches = 0
            return batches
        else:
            result = (ingredients[k] / recipe[k])
            if result < batches:
                batches = result
                k +=1
    return batches

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

print(recipe_batches(recipe1, ingredients1))
print(recipe_batches(recipe2, ingredients2))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))