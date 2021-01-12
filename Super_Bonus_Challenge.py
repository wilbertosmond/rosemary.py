from kitchen import Rosemary
from kitchen.utensils import Bowl, BakingTray, PieDish, Oven, Fridge
from kitchen.ingredients import Water, Butter, Sugar, Salt, Egg, Flour, Apple, Cornstarch, Cinnamon, Lemon

## ----- Step 1 -----
# Prepare cold water  
bowl_coldwater = Bowl.use(name='coldwater')
bowl_coldwater.add(Water.take(ml=500))
fridge = Fridge.use()
fridge.add(bowl_coldwater)

# Preheat oven
oven = Oven.use()
oven.preheat(degrees=180)

## ----- Step 2 ------
# Prepare bowl for mixture
bowl_mixture = Bowl.use(name='mixture')

# Mix ingredients
bowl_mixture.add(Flour.take(grams=300))
bowl_mixture.add(Salt.take('teaspoon'))
for butter in range(5):
    bowl_mixture.add(Butter.take(grams=50))
    bowl_mixture.mix()

# Add the chilled water into mixture bowl
fridge.take()
bowl_mixture.add(bowl_coldwater.take())
fridge.add(bowl_mixture)

## ----- Step 3 -----
# Prepare bowl for filling
bowl_filling = Bowl.use(name='filling')

# Peel and slice apple, and add to filling bowl
for apple in Apple.take(6):
    apple.peel()
    apple.slice()
    bowl_filling.add(apple)

# Zest and juice a lemon, and add to filling bowl
lemon = Lemon.take()
lemonzest = lemon.zest()
lemonjuice = lemon.squeeze()
bowl_filling.add(lemonzest.take('1/2'))
bowl_filling.add(lemonjuice.take('1/2'))

# Add the rest of the filling ingredients into the bowl
bowl_filling.add(Sugar.take(grams=150))
bowl_filling.add(Cornstarch.take('spoon'))
bowl_filling.add(Salt.take('pinch'))
bowl_filling.add(Cinnamon.take('teaspoon'))
bowl_filling.mix()

# Separate bowl for mixed egg
bowl_egg = Bowl.use(name='egg')
egg = Egg.take()
egg.crack()
bowl_egg.add(egg)
bowl_egg.mix()

## ----- Step 4 -----
# Prepare pie dish
piedish = PieDish.use()
piedish.add(bowl_mixture.take('3/4'))
piedish.add(bowl_filling.take())
piedish.add(bowl_mixture.take('1/4'))
piedish.add(bowl_egg.take())
piedish.add(Sugar.take('spoon'))
piedish.add(lemonzest.take('1/2'))
piedish.add(lemonjuice.take('1/2'))

# Bake pie dish in oven for 60 minutes
oven.add(piedish)
oven.bake(minutes=60)
oven.take()

Rosemary.serve(piedish)