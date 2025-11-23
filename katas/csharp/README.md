# 🎓 Clean Code, OOP, Principios SOLID y Patrones de Diseño en C#

Este proyecto presenta ejemplos prácticos de Clean Code, OOP, Principios SOLID y Patrones de Diseño usando C#. Cada concepto incluye ejemplos "malos" (violando principios) y "buenos" (siguiendo buenas prácticas) para facilitar el aprendizaje.

## 📚 Contenido del proyecto

### ✨ 1. Clean Code (`CleanCode/`)

Principios de código limpio y legible:

- **Naming** - Nombrado descriptivo (sin magic numbers, encodings)
- **Functions** - Funciones pequeñas y enfocadas (una responsabilidad)
- **Format** - Formato horizontal y vertical consistente

### 🎯 2. Programación Orientada a Objetos (`OOP/`)

Los 4 pilares fundamentales de OOP:

- **Abstraction** - Abstracción (ocultar detalles de implementación)
- **Encapsulation** - Encapsulamiento (proteger el estado interno)
- **Inheritance** - Herencia (reutilización de código)
- **Polymorphism** - Polimorfismo (comportamiento específico sin condicionales)

### 🔷 3. Principios SOLID (`SOLID/`)

Los 5 principios fundamentales de diseño orientado a objetos:

- **S** - Single Responsibility Principle (SRP) - Responsabilidad Única
- **O** - Open/Closed Principle (OCP) - Abierto/Cerrado
- **L** - Liskov Substitution Principle (LSP) - Sustitución de Liskov
- **I** - Interface Segregation Principle (ISP) - Segregación de Interfaces
- **D** - Dependency Inversion Principle (DIP) - Inversión de Dependencias

### 🏗️ 4. Patrones de Diseño (`Patterns/`)

Soluciones probadas para problemas comunes de diseño:

- **Factory** - Patrón creacional para creación de objetos
- **Builder** - Patrón creacional para construcción compleja (Pizza)
- **Adapter** - Patrón estructural para compatibilidad de interfaces
- **Strategy** - Patrón de comportamiento para selección de algoritmos

## 🚀 Preparativos

### Prerequisitos

```bash
# Verificar .NET instalado
dotnet --version  # Debe ser 6.0 o mayor
```

### Instalación

```bash
# No se requiere instalación adicional
# Solo necesitas el .NET SDK
```

### Ejecutar Ejemplos

**Opción 1: Compilar y Ejecutar**

```bash
# Compilar
csc CleanCode/naming/naming-bad.cs

# Ejecutar
./naming-bad.exe  # Windows
./naming-bad      # Linux/Mac
```

**Opción 2: Usar dotnet script**

```bash
# Instalar dotnet-script (solo una vez)
dotnet tool install -g dotnet-script

# Ejecutar
dotnet script CleanCode/naming/naming-bad.cs
```

**Opción 3: Usar dotnet run**

```bash
dotnet run --project CleanCode/naming/naming-bad.cs
```

### Ejemplo Completo

```bash
# 1. Navegar a la carpeta
cd katas/csharp

# 2. Ejecutar ejemplo malo
csc SOLID/srp/srp-bad.cs && ./srp-bad.exe

# 3. Modificar el ejercicio
code SOLID/srp/srp-exercise.cs

# 4. Ejecutar tu solución
csc SOLID/srp/srp-exercise.cs && ./srp-exercise.exe

# 5. Ver la solución
csc SOLID/srp/srp-good.cs && ./srp-good.exe
```

## 🎯 Formato de aprendizaje (20 minutos por concepto)

Cada carpeta incluye:

1. **README.md** - Guía de aprendizaje
2. **ejemplo-bad.cs** - Código que viola el principio
3. **ejemplo-exercise.cs** - Archivo para tu práctica
4. **ejemplo-good.cs** - Código que sigue el principio

### Cómo estudiar

1. Lee el README del concepto
2. Ejecuta y analiza el ejemplo malo
   ```bash
   dotnet run --project OOP/abstraction/abstraction-bad.cs
   # O compile y ejecute:
   csc OOP/abstraction/abstraction-bad.cs && ./abstraction-bad.exe
   ```
3. Aplica las técnicas y principios aprendidos para refactorizar el ejemplo malo
4. Ejecuta tu solución
   ```bash
   dotnet run --project OOP/abstraction/abstraction-exercise.cs
   ```
5. Ejecuta y estudia el ejemplo bueno
   ```bash
   dotnet run --project OOP/abstraction/abstraction-good.cs
   ```

### Ejecución de archivos individuales

```bash
# Opción 1: Usando dotnet script (recomendado para ejemplos simples)
dotnet script CleanCode/naming/naming-bad.cs

# Opción 2: Compilar y ejecutar
csc CleanCode/naming/naming-bad.cs
./naming-bad.exe

# Opción 3: Usar dotnet run con un archivo específico
dotnet run --project CleanCode/naming/naming-bad.cs
```

## 🧪 Tests Unitarios

Cada concepto incluye tests unitarios completos usando **xUnit** para validar tanto las implementaciones malas como las buenas.

### Instalación del framework de testing

```bash
# Navegar a la carpeta del concepto
cd CleanCode/naming

# Crear proyecto de tests con xUnit
dotnet new xunit -n NamingTests

# Agregar el archivo de tests al proyecto
# Copiar Tests.cs al directorio del proyecto xUnit

# Restaurar dependencias
dotnet restore
```

