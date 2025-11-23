using System;

// Violación del ISP: Interfaz ancha fuerza a las clases a implementar métodos que no usan
// ❌ Problema: Todos los trabajadores deben implementar todos los métodos, incluso si no los necesitan

public interface IWorker
{
  string Work();
  string Eat();
  string Sleep();
}

public class Human : IWorker
{
  public string Work()
  {
    return "Humano trabajando";
  }

  public string Eat()
  {
    return "Humano comiendo";
  }

  public string Sleep()
  {
    return "Humano durmiendo";
  }
}

public class Robot : IWorker
{
  public string Work()
  {
    return "Robot trabajando";
  }

  // ❌ Los robots no comen, pero están forzados a implementar esto
  public string Eat()
  {
    throw new Exception("¡Los robots no comen!");
  }

  // ❌ Los robots no duermen, pero están forzados a implementar esto
  public string Sleep()
  {
    throw new Exception("¡Los robots no duermen!");
  }
}

// Uso mostrando el problema
class Program
{
  static void Main()
  {
    var human = new Human();
    var robot = new Robot();

    Console.WriteLine(human.Work()); // ✅ Funciona
    Console.WriteLine(human.Eat()); // ✅ Funciona
    Console.WriteLine(human.Sleep()); // ✅ Funciona

    Console.WriteLine(robot.Work()); // ✅ Funciona
                                     // Console.WriteLine(robot.Eat());   // ❌ ¡Lanza error!
                                     // Console.WriteLine(robot.Sleep()); // ❌ ¡Lanza error!
  }
}
