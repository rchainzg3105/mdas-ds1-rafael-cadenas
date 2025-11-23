# Violación del ISP: Interfaz ancha fuerza a las clases a implementar métodos que no usan
# Problema: Todos los trabajadores deben implementar todos los métodos, incluso si no los necesitan

from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def eat(self) -> str:
        pass

    @abstractmethod
    def sleep(self) -> str:
        pass


class Human(Worker):
    def work(self) -> str:
        return "Humano trabajando"

    def eat(self) -> str:
        return "Humano comiendo"

    def sleep(self) -> str:
        return "Humano durmiendo"


class Robot(Worker):
    def work(self) -> str:
        return "Robot trabajando"

    # ❌ Los robots no comen, pero están forzados a implementar esto
    def eat(self) -> str:
        raise Exception("¡Los robots no comen!")

    # ❌ Los robots no duermen, pero están forzados a implementar esto
    def sleep(self) -> str:
        raise Exception("¡Los robots no duermen!")


# Uso mostrando el problema
if __name__ == "__main__":
    human = Human()
    robot = Robot()

    print(human.work())  # ✅ Funciona
    print(human.eat())  # ✅ Funciona
    print(human.sleep())  # ✅ Funciona

    print(robot.work())  # ✅ Funciona
    # print(robot.eat())   # ❌ ¡Lanza error!
    # print(robot.sleep()) # ❌ ¡Lanza error!
