<?php
// Cumplimiento del ISP: Dividir interfaz ancha en interfaces más pequeñas y enfocadas
// Solución: Crear interfaces separadas para diferentes capacidades

// Interfaces separadas para diferentes capacidades ✅
interface Workable {
    public function work(): string;
}

interface Eatable {
    public function eat(): string;
}

interface Sleepable {
    public function sleep(): string;
}

// Human implementa todas las interfaces (necesita todas las capacidades) ✅
class Human implements Workable, Eatable, Sleepable {
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

// Robot solo implementa lo que necesita ✅
class Robot implements Workable {
    public function work(): string {
        return "Robot trabajando";
    }
    // ✅ ¡No necesita implementar eat() o sleep()!
}

// SuperHuman puede trabajar y tiene habilidades especiales
class SuperHuman implements Workable, Sleepable {
    public function work(): string {
        return "SuperHumano trabajando a super velocidad";
    }

    public function sleep(): string {
        return "SuperHumano durmiendo brevemente";
    }
    // ✅ No necesita comer (obtiene energía del sol)
}

// Uso - ¡sin más implementaciones forzadas!
$human = new Human();
$robot = new Robot();
$superHuman = new SuperHuman();

echo $human->work() . PHP_EOL; // ✅ Funciona
echo $human->eat() . PHP_EOL; // ✅ Funciona
echo $human->sleep() . PHP_EOL; // ✅ Funciona

echo $robot->work() . PHP_EOL; // ✅ Funciona
// $robot->eat() - El método no existe (¡seguro en tiempo de compilación!)

echo $superHuman->work() . PHP_EOL; // ✅ Funciona
echo $superHuman->sleep() . PHP_EOL; // ✅ Funciona
