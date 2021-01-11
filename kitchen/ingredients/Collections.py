from fractions import Fraction
from typing import Union
from kitchen.Kitchen import KitchenException
from kitchen.ingredients.Ingredient import Ingredient

class Portion(Ingredient):
    '''A Portion of a Mixture of Ingredients, usually the product of mixing Ingredients in a Bowl.'''
    
    def __init__(self, ingredient: 'Mixture', portion: Union[Fraction, int] = 1):
        self.contents = ingredient
        self.portion = Fraction(portion)
    
    def _take(self, portion: str) -> 'Portion':
        portion_unit = Fraction(portion)
        if portion_unit > self.portion:
            raise KitchenException('Not enough left!')
        self.portion -= portion_unit
        return Portion(self.contents, portion_unit)
    
    def __str__(self):
        return (f'{self.portion} portion of ' if self.portion < 1 else '') + str(self.contents) if self.portion > 0 else 'nothing'
    
    def __eq__(self, other):
        return isinstance(other, Portion) and other.contents == self.contents and other.portion == self.portion
    
    def __hash__(self):
        return super().__hash__()

class Collection(Ingredient):
    '''A Collection of Ingredients.'''
    
    def __init__(self, name: str = None):
        self.contents = {}
        self.name = name

    def _add(self, item: Ingredient):
        if isinstance(item, Ingredient):
            if item == self:
                raise KitchenException('Cannot add something to itself')
            if item in self.contents:
                self.contents[item] += 1
            else:
                self.contents[item] = 1
        else:
            raise KitchenException('Can only add edible things')
    
    def __str__(self):
        return (f'"{self.name}", containing ' if self.name is not None else '') \
            + ('(' if len(self.contents) > 1 else '') \
            + (', '.join((f'{amount}x {content}' if amount > 1 else str(content)) for content, amount in self.contents.items())
                if len(self.contents) > 0 else 'nothing') \
            + (')' if len(self.contents) > 1 else '')
    
    def __eq__(self, other):
        return isinstance(other, Collection) and other.contents == self.contents and other.name == self.name
    
    def __hash__(self):
        return super().__hash__()

class Stack(Collection):
    '''A Stack of Ingredients.'''
    
    def __str__(self):
        return 'stacked ' + super().__str__() if len(self.contents) > 1 else super().__str__()
    
    def __hash__(self):
        return super().__hash__()

class Mixture(Collection):
    '''A Mixture of Ingredients.'''
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self.mixed = False

    def _mix(self):
        self.mixed = True

    def __str__(self):
        return ('mixed ' if self.mixed else ('unmixed ' if len(self.contents) > 1 else '')) + super().__str__()
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, Mixture) and self.mixed == other.mixed
    
    def __hash__(self):
        return super().__hash__()

class CookedCollection(Collection):
    '''A cooked Collection of Ingredients.'''
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self.cooked = [0., 0.]
        self.side = 0

    def _cook(self, minutes: float = 1):
        self.cooked[self.side] += minutes

    def _flip(self):
        self.side = (self.side + 1) % 2

    def __str__(self):
        return f'cooked (for {self.cooked[0]}/{self.cooked[1]} minutes) ' + super().__str__()
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, CookedCollection) and self.cooked == other.cooked
    
    def __hash__(self):
        return super().__hash__()

class TemperatureCollection(Collection):
    '''A Collection of Ingredients that has been prepared by keeping at a (high or low) temperature.'''
    
    def __init__(self, name: str = None, temperature: int = 20):
        super().__init__(name)
        self.temperature = temperature
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, TemperatureCollection) and self.temperature == other.temperature
    
    def __hash__(self):
        return super().__hash__()

class ChilledCollection(TemperatureCollection):
    '''A chilled Collection of Ingredients.'''
    
    def __init__(self, temperature: int = 5):
        super().__init__(None, temperature=temperature)

    def __str__(self):
        return f'chilled (to {self.temperature} degrees) ' + super().__str__()
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, ChilledCollection) and self.temperature == other.temperature
    
    def __hash__(self):
        return super().__hash__()

class BakedCollection(TemperatureCollection):
    '''A baked Collection of Ingredients.'''
    
    def __init__(self, name: str = None):
        super().__init__(name)
        self.baked = 0

    def _bake(self, minutes: float = 1):
        self.baked += minutes

    def __str__(self):
        return ('unbaked ' if self.baked == 0 else f'baked (at {self.temperature} degrees for {self.baked} minutes) ') + super().__str__()
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, BakedCollection) and self.baked == other.baked and self.temperature == other.temperature
    
    def __hash__(self):
        return super().__hash__()

class PieCollection(BakedCollection):
    '''A baked Collection of Ingredients in the shape of a pie.'''
    
    def __init__(self, name: str = None):
        super().__init__(name)

    def __str__(self):
        return 'pie of ' + super().__str__()
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, PieCollection)
    
    def __hash__(self):
        return super().__hash__()
