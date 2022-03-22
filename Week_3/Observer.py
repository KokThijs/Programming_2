'''
Contains class to implement observer pattern
'''

class Observer():
    '''
    class containing observer methods
    '''
    def update(self, other):
        raise NotImplementedError('should be implemented in the subclasses')

