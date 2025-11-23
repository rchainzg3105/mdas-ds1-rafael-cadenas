# Cumplimiento del ISP: Dividir interfaz ancha en interfaces más pequeñas y enfocadas
# Solución: Crear interfaces separadas para diferentes capacidades

from abc import ABC, abstractmethod


# Interfaces separadas para diferentes capacidades ✅
class Workable(ABC):
    @abstractmethod
    def work(self) -> str:
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass


class Sleepable(ABC):
    @abstractmethod
    def sleep(self) -> str:
        pass


# Human implementa todas las interfaces (necesita todas las capacidades) ✅
class Human(Workable, Eatable, Sleepable):
    def work(self) -> str:
        return "Humano trabajando"

    def eat(self) -> str:
        return "Humano comiendo"

    def sleep(self) -> str:
        return "Humano durmiendo"


# Robot solo implementa lo que necesita ✅
class Robot(Workable):
    def work(self) -> str:
        return "Robot trabajando"
    # ✅ ¡No necesita implementar eat() o sleep()!


# SuperHuman puede trabajar y tiene habilidades especiales
class SuperHuman(Workable, Sleepable):
    def work(self) -> str:
        return "SuperHumano trabajando a super velocidad"

    def sleep(self) -> str:
        return "SuperHumano durmiendo brevemente"
    # ✅ No necesita comer (obtiene energía del sol)


# Uso - ¡sin más implementaciones forzadas!
if __name__ == "__main__":
    human = Human()
    robot = Robot()
    super_human = SuperHuman()

    print(human.work())  # ✅ Funciona
    print(human.eat())  # ✅ Funciona
    print(human.sleep())  # ✅ Funciona

    print(robot.work())  # ✅ Funciona
    # robot.eat() - El método no existe (¡seguro en tiempo de compilación!)

    print(super_human.work())  # ✅ Funciona
    print(super_human.sleep())  # ✅ Funciona
