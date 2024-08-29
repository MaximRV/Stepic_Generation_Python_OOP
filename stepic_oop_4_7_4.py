class Pet:
    pet_list = []

    def __init__(self, name):
        self.name = name
        Pet.pet_list.append(self)

    @classmethod
    def first_pet(cls):
        if Pet.pet_list:
            return Pet.pet_list[0]

    @classmethod
    def last_pet(cls):
        if Pet.pet_list:
            return Pet.pet_list[-1]


    @classmethod
    def num_of_pets(cls):
        return len(Pet.pet_list)


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
