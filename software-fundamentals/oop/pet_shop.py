from datetime import datetime


class Dog:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.__age = age

    def bark(self) -> None:
        if self.weight > 100:
            print("WOOF!")
        else:
            print("woof")

    def get_age(self) -> int:
        return self.__age

    # setter
    def set_age(self, new_age: int):
        if not isinstance(new_age, int):
            raise TypeError("Not a number, silly!")
        if new_age - self.__age != 1:
            raise ValueError("You are not a time traveling dog")
        self.__age = new_age

    def eat(self):
        """When this is called, print a message to the

        For this method - eating before 8am and after 7pm should raise an error.
        Write some tests to ensure this works correctly by creating new dates.
        """
        ...


class Cat:
    def __init__(self, name, age, weight):
        pass

    def eat(self):
        """When this is called, print a message to the

       For this method - eating before 8am and after 7pm should raise an error.
       Write some tests to ensure this works correctly by creating new dates.
       """
        ...


class Hamster:
    def __init__(self, name, age, weight):
        pass

    def eat(self):
        """When this is called, print a message to the

       For this method - eating before 8am and after 7pm should raise an error.
       Write some tests to ensure this works correctly by creating new dates.
       """
        ...


class PetStore:
    def __init__(self, animal_list: list[Dog]):
        if len(animal_list) > 9:
            raise ValueError("Too cute, to much! Can't handle it!")

        self.__animal_list = animal_list  # private variables __
        # Python renames __animal_list to something else

    def add_pet(self, pet: Dog) -> None:
        """accepts all Cats, and Hamsters under 0.5 years old."""
        if not isinstance(pet, Dog):
            raise TypeError("That 'aint no dog!")

        if len(self.__animal_list) < 10:
            self.__animal_list.append(pet)

        else:
            raise ValueError("Pet store full! Go away!")

    def pets_for_sale(self) -> list[Dog]:  # getter
        print("Here is our selection of dogs:")
        return [dog.name for dog in self.__animal_list]

    def pets_larger_than(self, weight: int) -> list[Dog]:
        dog_list = []
        for dog in self.__animal_list:
            if dog.weight > weight:
                dog_list.append(dog)
        return dog_list

    def get_cats(self):
        ...

    def get_hamsters(self):
        ...

    def get_dogs(self):
        ...


fluffy = Dog("Fluffy", 10, 12)

print(fluffy.get_age())

fluffy.set_age(13)

print(fluffy.get_age())

store = PetStore([fluffy])

print(store.pets_for_sale())

