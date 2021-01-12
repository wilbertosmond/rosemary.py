from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, BakingTray, Oven
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk, ChocolateChips, BakingPowder

##### ---------- Rescaling Pancakes

# input number of pancakes to function pancake(n)
# returns ingredients scaled to the number of pancakes
def pancake(n_pancakes):
    # Convert number of pancakes to number of recipes
    n = int(n_pancakes/8)

    # Take a bowl
    bowl = Bowl.use(name='batter')

    # Add the 2n eggs to the batter and mix
    for egg in Egg.take(2*n):
        egg.crack()
        bowl.add(egg)
    bowl.mix()

    # Add a dash of salt and mix in flour in 5n batches of 50n grams
    bowl.add(Salt.take('dash'))
    for flour in range(5*n):
        bowl.add(Flour.take(grams=50))
        bowl.mix()

    # Add in 2n x half milk and mix
    for milk in range(2*n):
        bowl.add(Milk.take(ml=250))
        bowl.mix()

    # Prepare plate
    plate = Plate.use()
    pan = Pan.use(name='pancakes')
    # Make 8n pancakes

    for serve in range(n_pancakes):
        # Make a pancake
        pan.add(Butter.take('slice'))
        pan.add(bowl.take(1/n_pancakes))
        for side in range(2):
            pan.cook(minutes=1)
            pan.flip()
        plate.add(pan.take())
    
    return Rosemary.serve(plate)

print(pancake(16)) # input scale of 8

##### ---------- Rescaling Cookies

# input number of pancakes to function cookies(n)
# returns ingredients scaled to the number of cookies
def cookie(n_cookies):
    # Convert number of pancakes to number of recipes (assuming one recipe can make 20 cookies)
    n = int(n_cookies/20)

    # Preheat oven
    oven = Oven.use()
    oven.preheat(degrees=175)

    # Prepare bowl with one part butter 
    bowl = Bowl.use(name='batter')
    bowl.add(Butter.take('one part'))

    # Add 200 grams of sugar in 10n successions
    for sugarpinch in range(10*n):
        bowl.add(Sugar.take(grams=20))
        bowl.mix()

    # Add two eggs and mix with salt
    for egg in Egg.take(2*n):
        egg.crack()
        bowl.add(egg)
    bowl.add(Salt.take('pinch'))
    bowl.mix()

    # Add 300g of flour and 200g of choco chips separated in 5n stages
    for stage in range(5*n):
        bowl.add(Flour.take(grams=60))
        bowl.add(ChocolateChips.take(grams=40))
        bowl.mix()

    bowl.add(BakingPowder.take('some'))

    # Prepare baking tray
    bakingtray = BakingTray.use(name='choco chip cookies')

    # Make 50n cookies from each scoop of batter
    for cookie in range(n_cookies):
        bakingtray.add(bowl.take(1/n_cookies))

    # Bake baking tray in oven for 10 minutes
    oven.add(bakingtray)
    oven.bake(minutes=10)
    oven.take()

    return Rosemary.serve(bakingtray)

print(cookie(10))