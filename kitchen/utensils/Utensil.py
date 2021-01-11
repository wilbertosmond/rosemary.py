from typing import List, Optional
from kitchen.ingredients.Ingredient import Ingredient
from kitchen.Kitchen import KitchenObject, KitchenException
from kitchen.ingredients.Collections import Stack, Mixture, Portion, CookedCollection, BakedCollection, PieCollection, ChilledCollection

class Utensil(KitchenObject):
    '''A Kitchen Utensil to modify or combine Ingredients in specific ways.'''
    pass

class Plate(Utensil):
    '''A Kitchen Utensil to serve and/or collect Ingredients.'''

    @staticmethod
    def use(name: str = None) -> 'Plate':
        '''Returns a Plate object with the given name.

        Args:
            name (str): the name to assign to the contents of the Plate.

        Returns:
            Plate: a new Plate object with the given name.
        '''
        
        return Plate(name=name)
    
    def __init__(self, name: str = None):
        self.contents = Stack(name=name)
    
    def add(self, item: Ingredient):
        '''Adds the given item onto the Plate.

        Args:
            item (Ingredient): the item, which should be an Ingredient, to add onto the Plate.
        '''

        self.contents._add(item)
    
    def __str__(self):
        return f'a plate with {self.contents}'

class Bowl(Utensil):
    '''A Kitchen Utensil for mixing Ingredients and dividing this mixture into other Utensils.'''
    
    @staticmethod
    def use(name: str = None) -> 'Bowl':
        '''Returns a Bowl object with the given name.

        Args:
            name (str): the name to assign to the contents of the Bowl.

        Returns:
            Bowl: a new Bowl object with the given name.
        '''

        return Bowl(name=name)
    
    def __init__(self, name: str = None):
        self.contents = Mixture(name=name)
    
    def add(self, item: Ingredient):
        '''Adds the given item to the Bowl.

        Args:
            item (Ingredient): the item, which should be an Ingredient, to add to the Bowl.

        Raises:
            KitchenException: when you try to add anything after using your mixture.
        '''

        if isinstance(self.contents, Mixture):
            self.contents._add(item)
        else:
            raise KitchenException('You can only add ingredients before using your mixture!')
    
    def mix(self):
        '''Mixes the current contents of the Bowl.

        Raises:
            KitchenException: when you try to mix after using your mixture.
        '''
        
        if isinstance(self.contents, Mixture):
            self.contents._mix()
        else:
            raise KitchenException('You can only mix ingredients before using your mixture!')

    def take(self, portion: str = '1') -> Portion:
        '''Returns a given portion of the current contents of the Bowl. The Mixture cannot be further altered after having taken part of it.

        Args:
            portion (str): the fraction of the current contents of the Bowl to return, as a string (e.g. '1/4'). Defaults to '1'.

        Returns:
            Portion: the given portion of the current contents of the Bowl.
        '''
        
        if isinstance(self.contents, Mixture):
            self.contents = Portion(self.contents)
        return self.contents._take(portion)
    
    def divide(self, portions: int) -> List[Portion]:
        '''Returns a list with a given number of equally divided portions of the current contents of the Bowl.

        Args:
            portions (int): the number of desired portions to divide the current contents of the Bowl into.

        Raises:
            KitchenException: when you try to divide the contents after having already taken part of them.

        Returns:
            List[Portion]: a list of equally divided portions of the current contents of the Bowl.
        '''
        
        if isinstance(self.contents, Mixture):
            return [self.take(f'1/{portions}') for i in range(portions)]
        else:
            raise KitchenException('You can only divide bowl contents before using your mixture in another way!')

    def __str__(self):
        return f'a bowl with {self.contents}'

class Pan(Utensil):
    '''A Kitchen Utensil for cooking Ingredients.'''
    
    @staticmethod
    def use(name: str = None) -> 'Pan':
        '''Returns a Pan object with the given name.

        Args:
            name (str): the name to assign to the contents of the Pan.

        Returns:
            Pan: a new Pan object with the given name.
        '''

        return Pan(name=name)
    
    def __init__(self, name: str = None):
        self.contents = CookedCollection(name=name)
    
    def add(self, item: Ingredient):
        '''Adds the given item to the Pan.

        Args:
            item (Ingredient): the item, which should be an Ingredient, to add to the Pan.
        '''

        self.contents._add(item)
    
    def cook(self, minutes: float = 1):
        '''Cooks the current contents of the Pan, on the current side, for the given number of minutes.

        Args:
            minutes (float): the number of minutes for which to cook the current contents of the Pan.
        '''
        
        self.contents._cook(minutes)

    def flip(self):
        '''Flips the current contents of the Pan.'''
        
        self.contents._flip()

    def take(self) -> CookedCollection:
        '''Returns the contents of the Pan.

        Returns:
            CookedCollection: the current contents of the Pan, as a CookedCollection.
        '''

        contents = self.contents
        self.contents = CookedCollection(name=contents.name)
        return contents

    def __str__(self):
        return f'a pan with {self.contents}'

class BakingUtensil(Utensil):
    '''A Kitchen Utensil to collect Ingredients for baking.'''
    
    def __init__(self, name: str = None):
        self.contents = BakedCollection(name=name)

    def add(self, item: Ingredient):
        '''Adds the given item to the BakingUtensil container.

        Args:
            item (Ingredient): the item, which should be an Ingredient, to add to the BakingUtensil container.
        '''

        self.contents._add(item)
    
    def _bake(self, temperature: int = 20, minutes: float = 1):
        self.contents.temperature = temperature
        self.contents._bake(minutes)

    def take(self) -> BakedCollection:
        '''Returns the contents of the BakingUtensil.

        Returns:
            BakedCollection: the current contents of the BakingUtensil, as a BakedCollection.
        '''

        contents = self.contents
        self.contents = BakedCollection(name=contents.name)
        return contents
        
