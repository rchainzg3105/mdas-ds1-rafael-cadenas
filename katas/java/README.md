# 🎓 Clean Code, OOP, Principios SOLID y Patrones de Diseño en Java

Este proyecto presenta ejemplos prácticos de Clean Code, OOP, Principios SOLID y Patrones de Diseño usando Java. Cada concepto incluye ejemplos "malos" (violando principios) y "buenos" (siguiendo buenas prácticas) para facilitar el aprendizaje.

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
# Verificar Java instalado
java --version   # Debe ser 11 o mayor
javac --version  # Debe ser 11 o mayor
```

### Instalación

```bash
# No se requiere instalación adicional
# Solo necesitas el JDK
```

### Ejecutar Ejemplos

**Opción 1: Compilar y Ejecutar (Recomendado para aprender)**

```bash
# Compilar
javac CleanCode/naming/NamingBad.java

# Ejecutar
java CleanCode.naming.NamingBad
```

**Opción 2: Usar Maven (Para proyectos completos)**

```bash
# Crear proyecto Maven (solo una vez)
mvn archetype:generate -DgroupId=com.katas -DartifactId=solid-katas

# Compilar y ejecutar
mvn compile exec:java -Dexec.mainClass="NamingBad"
```

**Opción 3: Usar Gradle**

```bash
# Crear proyecto Gradle (solo una vez)
gradle init

# Ejecutar
gradle run
```

### Ejemplo Completo

```bash
# 1. Navegar a la carpeta
cd katas/java

# 2. Ejecutar ejemplo malo
javac OOP/abstraction/AbstractionBad.java
java OOP.abstraction.AbstractionBad

# 3. Modificar el ejercicio
code OOP/abstraction/AbstractionExercise.java

# 4. Compilar y ejecutar tu solución
javac OOP/abstraction/AbstractionExercise.java
java OOP.abstraction.AbstractionExercise

