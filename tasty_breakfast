# A functional breakfast

"""
Purpose: Make code more readable, reuse multiple times, write shorter code
"""

def mix_and_cook():
    print('mix ingredients')
    print('pour mixture onto pan')
    print('cook 1st side ')
    print('alright flip')
    print('cook 2nd side')
    omelette = 'a tasty omelette'

def make_pancake():
   mix_and_cook()
   pancake = 'good pancake'
   return pancake

def make_omelette(ingredients):
    mix_and_cook()
    omelette = 'a {} omelette' .format(ingredients)
    return omelette

def okay_omelette(*ingredients):
    mix_and_cook()
    omelette = 'an okay omelette with {} ingredients' .format(len(ingredients))
    return omelette

print(make_omelette)
print(make_pancake)

# Make some regular omelettes
print(make_omelette('tomato'))
print(make_omelette('cheese'))

print(okay_omelette('sausage', 'onion', 'pepper', 'spinach', 'mushroom', 'tomato'))
