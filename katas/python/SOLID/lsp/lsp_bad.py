# Violación del LSP: Las clases derivadas rompen las expectativas de la clase padre
# ❌ Problema: FlyingBird asume que TODOS los pájaros pueden volar


class Bird:
    def fly(self) -> str:
        return "¡Volando alto en el cielo!"

    def eat(self) -> str:
        return "Comiendo deliciosa comida"


# ❌ Problema: Penguin ES-UN Bird, ¡pero no puede volar!
class Penguin(Bird):
    def fly(self) -> str:
        # ❌ Esto viola LSP - rompe la expectativa del padre
        # ¡Comportamiento roto!
        raise Exception("¡Los pingüinos no pueden volar!")

    def swim(self) -> str:
        return "Nadando con gracia"


class Eagle(Bird):
    def fly(self) -> str:
        return "¡Volando como un águila!"


# Esta función espera que TODOS los pájaros vuelen ❌
def make_bird_fly(bird: Bird) -> str:
    return bird.fly()  # ¡Esto lanzará un error para Penguin!


# Probando la violación
if __name__ == "__main__":
    print("=== Demostración de Violación LSP ===")

    eagle = Eagle()
    penguin = Penguin()

    print("Águila:", make_bird_fly(eagle))  # ✅ Funciona bien

    try:
        print("Pingüino:", make_bird_fly(penguin))  # ❌ ¡SE ROMPE!
    except Exception as error:
        print("ERROR:", str(error))
