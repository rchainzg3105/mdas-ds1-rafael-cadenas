package SOLID.isp;

// Violación del ISP: Interfaz ancha fuerza a las clases a implementar métodos que no usan
// Problema: Todos los trabajadores deben implementar todos los métodos, incluso si no los necesitan

public class IspBad {
    public static void main(String[] args) {
        Human human = new Human();
        Robot robot = new Robot();

        System.out.println(human.work()); // ✅ Funciona
        System.out.println(human.eat()); // ✅ Funciona
        System.out.println(human.sleep()); // ✅ Funciona

        System.out.println(robot.work()); // ✅ Funciona
        // System.out.println(robot.eat());   // ❌ ¡Lanza error!
        // System.out.println(robot.sleep()); // ❌ ¡Lanza error!
    }
}

interface Worker {
    String work();
    String eat();
    String sleep();
}

class Human implements Worker {
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

class Robot implements Worker {
    public String work() {
        return "Robot trabajando";
    }

    // ❌ Los robots no comen, pero están forzados a implementar esto
    public String eat() {
        throw new UnsupportedOperationException("¡Los robots no comen!");
    }

    // ❌ Los robots no duermen, pero están forzados a implementar esto
    public String sleep() {
        throw new UnsupportedOperationException("¡Los robots no duermen!");
    }
}
