using Xunit;

namespace CleanCode.Functions.Tests
{
  /// <summary>
  /// Tests para el concepto de Functions en Clean Code
  /// Valida tanto las implementaciones malas como las buenas
  /// </summary>
  public class FunctionsTests
  {
    [Fact]
    public void OrderProcessorBad_ProcessOrder_ValidOrder_ProcessesSuccessfully()
    {
      // Arrange
      var processor = new OrderProcessor(); // De functions-bad.cs
      var items = new[] { new { name = "Product", price = 100.0, qty = 2 } };

      // Act
      var result = processor.ProcessOrder(1, "John Doe", "john@email.com", items);

      // Assert
      Assert.Contains("Pedido procesado", result);
      Assert.Contains("Total: 200", result);
    }

    [Fact]
    public void OrderProcessorBad_ProcessOrder_InvalidCustomer_ReturnsError()
    {
      // Arrange
      var processor = new OrderProcessor();
      var items = new[] { new { name = "Product", price = 100.0, qty = 2 } };

      // Act
      var result = processor.ProcessOrder(0, "", "", items);

      // Assert
      Assert.Contains("Error", result);
    }

    [Fact]
    public void OrderProcessorBad_ProcessOrder_EmptyItems_ReturnsError()
    {
      // Arrange
      var processor = new OrderProcessor();
      var items = new object[] { };

      // Act
      var result = processor.ProcessOrder(1, "John Doe", "john@email.com", items);

      // Assert
      Assert.Contains("Error", result);
    }
  }
}

/*
INSTRUCCIONES PARA EJECUTAR LOS TESTS:

1. Navegar a la carpeta del concepto:
   cd katas/csharp/CleanCode/functions

2. Crear un proyecto de tests xUnit (si no existe):
   dotnet new xunit -n FunctionsTests

3. Agregar referencias a los archivos fuente

4. Ejecutar los tests:
   dotnet test

5. Ver resultados detallados:
   dotnet test --logger "console;verbosity=detailed"
*/
