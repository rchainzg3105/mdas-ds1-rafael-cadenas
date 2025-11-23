<?php
// Violación del ISP: Interfaz ancha fuerza a las clases a implementar métodos que no usan
// Problema: Todos los trabajadores deben implementar todos los métodos, incluso si no los necesitan

interface Worker {
    public function work(): string;
    public function eat(): string;
    public function sleep(): string;
}

class Human implements Worker {
    public function work(): string {
        return "Humano trabajando";
    }

    public function eat(): string {
        return "Humano comiendo";
    }

    public function sleep(): string {
        return "Humano durmiendo";
    }
}

class Robot implements Worker {
    public function work(): string {
        return "Robot trabajando";
    }

    // ❌ Los robots no comen, pero están forzados a implementar esto
    public function eat(): string {
        throw new Exception("¡Los robots no comen!");
    }

    // ❌ Los robots no duermen, pero están forzados a implementar esto
    public function sleep(): string {
        throw new Exception("¡Los robots no duermen!");
    }
}

// Uso mostrando el problema
$human = new Human();
$robot = new Robot();

echo $human->work() . PHP_EOL; // ✅ Funciona
echo $human->eat() . PHP_EOL; // ✅ Funciona
echo $human->sleep() . PHP_EOL; // ✅ Funciona

echo $robot->work() . PHP_EOL; // ✅ Funciona
// echo $robot->eat() . PHP_EOL;   // ❌ ¡Lanza error!
// echo $robot->sleep() . PHP_EOL; // ❌ ¡Lanza error!
