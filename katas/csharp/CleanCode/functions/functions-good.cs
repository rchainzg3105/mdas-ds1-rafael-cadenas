using System;

// Cumplimiento de Clean Code: Funciones Bien Diseñadas
// ✅ Solución: Una cosa por función, pequeñas, mismo nivel de abstracción, sin efectos secundarios

public class User
{
  public string Name { get; set; }
  public int Score { get; set; }
}

public class UserScoreProcessor
{
  private const int FAST_TIME_BONUS = 10;
  private const int FAST_TIME_THRESHOLD_SECONDS = 60;

  // ✅ Función hace UNA cosa: orquestar el procesamiento del puntaje
  // ✅ Mismo nivel de abstracción
  public void ProcessUserScore(User user, int newScore, int timeInSeconds)
  {
    int bonus = CalculateBonus(timeInSeconds);
    int finalScore = user.Score + newScore + bonus;

    UpdateScore(user, finalScore);
    SendNotification(user);
    LogActivity(user, newScore);
  }

  // ✅ Función pequeña que hace UNA cosa: calcular bonus
  private int CalculateBonus(int timeInSeconds)
  {
    if (timeInSeconds < FAST_TIME_THRESHOLD_SECONDS)
    {
      Console.WriteLine($"Aplica bonus de {FAST_TIME_BONUS} puntos por tiempo rápido.");
      return FAST_TIME_BONUS;
    }
    return 0;
  }

  // ✅ Función pequeña que hace UNA cosa: actualizar puntaje
  private void UpdateScore(User user, int finalScore)
  {
    user.Score = finalScore;
  }

  // ✅ Función pequeña que hace UNA cosa: enviar notificación
  private void SendNotification(User user)
  {
    Console.WriteLine($"Notificación enviada a {user.Name}: Tu nuevo puntaje es {user.Score}");
  }

  // ✅ Función pequeña que hace UNA cosa: registrar actividad
  private void LogActivity(User user, int newScore)
  {
    Console.WriteLine($"LOG: {user.Name} obtuvo {newScore} puntos. Puntaje final: {user.Score}");
  }
}

// Uso
class Program
{
  static void Main()
  {
    Console.WriteLine("=== Cumplimiento de Funciones en Clean Code ===");
    var user = new User { Name = "Alex", Score = 100 };
    var processor = new UserScoreProcessor();
    processor.ProcessUserScore(user, 50, 30);
    Console.WriteLine($"Puntaje final del usuario: {user.Score}");
  }
}
