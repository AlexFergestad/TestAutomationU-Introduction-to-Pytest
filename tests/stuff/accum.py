class Accumulator : 

    def __init__(self) -> None:
        self._count = 0
    
    # controls how callers can get and set values
    # a caller can get the value of count but can't set it
    @property
    def count(self):
        return self._count
    
    # Only way to internally change the count down
    # Accepts an amount to add as an input
    # adds the amount to the internal account
    def add(self, more=1):
        self._count += more


