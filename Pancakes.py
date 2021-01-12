from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk

# Take a bowl
bowl = Bowl.use(name='batter')

# Add the 2 eggs to the batter and mix
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Add a dash of salt and mix in flour in 5 batches of 50 grams
bowl.add(Salt.take('dash'))
for flour in range(5):
    bowl.add(Flour.take(grams=50))
    bowl.mix()

# Add in 2 x half milk and mix
for milk in range(2):
    bowl.add(Milk.take(ml=250))
    bowl.mix()

# Prepare plate
plate = Plate.use()
pan = Pan.use(name='pancakes')
# Make 8 pancakes
for serve in range(8):
    # Make a pancake
    pan.add(Butter.take('slice'))
    pan.add(bowl.take(1/8))
    for side in range(2):
        pan.cook(minutes=1)
        pan.flip()
    plate.add(pan.take())
Rosemary.serve(plate)