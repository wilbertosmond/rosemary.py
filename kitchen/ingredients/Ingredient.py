from copy import copy
from typing import List, Optional, Union
from kitchen.Kitchen import KitchenObject, KitchenException

class Ingredient(KitchenObject):
    '''An Ingredient in Rosemary's Kitchen.'''

    @staticmethod
    def _take(ingredient: type, amount: int):
        if amount <= 0:
            raise KitchenException('Cannot take non-positive amount!')
        return [ingredient() for i in range(amount)] if amount > 1 else ingredient()

    def __init__(self):
        self.name = 'unknown'
        self.amount = -1
        raise KitchenException('Cannot initiate abstract ingredient!')

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        return isinstance(other, Ingredient) and self.name == other.name
    
    def __iter__(self):
        return iter([self])

class UncountableIngredient(Ingredient):
    '''An uncountable Ingredient in Rosemary's Kitchen.'''
    
    @staticmethod
    def _take(ingredient: type, unit: str, amount: Optional[str], units: Optional[int]):
        if units is not None:
            return ingredient(f'{units} {unit}')
        elif amount is not None:
            return ingredient(amount)
        else:
            raise KitchenException('Can\'t take nothing!')

    def __init__(self, name: str, amount: str):
        if not isinstance(amount, str):
            raise KitchenException('Cannot take scalar amount of uncountable ingredient!')
        
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.amount} of {self.name}' if isinstance(self.amount, str) else \
               f'{self.amount} {self.name}' + ('s' if self.amount > 1 else '')
    
    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other):
        return isinstance(other, UncountableIngredient) and self.name == other.name and self.amount == other.amount
    
    def times(self, amount: int) -> List['UncountableIngredient']:
        '''Returns a list containing the given number of times the current amount of this uncountable Ingredient.

        Args:
            amount (int): the number of times to multiply this Ingredient.

        Returns:
            List[UncountableIngredient]: a list containing the given number of times the current amount of this uncountable Ingredient.
        '''
        
        return [copy(self) for i in range(amount)]

class Butter(UncountableIngredient):
    '''A pale yellow edible fatty substance made by churning cream and used as a spread or in cooking.'''

    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'Butter':
        '''Returns a given amount of Butter.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            Butter: the given amount of Butter.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('butter', amount)
    
    def __hash__(self):
        return super().__hash__()
    
class Egg(Ingredient):
    '''An oval object laid by a female bird, usually containing a developing embryo enclosed in a chalky shell.'''

    @staticmethod
    def take(amount: int = 1) -> Union['Egg', List['Egg']]:
        '''Returns a given number of Eggs.

        Args:
            amount (int): the amount of Eggs to take. Optional, defaults to 1.

        Returns:
            Egg: the given amount of Eggs.
        '''
        
        return Ingredient._take(__class__, amount)
    
    def __init__(self):
        self.name = 'egg'
        self.cracked = False

    def crack(self):
        '''Cracks the current egg.'''

        self.cracked = True
    
    def __str__(self):
        return ('cracked ' if self.cracked else '') + self.name
    
    def __eq__(self, other):
        return isinstance(other, Egg) and self.cracked == other.cracked
    
    def __hash__(self):
        return super().__hash__()

class Apple(Ingredient):
    '''The round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.'''
    
    @staticmethod
    def take(amount: int = 1) -> Union['Apple', List['Apple']]:
        '''Returns a given number of Apples.

        Args:
            amount (int): the amount of Apples to take. Optional, defaults to 1.

        Returns:
            Apple: the given amount of Apples.
        '''
        
        return Ingredient._take(__class__, amount)
    
    def __init__(self):
        self.name = 'apple'
        self.peeled = False
        self.sliced = False

    def peel(self):
        '''Peels the current Apple.

        Raises:
            KitchenException: when you try to peel a sliced Apple.
        '''
        
        if not self.peeled:
            if self.sliced:
                raise KitchenException('Can\'t peel a sliced fruit!')
            self.peeled = True
    
    def slice(self):
        '''Slices the current Apple.'''
        
        self.sliced = True
    
    def __str__(self):
        return ('sliced ' if self.sliced else '') + ('peeled ' if self.peeled else '') + self.name
    
    def __eq__(self, other):
        return isinstance(other, Apple) and self.sliced == other.sliced and self.peeled == other.peeled
    
    def __hash__(self):
        return super().__hash__()

class Lemon(Ingredient):
    '''A pale yellow oval citrus fruit with thick skin and fragrant, acidic juice.'''
    
    @staticmethod
    def take(amount: int = 1) -> Union['Lemon', List['Lemon']]:
        '''Returns a given number of Lemons.

        Args:
            amount (int): the amount of Lemons to take. Optional, defaults to 1.

        Returns:
            Lemon: the given amount of Lemons.
        '''

        return Ingredient._take(__class__, amount)
    
    def __init__(self):
        self.name = 'lemon'
        self.zested = False
        self.squeezed = False

    def zest(self) -> 'LemonZest':
        '''Zests the current Lemon, and returns the LemonZest.

        Returns:
            LemonZest: the LemonZest from the current Lemon.
        '''

        self.zested = True
        return LemonZest.take(grams=50)
    
    def squeeze(self) -> 'LemonJuice':
        '''Squeezes the current Lemon, and returns the LemonJuice.

        Returns:
            LemonJuice: the LemonJuice from the current Lemon.
        '''
        
        self.squeezed = True
        return LemonJuice.take(ml=200)
    
    def __str__(self):
        return ('squeezed ' if self.squeezed else '') + ('zested ' if self.zested else '') + self.name
    
    def __eq__(self, other):
        return isinstance(other, Lemon) and self.squeezed == other.squeezed and self.zested == other.zested
    
    def __hash__(self):
        return super().__hash__()

class LemonZest(UncountableIngredient):
    '''The outer part of the peel of a Lemon, used as flavouring.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'LemonZest':
        '''Returns a given amount of LemonZest.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            LemonZest: the given amount of LemonZest.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('lemon zest', amount)
    
    def __hash__(self):
        return super().__hash__()

class LemonJuice(UncountableIngredient):
    '''The liquid obtained from a Lemon.'''
    
    @staticmethod
    def take(amount: str = None, ml: int = None) -> 'LemonJuice':
        '''Returns a given amount of LemonJuice.

        Args:
            amount (str): the amount, specified as a string.
            ml (int): the amount, specified in number of millilitres.

        Returns:
            LemonJuice: the given amount of LemonJuice.
        '''

        return UncountableIngredient._take(__class__, 'ml', amount, ml)
    
    def __init__(self, amount: str):
        super().__init__('lemon juice', amount)
    
    def __hash__(self):
        return super().__hash__()

class Salt(UncountableIngredient):
    '''A white crystalline substance that gives seawater its characteristic taste and is used for seasoning or preserving food.'''
   
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'Salt':
        '''Returns a given amount of Salt.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            Salt: the given amount of Salt.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('salt', amount)
    
    def __hash__(self):
        return super().__hash__()

