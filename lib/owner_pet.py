class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Returns the list of pets owned by the owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner after checking if it's a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of the Pet class can be added.")
        if pet not in self._pets:  # Ensure the pet isn't added twice
            self._pets.append(pet)
        pet.owner = self  # Set the owner of the pet

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}.")
        self.pet_type = pet_type
        self.owner = None
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)  # Automatically add the pet to the owner's list
        Pet.all.append(self)
