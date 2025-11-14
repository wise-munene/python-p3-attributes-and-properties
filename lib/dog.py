APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=""):
        # Only validate if name is explicitly passed
        if name is not None:
            self.name = name
        else:
            self._name = ""  # silent default
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value == "":
            self._breed = value
            return
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None
