# Cumplimiento del LSP: Jerarquía de herencia apropiada que no rompe expectativas
# ✅ Solución: Usar abstracciones apropiadas que coincidan con el comportamiento del mundo real

from abc import ABC, abstractmethod


# Clase base para comportamiento común ✅
class Animal(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass


# Interfaces separadas para diferentes capacidades ✅
class Flyable(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self) -> str:
        pass


# Aves que SÍ pueden volar ✅
class Eagle(Animal, Flyable):
    def eat(self) -> str:
        return "Águila comiendo pescado"

    def make_sound(self) -> str:
        return "Águila: ¡Graznido!"

    def fly(self) -> str:
        return "¡Águila volando alto!"


# Aves que NO pueden volar pero pueden nadar ✅
class Penguin(Animal, Swimmable):
    def eat(self) -> str:
        return "Pingüino comiendo pescado"

    def make_sound(self) -> str:
        return "Pingüino: ¡Graznido!"

    def swim(self) -> str:
        return "Pingüino nadando con gracia"


# Aves que pueden hacer ambas cosas ✅
class Duck(Animal, Flyable, Swimmable):
    def eat(self) -> str:
        return "Pato comiendo semillas"

    def make_sound(self) -> str:
        return "Pato: ¡Cuac!"

    def fly(self) -> str:
        return "Pato volando al estanque"

    def swim(self) -> str:
        return "Pato chapoteando en el agua"


# Funciones que funcionan con contratos apropiados ✅
def feed_animal(animal: Animal) -> str:
    return animal.eat()  # ✅ TODOS los animales pueden comer


def make_flyable_creature_fly(creature: Flyable) -> str:
    return creature.fly()  # ✅ Solo cosas que SÍ pueden volar


def make_swimmable_creature_swim(creature: Swimmable) -> str:
    return creature.swim()  # ✅ Solo cosas que SÍ pueden nadar


# Probando - ¡sin fallos! ✅
if __name__ == "__main__":
    print("=== Pruebas de Animales con LSP ===")

    eagle = Eagle()
    penguin = Penguin()
    duck = Duck()

    # Todos los animales pueden ser tratados de la misma manera ✅
    print("Alimentando:", feed_animal(eagle))
    print("Alimentando:", feed_animal(penguin))
    print("Alimentando:", feed_animal(duck))

    # Solo a las criaturas voladoras se les pide volar ✅
    print("Volando:", make_flyable_creature_fly(eagle))
    print("Volando:", make_flyable_creature_fly(duck))
    # ¡penguin no se le pide volar - seguro en tiempo de compilación!

    # Solo a las criaturas nadadoras se les pide nadar ✅
    print("Nadando:", make_swimmable_creature_swim(penguin))
    print("Nadando:", make_swimmable_creature_swim(duck))
    # ¡eagle no se le pide nadar - seguro en tiempo de compilación!
