package SOLID.isp;

// Cumplimiento del ISP: Dividir interfaz ancha en interfaces más pequeñas y enfocadas
// Solución: Crear interfaces separadas para diferentes capacidades

public class IspGood {
    public static void main(String[] args) {
        Human human = new Human();
        Robot robot = new Robot();
        SuperHuman superHuman = new SuperHuman();

        System.out.println(human.work()); // ✅ Funciona
        System.out.println(human.eat()); // ✅ Funciona
        System.out.println(human.sleep()); // ✅ Funciona

        System.out.println(robot.work()); // ✅ Funciona
        // robot.eat() - El método no existe (¡seguro en tiempo de compilación!)

        System.out.println(superHuman.work()); // ✅ Funciona
        System.out.println(superHuman.sleep()); // ✅ Funciona
    }
}

// Interfaces separadas para diferentes capacidades ✅
interface Workable {
    String work();
}

interface Eatable {
    String eat();
}

interface Sleepable {
    String sleep();
}

// Human implementa todas las interfaces (necesita todas las capacidades) ✅
class Human implements Workable, Eatable, Sleepable {
    public String work() {
        return "Humano trabajando";
    }

    public String eat() {
        return "Humano comiendo";
    }

    public String sleep() {
        return "Humano durmiendo";
    }
}

// Robot solo implementa lo que necesita ✅
class Robot implements Workable {
    public String work() {
        return "Robot trabajando";
    }
    // ✅ ¡No necesita implementar eat() o sleep()!
}

// SuperHuman puede trabajar y tiene habilidades especiales
class SuperHuman implements Workable, Sleepable {
    public String work() {
        return "SuperHumano trabajando a super velocidad";
    }

    public String sleep() {
        return "SuperHumano durmiendo brevemente";
    }
    // ✅ No necesita comer (obtiene energía del sol)
}