# 5. Ver la solución
javac OOP/abstraction/AbstractionGood.java
java OOP.abstraction.AbstractionGood
```

## 🎯 Formato de aprendizaje (20 minutos por concepto)

Cada carpeta incluye:

1. **README.md** - Guía de aprendizaje
2. **EjemploBad.java** - Código que viola el principio
3. **EjemploExercise.java** - Archivo para tu práctica
4. **EjemploGood.java** - Código que sigue el principio

### Cómo estudiar

1. Lee el README del concepto
2. Ejecuta y analiza el ejemplo malo
   ```bash
   javac OOP/abstraction/AbstractionBad.java
   java OOP.abstraction.AbstractionBad
   ```
3. Aplica las técnicas y principios aprendidos para refactorizar el ejemplo malo
4. Ejecuta tu solución
   ```bash
   javac OOP/abstraction/AbstractionExercise.java
   java OOP.abstraction.AbstractionExercise
   ```
5. Ejecuta y estudia el ejemplo bueno
   ```bash
   javac OOP/abstraction/AbstractionGood.java
   java OOP.abstraction.AbstractionGood
   ```

### Compilar y ejecutar múltiples archivos

```bash
# Compilar todos los archivos de una carpeta
javac CleanCode/naming/*.java

# Ejecutar un archivo específico
java CleanCode.naming.NamingGood
```

## 🧪 Tests Unitarios

Cada concepto incluye tests unitarios completos usando **JUnit 5** para validar tanto las implementaciones malas como las buenas.

### Instalación del framework de testing

#### Opción 1: Descargar JUnit standalone

```bash
# Descargar JUnit Platform Console Standalone
wget https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.9.3/junit-platform-console-standalone-1.9.3.jar

# O con curl
curl -O https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.9.3/junit-platform-console-standalone-1.9.3.jar
```

#### Opción 2: Usar Maven (pom.xml)

```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.9.3</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

#### Opción 3: Usar Gradle (build.gradle)

```gradle
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter:5.9.3'
}

test {
    useJUnitPlatform()
}
```

### Ejecutar todos los tests

```bash
# Con Maven
mvn test

# Con Gradle
gradle test

# Con JUnit standalone (desde la raíz)
java -jar junit-platform-console-standalone-1.9.3.jar \
  --class-path . \
  --scan-class-path
```

### Ejecutar tests por concepto

```bash
# Compilar tests de un concepto específico
cd CleanCode/naming
javac -cp .:../../junit-platform-console-standalone-1.9.3.jar *.java

# Ejecutar tests
java -jar ../../junit-platform-console-standalone-1.9.3.jar \
  --class-path . \
  --select-class NamingTests

# O con Maven (si está configurado)
mvn test -Dtest=NamingTests

# O con Gradle
gradle test --tests NamingTests
```

### Ejecutar tests por categoría

```bash
# Todos los tests de Clean Code
mvn test -Dtest=CleanCode.**

# Todos los tests de SOLID
mvn test -Dtest=SOLID.**

# Todos los tests de Patterns
mvn test -Dtest=Patterns.**
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

**Problema:** `javac: command not found`
**Solución:** Instalar JDK y configurar JAVA_HOME

**Problema:** `package org.junit.jupiter does not exist`
**Solución:** Ejecutar `mvn install` o descargar JUnit manualmente

**Problema:** `Could not find or load main class`
**Solución:** Verificar el classpath y el nombre completo de la clase con paquete

**Problema:** Tests no corren
**Solución:** Verificar anotación `@Test` y imports correctos

**Problema:** `NoClassDefFoundError`
**Solución:** Compilar todas las clases dependientes

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
javac CleanCode/naming/NamingGood.java

# Ejecutar (nota el formato con paquetes)
java CleanCode.naming.NamingGood

# Compilar múltiples archivos
javac CleanCode/naming/*.java

# Ejecutar con classpath
java -cp . CleanCode.naming.NamingGood

# Compilar con warnings
javac -Xlint:all CleanCode/naming/NamingGood.java

# Crear JAR
jar cvf katas.jar CleanCode/**/*.class

# Con Maven - limpiar y compilar
mvn clean compile

# Con Gradle
gradle build
gradle run
```

## 📚 Recursos Adicionales

### Documentación de Frameworks

- **JUnit 5**: https://junit.org/junit5/
- **Java Documentation**: https://docs.oracle.com/en/java/
- **Maven**: https://maven.apache.org/guides/
- **Gradle**: https://docs.gradle.org/

### Tutoriales

- JUnit: https://junit.org/junit5/docs/current/user-guide/
- Maven Getting Started: https://maven.apache.org/guides/getting-started/

### Buenas Prácticas de Testing

- Arrange-Act-Assert (AAA) pattern
- Tests independientes y aislados
- Un concepto por test
- Nombres descriptivos
- Setup y Teardown cuando sea necesario

### Libros y Recursos

- **Clean Code (libro)**: Robert C. Martin
- **Effective Java**: Joshua Bloch
- **Design Patterns in Java**: https://refactoring.guru/design-patterns/java

## 🎯 Características de Java Utilizadas

- **Interfaces**: Para abstracción y contratos
- **Abstract Classes**: Para herencia con implementación base
- **Encapsulation**: Con getters/setters y modificadores de acceso
- **Polymorphism**: Con @Override y interfaces
- **Static Members**: Para constantes y factory methods
- **Builder Pattern**: Con fluent interface
- **Generics**: Para type safety (cuando aplicable)
- **Collections Framework**: ArrayList, HashMap, etc.
- **Exception Handling**: Try-catch para manejo de errores
- **Java 11+ Features**: var, String methods, etc.

## 📦 Configuración de Maven (pom.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.mdas.katas</groupId>
    <artifactId>java-katas</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.9.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

---

**¡Disfruta aprendiendo Java con buenas prácticas!** ☕