class BakingTray(BakingUtensil):
    '''A Kitchen Utensil to collect Ingredients for baking.'''

    @staticmethod
    def use(name: str = None) -> 'BakingTray':
        '''Returns a BakingTray object with the given name.

        Args:
            name (str): the name to assign to the contents of the BakingTray.

        Returns:
            BakingTray: a new BakingTray object with the given name.
        '''

        return BakingTray(name=name)
    
    def __init__(self, name: str = None):
        super().__init__(name)

    def __str__(self):
        return f'a tray with {self.contents}'

class PieDish(BakingUtensil):
    '''A Kitchen Utensil to collect Ingredients for baking.'''
    
    @staticmethod
    def use(name: str = None) -> 'PieDish':
        '''Returns a PieDish object with the given name.

        Args:
            name (str): the name to assign to the contents of the PieDish.

        Returns:
            PieDish: a new PieDish object with the given name.
        '''

        return PieDish(name=name)
    
    def __init__(self, name: str = None):
        self.contents = PieCollection(name=name)

    def take(self) -> PieCollection:
        '''Returns the contents of the PieDish.

        Returns:
            PieCollection: the current contents of the PieDish, as a PieCollection.
        '''

        contents = self.contents
        self.contents = PieCollection(name=contents.name)
        return contents

    def __str__(self):
        return f'a pie dish containing {self.contents}'

class Oven(Utensil):
    '''A Kitchen Utensil to bake Ingredients in using a BakingUtensil, for instance a BakingTray or PieDish.'''
    
    @staticmethod
    def use(degrees: int = 20) -> 'Oven':
        '''Returns an Oven object preheated to the given temperature.

        Args:
            degrees (int): the temperature to preheat the Oven to. Defaults to 20 (room temperature).

        Returns:
            Oven: a new Oven object preheated to the given temperature.
        '''

        return Oven(degrees=degrees)
    
    def __init__(self, degrees: int = 20, name: str = None):
        self.contents = None
        self.degrees = degrees

    def preheat(self, degrees: int = 20):
        '''Preheats the Oven to the given temperature.

        Args:
            degrees (int): the temperature to preheat the Oven to. Defaults to 20 (room temperature).
        '''

        self.degrees = degrees

    def add(self, item: BakingUtensil):
        '''Adds the given item to the Fridge.

        Args:
            item (BakingUtensil): the item, which should be a BakingUtensil, to add to the Oven.

        Raises:
            KitchenException: when you try to add anything except a BakingUtensil to the Oven, or if the oven is already in use.
        '''

        if not isinstance(item, BakingUtensil):
            raise KitchenException('Can only put suitable container into the oven!')
        if self.contents is not None:
            raise KitchenException('Can only put one container into the oven at a time!')
        self.contents = item
    
    def bake(self, minutes: float = 1):
        '''Bake the current contents of the Oven for a given number of minutes.

        Args:
            minutes (float): the number of minutes to bake the current contents of the Oven for. Defaults to 1.

        Raises:
            KitchenException: when the Oven is currently empty.
        '''

        if self.contents is None:
            raise KitchenException('Cannot bake nothing!')
        self.contents._bake(self.degrees, minutes)
    
    def take(self) -> Optional[BakingUtensil]:
        '''Returns the BakingUtensil that was added to the Oven, if any.

        Returns:
            BakingUtensil: the most recent BackingUtensil that was put in the Oven.
        '''

        contents = self.contents
        self.contents = None
        return contents

    def __str__(self):
        return f'an oven with {self.contents}'

class Fridge(Utensil):
    '''A Kitchen Utensil to cool Ingredients before use.'''
    
    @staticmethod
    def use(degrees: int = 5) -> 'Fridge':
        '''Returns a Fridge object set to the given temperature.

        Args:
            degrees (int): the temperature to set the Fridge to. Defaults to 5.

        Returns:
            Fridge: a new Fridge object set to the given temperature.
        '''

        return Fridge(degrees=degrees)
    
    def __init__(self, degrees: int = 5):
        self.temperature = degrees
        self.contents = []
    
    def add(self, item: Bowl):
        '''Adds the given item to the Fridge.

        Args:
            item (Bowl): the item, which should be a Bowl, to add to the Fridge.

        Raises:
            KitchenException: when you try to add anything except a Bowl to the Fridge.
        '''

        if not isinstance(item, Bowl):
            raise KitchenException('You can only add a bowl to the fridge!')
        contents = item.contents
        chilled_contents = ChilledCollection(temperature=self.temperature)
        chilled_contents._add(contents)
        item.contents = Mixture(None)
        item.contents._add(chilled_contents)
        self.contents.append(item)
    
    def set_temperature(self, degrees: int = 5):
        '''Sets the Fridge to the given temperature.

        Args:
            degrees (int): the temperature to set the Fridge to. Defaults to 5.
        '''

        for item in self.contents:
            item.contents.contents[0].temperature = degrees

    def take(self) -> Bowl:
        '''Returns the last item that was added to the Fridge.

        Returns:
            Bowl: the last item, which will be a Bowl, that was added to the Fridge.
        '''
        return self.contents.pop()

    def __str__(self):
        return f'a fridge with {self.contents}'
