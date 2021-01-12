from kitchen import Rosemary
from kitchen.utensils import Bowl, BakingTray, Oven
from kitchen.ingredients import Butter, Sugar, Salt, Egg, Flour, ChocolateChips, BakingPowder
import time

# Preheat oven
oven = Oven.use()
oven.preheat(degrees=175)

# Prepare bowl with one part butter 
bowl = Bowl.use(name='batter')
bowl.add(Butter.take('one part'))

# Add 200 grams of sugar in 10 successions
for sugarpinch in range(10):
    bowl.add(Sugar.take(grams=20))
    bowl.mix()

# Add two eggs and mix with salt
for egg in Egg.take(2):
    egg.crack()
    bowl.add(egg)
bowl.add(Salt.take('pinch'))
bowl.mix()

# Add 300g of flour and 200g of choco chips separated in 5 stages
for stage in range(5):
    bowl.add(Flour.take(grams=60))
    bowl.add(ChocolateChips.take(grams=40))
    bowl.mix()

bowl.add(BakingPowder.take('some'))

# Prepare baking tray
bakingtray = BakingTray.use(name='choco chip cookies')

# Make 50 cookies from each scoop of batter
for cookie in range(20):
    bakingtray.add(bowl.take('1/20'))

# Bake baking tray in oven for 10 minutes
oven.add(bakingtray)
oven.bake(minutes=10)
oven.take()

# Let cool for 5 mins before serving
#time.sleep(300)

Rosemary.serve(bakingtray)