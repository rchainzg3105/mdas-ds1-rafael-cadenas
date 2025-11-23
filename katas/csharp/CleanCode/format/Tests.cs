using Xunit;

namespace CleanCode.Format.Tests
{
  /// <summary>
  /// Tests para el concepto de Format en Clean Code
  /// Valida tanto las implementaciones malas como las buenas
  /// </summary>
  public class FormatTests
  {
    [Fact]
    public void CalculatorBad_Add_TwoNumbers_ReturnsSum()
    {
      // Arrange
      var calc = new Calculator(); // De format-bad.cs

      // Act
      var result = calc.Add(5, 3);

      // Assert
      Assert.Equal(8, result);
    }

    [Fact]
    public void CalculatorBad_Subtract_TwoNumbers_ReturnsDifference()
    {
      // Arrange
      var calc = new Calculator();

      // Act
      var result = calc.Subtract(10, 4);

      // Assert
      Assert.Equal(6, result);
    }

    [Fact]
    public void CalculatorBad_Multiply_TwoNumbers_ReturnsProduct()
    {
      // Arrange
      var calc = new Calculator();

      // Act
      var result = calc.Multiply(6, 7);

      // Assert
      Assert.Equal(42, result);
    }

    [Fact]
    public void CalculatorBad_Divide_TwoNumbers_ReturnsQuotient()
    {
      // Arrange
      var calc = new Calculator();

      // Act
      var result = calc.Divide(15, 3);

      // Assert
      Assert.Equal(5, result);
    }

    [Fact]
    public void CalculatorBad_Divide_ByZero_ReturnsErrorMessage()
    {
      // Arrange
      var calc = new Calculator();

      // Act
      var result = calc.Divide(10, 0);

      // Assert
      Assert.Contains("Error", result.ToString());
    }

    [Fact]
    public void CalculatorGood_Add_NegativeNumbers_ReturnsCorrectSum()
    {
      // Arrange
      var calc = new Calculator(); // De format-good.cs

      // Act
      var result = calc.Add(-5, 3);

      // Assert
      Assert.Equal(-2, result);
    }

    [Fact]
    public void CalculatorGood_Multiply_ByZero_ReturnsZero()
    {
      // Arrange
      var calc = new Calculator();

      // Act
      var result = calc.Multiply(5, 0);

      // Assert
      Assert.Equal(0, result);
    }
  }
}

/*
INSTRUCCIONES PARA EJECUTAR LOS TESTS:

1. Navegar a la carpeta:
   cd katas/csharp/CleanCode/format

2. Crear proyecto de tests:
   dotnet new xunit -n FormatTests

3. Ejecutar tests:
   dotnet test

4. Ver detalles:
   dotnet test -v detailed
*/