### Ejecutar todos los tests

```bash
# Desde la carpeta raíz de csharp
# Ejecutar todos los tests (requiere configuración previa de proyectos)
dotnet test

# Ejecutar tests con salida detallada
dotnet test -v detailed

# Ejecutar tests con coverage
dotnet test /p:CollectCoverage=true
```

### Ejecutar tests por concepto

```bash
# Tests de Clean Code - Naming
cd CleanCode/naming
dotnet new xunit -n NamingTests
# Agregar Tests.cs al proyecto
dotnet test

# Tests de SOLID - SRP
cd SOLID/srp
dotnet new xunit -n SrpTests
# Agregar Tests.cs al proyecto
dotnet test

# Tests de Patterns - Factory
cd Patterns/factory
dotnet new xunit -n FactoryTests
# Agregar Tests.cs al proyecto
dotnet test
```

## 🔍 Beneficios demostrados

### ✅ Clean Code:

- **Legibilidad**: Código fácil de entender
- **Menos Bugs**: Nombres claros reducen errores
- **Colaboración**: Otros desarrolladores entienden rápidamente
- **Mantenimiento**: Cambios futuros más simples

### ✅ OOP:

- **Abstracción**: Interfaces simples, complejidad oculta
- **Encapsulamiento**: Datos protegidos y validados
- **Herencia**: Código compartido, menos duplicación
- **Polimorfismo**: Extensible sin modificar código existente

### ✅ SOLID:

- **Mantenibilidad**: Fácil de modificar y extender
- **Testabilidad**: Clases pueden probarse aisladamente
- **Flexibilidad**: Código se adapta a cambios
- **Legibilidad**: Separación clara de responsabilidades
- **Reutilización**: Componentes reutilizables

### ✅ Patrones de Diseño:

- **Reutilización**: Soluciones probadas a problemas comunes
- **Comunicación**: Vocabulario compartido entre desarrolladores
- **Mejores Prácticas**: Enfoques probados en el tiempo
- **Flexibilidad**: Modificar comportamiento sin cambiar estructura
- **Mantenibilidad**: Código bien organizado y predecible

## 🔧 Solución de Problemas Comunes

**Problema:** `dotnet: command not found`
**Solución:** Instalar .NET SDK desde https://dotnet.microsoft.com/download

**Problema:** `csc: command not found`
**Solución:** Usar `dotnet` o agregar el compilador al PATH

**Problema:** Referencias no encontradas en tests
**Solución:** Verificar rutas en `.csproj` con `<Compile Include="../archivo.cs" />`

**Problema:** Tests no se ejecutan
**Solución:** Ejecutar `dotnet build` primero

**Problema:** Namespace conflicts
**Solución:** Usar namespaces únicos o `global using` en C# 10+

## 🎓 Ruta de Aprendizaje Recomendada

1. **Clean Code** (60 minutos)

   - naming → functions → format

2. **OOP** (80 minutos)

   - abstraction → encapsulation → inheritance → polymorphism

3. **SOLID** (100 minutos)

   - srp → ocp → dip → isp → lsp

4. **Patterns** (80 minutos)
   - factory → strategy → builder → adapter

## 🛠️ Comandos Útiles

```bash
# Compilar un archivo
csc CleanCode/naming/naming-good.cs

# Ejecutar
./naming-good.exe  # Windows
./naming-good      # Linux/Mac (con Mono)

# Compilar con warnings
csc /warn:4 CleanCode/naming/naming-good.cs

# Crear proyecto de consola
dotnet new console -n MiProyecto

# Ejecutar tests con filtro
dotnet test --filter "FullyQualifiedName~UserServiceBad"

# Limpiar builds
dotnet clean
```

## 📚 Recursos Adicionales

### Documentación de Frameworks

- **xUnit**: https://xunit.net/
- **C# Documentation**: https://docs.microsoft.com/en-us/dotnet/csharp/
- **.NET CLI**: https://docs.microsoft.com/en-us/dotnet/core/tools/

### Tutoriales

- xUnit: https://xunit.net/docs/getting-started/netcore/cmdline
- C# Testing: https://docs.microsoft.com/en-us/dotnet/core/testing/

### Buenas Prácticas de Testing

- Arrange-Act-Assert (AAA) pattern
- Tests independientes y aislados
- Un concepto por test
- Nombres descriptivos
- Setup y Teardown cuando sea necesario

### Libros y Recursos

- **Clean Code (libro)**: Robert C. Martin
- **Design Patterns in C#**: https://refactoring.guru/design-patterns/csharp

## 🎯 Características de C# Utilizadas

- **Properties**: Para encapsulamiento elegante
- **Interfaces**: Para abstracción y polimorfismo
- **Abstract Classes**: Para herencia con comportamiento base
- **Static Members**: Para constantes y métodos utilitarios
- **Constructor Chaining**: En el patrón Builder
- **Object Initializers**: Para inicialización clara
- **String Interpolation**: Para concatenación legible
- **Nullable Reference Types**: Para evitar null reference exceptions (C# 8+)
- **Record Types**: Para objetos inmutables (C# 9+)
- **Top-level Statements**: Para código más conciso (C# 9+)

---

**¡Disfruta aprendiendo C# con buenas prácticas!** 🔷
