""" BioDB First Project """

class Animal:
    """ Parent class of different animals """
    
    def __init__(self, name:str, year:int) -> None:
        """Initialises class Animal

        Parameters
        ----------
        name: str
            name of the animal
        year : int
            birthday of animal

        Returns
        -------
        None

        """
        self.name = name
        self.year = year

class Dog(Animal):
    def __init__(self, name: str, year: int) -> None:
        """Initialises class Dog and the super class Animal

        Parameters
        ----------
        name: str
            name of the dog
        year : int
            birthday of dog

        Returns
        -------
        None

        """
        super().__init__(name, year)
    
    def say_hello(self) -> None:
        """ Class method to say hello 

        Returns
        -------
        str
            sound of dog
        
        """
        return 'Woof Woof!!'

class Cat(Animal):
    def __init__(self, name: str, year: int) -> None:
        """Initialises class Cat and the super class Animal

        Parameters
        ----------
        name: str
            name of the cat
        year : int
            birthday of cat

        Returns
        -------
        None

        """
        super().__init__(name, year)
    
    def say_hello(self) -> None:
        """ Class method to say hello 

        Returns
        -------
        str
            sound of cat
        
        """
        return 'Meow!!'
    