from kitchen import Rosemary
from kitchen.utensils import Pan, Plate
from kitchen.ingredients import Butter, Egg, Salt

egg = Egg.take()
egg.crack()

pan = Pan.use(name='omelette')
pan.add(Butter.take('slice'))
pan.add(egg)
pan.add(Salt.take('dash'))
pan.cook(minutes=2)

plate = Plate.use()
omelette = pan.take()
plate.add(omelette)

Rosemary.serve(plate)
