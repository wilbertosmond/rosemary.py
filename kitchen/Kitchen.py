class KitchenException(Exception):
    '''An Exception raised in Rosemary's Kitchen when things go very, very wrong.'''
    
    def __init__(self, message: str, *args, **kwargs):
        Exception.__init__(self, 'The kitchen exploded!! '.upper() + message, *args, **kwargs)

class KitchenObject:
    '''An object is Rosemary's Kitchen, such as an Ingredient or Utensil.'''
    
    def __repr__(self):
        return str(self)
