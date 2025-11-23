using System;

// Violación de Clean Code: Funciones Mal Diseñadas
// ❌ Problemas: Hacen muchas cosas, grandes, niveles de abstracción mezclados, efectos secundarios

public class User
{
  public string Name { get; set; }
  public int Score { get; set; }
}

public class UserScoreProcessor
{
  // ❌ Función hace MUCHAS cosas: calcula bonus, actualiza score, envía notificación y loguea
  // ❌ Niveles de abstracción mezclados
  public void ProcessUserScore(User user, int newScore, int timeInSeconds)
  {
    Console.WriteLine($"Procesando puntaje para {user.Name}...");

    // Nivel bajo: cálculo de bonus
    int bonus = 0;
    if (timeInSeconds < 60)
    {
      bonus = 10;
      Console.WriteLine($"Aplica bonus de {bonus} puntos por tiempo rápido.");
    }

    int finalScore = user.Score + newScore + bonus;

    // Nivel medio: actualizar el score del usuario (efecto secundario)
    user.Score = finalScore;

    // Nivel bajo: enviar notificación
    Console.WriteLine($"Notificación enviada a {user.Name}: Tu nuevo puntaje es {finalScore}");

    // Nivel bajo: guardar en log
    Console.WriteLine($"LOG: {user.Name} obtuvo {newScore} puntos. Puntaje final: {finalScore}");
  }
}

// Uso
class Program
{
  static void Main()
  {
    Console.WriteLine("=== Violación de Funciones en Clean Code ===");
    var user = new User { Name = "Alex", Score = 100 };
    var processor = new UserScoreProcessor();
    processor.ProcessUserScore(user, 50, 30);
    Console.WriteLine($"Puntaje final del usuario: {user.Score}");
  }
}
