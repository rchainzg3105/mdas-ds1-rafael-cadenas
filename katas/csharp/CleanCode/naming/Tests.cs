using Xunit;

namespace CleanCode.Naming.Tests
{
  /// <summary>
  /// Tests para el concepto de Naming en Clean Code
  /// Valida tanto las implementaciones malas como las buenas
  /// </summary>
  public class NamingTests
  {
    [Fact]
    public void UserServiceBad_ValidateUser_UnderAge_ReturnsFalse()
    {
      // Arrange - Preparar
      var service = new UserService(); // De naming-bad.cs

      // Act - Actuar
      var result = service.ValidateUser(17, "ACT", 1200);

      // Assert - Verificar
      Assert.False(result);
    }

    [Fact]
    public void UserServiceBad_ValidateUser_ActiveStatus_ReturnsTrue()
    {
      // Arrange
      var service = new UserService();

      // Act
      var result = service.ValidateUser(20, "ACT", 500);

      // Assert
      Assert.True(result);
    }

    [Fact]
    public void UserServiceBad_ValidateUser_PremiumPoints_ReturnsTrue()
    {
      // Arrange
      var service = new UserService();

      // Act
      var result = service.ValidateUser(20, "INA", 1200);

      // Assert
      Assert.True(result);
    }

    [Fact]
    public void UserServiceBad_CalculateDiscount_VIP_Returns20Percent()
    {
      // Arrange
      var service = new UserService();

      // Act
      var discount = service.CalculateDiscount(100, "VIP");

      // Assert
      Assert.Equal(20.0, discount);
    }

    [Fact]
    public void UserServiceBad_CalculateDiscount_Regular_Returns5Percent()
    {
      // Arrange
      var service = new UserService();

      // Act
      var discount = service.CalculateDiscount(100, "REG");

      // Assert
      Assert.Equal(5.0, discount);
    }

    [Fact]
    public void UserServiceBad_CalculateDiscount_UnknownType_ReturnsZero()
    {
      // Arrange
      var service = new UserService();

      // Act
      var discount = service.CalculateDiscount(100, "UNKNOWN");

      // Assert
      Assert.Equal(0, discount);
    }
  }
}

/*
INSTRUCCIONES PARA EJECUTAR LOS TESTS:

1. Instalar .NET SDK (si no está instalado):
   https://dotnet.microsoft.com/download

2. Navegar a la carpeta del concepto:
   cd katas/csharp/CleanCode/naming

3. Crear un proyecto de tests (solo primera vez):
   dotnet new xunit -n NamingTests

4. Agregar referencia a los archivos fuente:
   - Copiar naming-bad.cs y naming-good.cs a la carpeta del proyecto de tests
   - O agregar referencias apropiadas

5. Ejecutar los tests:
   dotnet test

6. Ejecutar tests con detalles:
   dotnet test --logger "console;verbosity=detailed"
*/
