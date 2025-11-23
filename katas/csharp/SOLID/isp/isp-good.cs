using System;

// Cumplimiento del ISP: Dividir interfaz ancha en interfaces más pequeñas y enfocadas
// ✅ Solución: Crear interfaces separadas para diferentes capacidades

// Interfaces separadas para diferentes capacidades ✅
public interface IWorkable
{
  string Work();
}

public interface IEatable
{
  string Eat();
}

public interface ISleepable
{
  string Sleep();
}

// Human implementa todas las interfaces (necesita todas las capacidades) ✅
public class Human : IWorkable, IEatable, ISleepable
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

// Robot solo implementa lo que necesita ✅
public class Robot : IWorkable
{
  public string Work()
  {
    return "Robot trabajando";
  }
  // ✅ ¡No necesita implementar Eat() o Sleep()!
}

// SuperHuman puede trabajar y tiene habilidades especiales
public class SuperHuman : IWorkable, ISleepable
{
  public string Work()
  {
    return "SuperHumano trabajando a super velocidad";
  }

  public string Sleep()
  {
    return "SuperHumano durmiendo brevemente";
  }
  // ✅ No necesita comer (obtiene energía del sol)
}

// Uso - ¡sin más implementaciones forzadas!
class Program
{
  static void Main()
  {
    var human = new Human();
    var robot = new Robot();
    var superHuman = new SuperHuman();

    Console.WriteLine(human.Work()); // ✅ Funciona
    Console.WriteLine(human.Eat()); // ✅ Funciona
    Console.WriteLine(human.Sleep()); // ✅ Funciona

    Console.WriteLine(robot.Work()); // ✅ Funciona
                                     // robot.Eat() - El método no existe (¡seguro en tiempo de compilación!)

    Console.WriteLine(superHuman.Work()); // ✅ Funciona
    Console.WriteLine(superHuman.Sleep()); // ✅ Funciona
  }
}
