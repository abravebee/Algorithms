#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # batches = 0
    # if ingredients length < recipe length (amount of keys)
        # return batches
    # if ingredients keys don't match recipe keys
        # return batches
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


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))