class Flour(UncountableIngredient):
    '''A powder obtained by grinding grain, typically wheat, and used to make bread, cakes, and pastry.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'Flour':
        '''Returns a given amount of Flour.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            Flour: the given amount of Flour.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('flour', amount)
    
    def __hash__(self):
        return super().__hash__()

class Sugar(UncountableIngredient):
    '''A sweet crystalline substance obtained from various plants, especially sugar cane and sugar beet, consisting essentially of sucrose.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'Sugar':
        '''Returns a given amount of Sugar.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            Sugar: the given amount of Sugar.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('sugar', amount)
    
    def __hash__(self):
        return super().__hash__()

class Cinnamon(UncountableIngredient):
    '''An aromatic spice made from the peeled, dried, and rolled bark of a south-east Asian tree.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'Cinnamon':
        '''Returns a given amount of Cinnamon.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            Cinnamon: the given amount of Cinnamon.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('cinnamon', amount)
    
    def __hash__(self):
        return super().__hash__()

class Cornstarch(UncountableIngredient):
    '''Finely ground maize flour, used as a thickener in cooking; cornflour.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'Cornstarch':
        '''Returns a given amount of Cornstarch.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            Cornstarch: the given amount of Cornstarch.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('cornstarch', amount)
    
    def __hash__(self):
        return super().__hash__()

class BakingPowder(UncountableIngredient):
    '''A mixture of sodium bicarbonate and cream of tartar, used instead of yeast in baking.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'BakingPowder':
        '''Returns a given amount of BakingPowder.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            BakingPowder: the given amount of BakingPowder.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('baking powder', amount)
    
    def __hash__(self):
        return super().__hash__()

class ChocolateChips(UncountableIngredient):
    '''Small pieces of chocolate used in biscuits, cakes, and ice cream.'''
    
    @staticmethod
    def take(amount: str = None, grams: int = None) -> 'ChocolateChips':
        '''Returns a given amount of ChocolateChips.

        Args:
            amount (str): the amount, specified as a string.
            grams (int): the amount, specified in number of grams.

        Returns:
            ChocolateChips: the given amount of ChocolateChips.
        '''

        return UncountableIngredient._take(__class__, 'g', amount, grams)
    
    def __init__(self, amount: str):
        super().__init__('chocolate chips', amount)
    
    def __hash__(self):
        return super().__hash__()

class Milk(UncountableIngredient):
    '''An opaque white fluid rich in fat and protein, secreted by female mammals for the nourishment of their young.'''
    
    @staticmethod
    def take(amount: str = None, ml: int = None) -> 'Milk':
        '''Returns a given amount of Milk.

        Args:
            amount (str): the amount, specified as a string.
            ml (int): the amount, specified in number of millilitres.

        Returns:
            Milk: the given amount of Milk.
        '''

        return UncountableIngredient._take(__class__, 'ml', amount, ml)
    
    def __init__(self, amount: str):
        super().__init__('milk', amount)
    
    def __hash__(self):
        return super().__hash__()

class Water(UncountableIngredient):
    '''A colourless, transparent, odourless liquid that forms the seas, lakes, rivers, and rain and is the basis of the fluids of living organisms.'''
    
    @staticmethod
    def take(amount: str = None, ml: int = None) -> 'Water':
        '''Returns a given amount of Water.

        Args:
            amount (str): the amount, specified as a string.
            ml (int): the amount, specified in number of millilitres.

        Returns:
            Water: the given amount of Water.
        '''

        return UncountableIngredient._take(__class__, 'ml', amount, ml)
    
    def __init__(self, amount: str):
        super().__init__('water', amount)
    
    def __hash__(self):
        return super().__hash__()
