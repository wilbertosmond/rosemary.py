from kitchen.Kitchen import KitchenObject, KitchenException

class Rosemary:
    @staticmethod
    def _print(action, kitchen_object):
        if isinstance(kitchen_object, KitchenObject):
            print(f'Rosemary {action}s {kitchen_object}')
        else:
            raise KitchenException(f'Rosemary can\'t {action} that!')
    
    @staticmethod
    def taste(kitchen_object: KitchenObject):
        '''Rosemary tastes the given KitchenObject, and prints her findings into the terminal.

        Args:
            kitchen_object (KitchenObject): the KitchenObject for Rosemary to taste.
        '''

        Rosemary._print('taste', kitchen_object)
    
    @staticmethod
    def serve(kitchen_object: KitchenObject):
        '''Rosemary serves the given KitchenObject, and prints the result into the terminal.

        Args:
            kitchen_object (KitchenObject): the KitchenObject for Rosemary to serve.
        '''

        Rosemary._print('serve', kitchen_object)
        exit()
