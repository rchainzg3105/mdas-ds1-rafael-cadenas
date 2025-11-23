using System;
using System.Collections.Generic;

// Violación de Clean Code: Mal Nombrado
// ❌ Problemas: Nombres sin intención, información falsa, difícil pronunciar, codificaciones

class Program
{
  static void Main()
  {
    // ❌ Sin intención clara
    int d; // ¿Qué es 'd'?
    string x; // ¿Qué es 'x'?
    int[] arr = { 1, 2, 3 }; // ¿Array de qué?

    // ❌ Información falsa
    HashSet<string> userList = new HashSet<string>(); // ¡No es una List, es un HashSet!
    Dictionary<string, int> accountsArray = new Dictionary<string, int>(); // ¡No es un array!

    // ❌ Difícil de pronunciar
    string yyyymmdstr = "20251102"; // ¿Cómo pronuncias esto?
    DateTime genymdhms = DateTime.Now; // ¿Gen-y-m-d-h-m-s?

    // ❌ Codificaciones innecesarias (notación húngara)
    string strFirstName = "John"; // El 'str' es redundante en C#
    int intAge = 25; // El 'int' es redundante
    bool boolIsActive = true; // El 'bool' es redundante

    // ❌ Números y strings mágicos
    var service = new UserService();
    var user = new { age = 20, status = "ACT", points = 1200 };

    Console.WriteLine("=== Violación de Nombrado en Clean Code ===");

    d = 86400; // ¿Segundos? ¿Milisegundos? ¿Días?
    x = "usuario@email.com";

    Console.WriteLine($"Usuario válido: {service.ValidateUser(user.age, user.status, user.points)}");
    Console.WriteLine($"Descuento: {service.CalculateDiscount(100, "VIP")}");
  }
}

class UserService
{
  public bool ValidateUser(int age, string status, int points)
  {
    if (age < 18) // ❌ ¿Qué significa 18?
    {
      return false;
    }

    if (status == "ACT") // ❌ ¿Qué significa "ACT"?
    {
      return true;
    }

    if (points > 1000) // ❌ ¿Por qué 1000?
    {
      return true;
    }

    return false;
  }

  public double CalculateDiscount(double total, string type)
  {
    if (type == "VIP")
    {
      return total * 0.2; // ❌ ¿Qué significa 0.2?
    }
    else if (type == "REG")
    {
      return total * 0.05; // ❌ ¿Qué significa 0.05?
    }
    return 0;
  }
}
