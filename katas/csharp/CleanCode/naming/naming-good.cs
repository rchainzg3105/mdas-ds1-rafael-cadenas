using System;
using System.Collections.Generic;

// Cumplimiento de Clean Code: Buen Nombrado
// ✅ Solución: Nombres con intención, sin información falsa, pronunciables, sin codificaciones

class Program
{
  static void Main()
  {
    // ✅ Nombres con intención clara
    int secondsInDay;
    string userEmailAddress;
    int[] productPrices = { 1, 2, 3 };

    // ✅ Sin información falsa
    HashSet<string> activeUsers = new HashSet<string>(); // Correcto: es un HashSet
    Dictionary<string, int> userAccount = new Dictionary<string, int>(); // Correcto: es un Dictionary

    // ✅ Pronunciables
    string currentDateString = "20251102";
    DateTime generatedTimestamp = DateTime.Now;

    // ✅ Sin codificaciones innecesarias
    string firstName = "John"; // C# ya sabe que es string
    int age = 25; // C# ya sabe que es int
    bool isActive = true; // C# ya sabe que es bool

    // ✅ Uso correcto con constantes
    var userService = new UserService();
    var validUser = new User { Age = 20, Status = "ACT", Points = 1200 };

    Console.WriteLine("=== Cumplimiento de Nombrado en Clean Code ===");

    secondsInDay = 86400; // ✅ Claro: segundos en un día
    userEmailAddress = "usuario@email.com"; // ✅ Claro: dirección de email del usuario

    Console.WriteLine($"Usuario válido: {userService.ValidateUser(validUser)}");
    Console.WriteLine($"Descuento: {userService.CalculateDiscount(100, "VIP")}");
  }
}

class UserService
{
  // Constantes descriptivas
  private const int MINIMUM_AGE = 18;
  private const string ACTIVE_STATUS = "ACT";
  private const int PREMIUM_POINTS_THRESHOLD = 1000;

  private const string VIP_CUSTOMER_TYPE = "VIP";
  private const string REGULAR_CUSTOMER_TYPE = "REG";

  private const double VIP_DISCOUNT_RATE = 0.2;
  private const double REGULAR_DISCOUNT_RATE = 0.05;

  public bool ValidateUser(User user)
  {
    if (user.Age < MINIMUM_AGE) // ✅ Claro: edad mínima requerida
    {
      return false;
    }

    if (user.Status == ACTIVE_STATUS) // ✅ Claro: estado activo
    {
      return true;
    }

    if (user.Points > PREMIUM_POINTS_THRESHOLD) // ✅ Claro: umbral de puntos premium
    {
      return true;
    }

    return false;
  }

  public double CalculateDiscount(double totalAmount, string customerType)
  {
    if (customerType == VIP_CUSTOMER_TYPE)
    {
      return totalAmount * VIP_DISCOUNT_RATE; // ✅ Claro: tasa de descuento VIP
    }
    else if (customerType == REGULAR_CUSTOMER_TYPE)
    {
      return totalAmount * REGULAR_DISCOUNT_RATE; // ✅ Claro: tasa de descuento regular
    }
    return 0;
  }
}

// ✅ Clase con propiedades descriptivas
class User
{
  public int Age { get; set; }
  public string Status { get; set; }
  public int Points { get; set; }
}
