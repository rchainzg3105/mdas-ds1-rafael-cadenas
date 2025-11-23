# Cumplimiento de Herencia: Reutilización mediante clase base
# ✅ Solución: Código común en clase padre, específico en hijos

from typing import List


# ✅ Clase base con comportamiento común
class Animal:
    # ✅ Propiedades comunes protegidas (accesibles en hijos)
    def __init__(self, name: str, age: int, weight: float):
        self._name = name
        self._age = age
        self._weight = weight

    # ✅ Métodos comunes definidos una sola vez
    def eat(self) -> None:
        print(f"{self._name} está comiendo")
        self._weight += 0.5

    def sleep(self) -> None:
        print(f"{self._name} está durmiendo")

    def get_info(self) -> str:
        return f"Nombre: {self._name}, Edad: {self._age} años, Peso: {self._weight}kg"

    # ✅ Método para que cada hijo implemente su sonido
    def make_sound(self) -> None:
        print(f"{self._name} hace un sonido")


# ✅ Dog hereda de Animal - sin duplicación
class Dog(Animal):
    # ✅ Solo comportamiento específico de perros
    def make_sound(self) -> None:
        print(f"{self._name} dice: ¡Guau guau!")

    def fetch(self) -> None:
        print(f"{self._name} está trayendo la pelota")


# ✅ Cat hereda de Animal - sin duplicación
class Cat(Animal):
    # ✅ Solo comportamiento específico de gatos
    def make_sound(self) -> None:
        print(f"{self._name} dice: ¡Miau miau!")

    def purr(self) -> None:
        print(f"{self._name} está ronroneando")


# ✅ Bird hereda de Animal - sin duplicación
class Bird(Animal):
    # ✅ Solo comportamiento específico de pájaros
    def make_sound(self) -> None:
        print(f"{self._name} dice: ¡Pío pío!")

    def fly(self) -> None:
        print(f"{self._name} está volando")


if __name__ == "__main__":
    # ✅ Código reutilizado y fácil de mantener
    print("=== Cumplimiento de Herencia ===")

    dog = Dog("Rex", 5, 25)
    cat = Cat("Luna", 3, 4)
    bird = Bird("Piolín", 1, 0.5)

    # ✅ Métodos heredados funcionan igual
    print(dog.get_info())
    dog.eat()
    dog.make_sound()
    dog.fetch()

    print(cat.get_info())
    cat.eat()
    cat.make_sound()
    cat.purr()

    print(bird.get_info())
    bird.eat()
    bird.make_sound()
    bird.fly()

    # ✅ Si necesito cambiar eat() o sleep(), cambio una sola vez en Animal
    # ✅ Nuevos animales heredan automáticamente el comportamiento común
    # ✅ Consistencia garantizada

    # ✅ Bonus: Puedo trabajar con tipo Animal
    animals: List[Animal] = [dog, cat, bird]
    print("\n=== Todos los animales ===")
    for animal in animals:
        animal.eat()  # ✅ Funciona para todos
        animal.make_sound()  # ✅ Cada uno con su sonido específico
