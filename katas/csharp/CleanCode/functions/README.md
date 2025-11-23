````markdown
# Clean Code: Funciones - Ejemplo

## 🎯 Objetivos de aprendizaje

- Crear funciones que hacen UNA sola cosa
- Mantener funciones pequeñas y legibles
- Usar el mismo nivel de abstracción en cada función
- Evitar efectos secundarios inesperados
- Aplicar early return para mejorar legibilidad

## 📋 El problema: Funciones que hacen demasiado

**Regla:** _Las funciones deben hacer una sola cosa, hacerla bien, y ser lo único que hagan_

### ¿Qué está mal aquí? 🚫

```csharp
public void ProcessOrder(string name, string email, List<Item> items, Payment payment)
{
    // ❌ Valida
    if (string.IsNullOrEmpty(name)) return;
    if (!email.Contains("@")) return;

    // ❌ Calcula
    decimal total = 0;
    for (int i = 0; i < items.Count; i++)
    {
        total += items[i].Price * items[i].Quantity;
    }

    // ❌ Aplica descuento
    if (total > 100) total = total * 0.9m;

    // ❌ Guarda
    this.orders.Add(new Order { ... });

    // ❌ Envía email
    Console.WriteLine("Sending email...");
    this.emailsSent++; // ❌ Efecto secundario
}
```

**Problemas:**

- **Hace muchas cosas**: valida, calcula, guarda, envía email
- **Muy grande**: difícil de leer y probar
- **Niveles mezclados**: alto nivel (guardar) + bajo nivel (loop)
- **Efectos secundarios**: modifica `emailsSent` sin avisar
- **Sin early return**: muchos niveles de anidación

## 🔧 Tu tarea

1. **Estudia** `functions-bad.cs` - identifica funciones grandes con múltiples responsabilidades
2. **Implementa** tu solución en `functions-exercise.cs` antes de ver la propuesta
3. **Observa** `functions-good.cs` y compara con tu solución

## 🎯 Puntos clave

- Una función = una responsabilidad
- Funciones pequeñas (5-20 líneas)
- Mismo nivel de abstracción
- Sin efectos secundarios inesperados
- Early return para validaciones

## ⏱️ Verificación rápida

Pregúntate:

- ¿Esta función hace una sola cosa?
- ¿Es pequeña y fácil de entender?
- ¿Mezcla niveles de abstracción?

## 🚀 Cómo ejecutar

```bash
# Compilar y ejecutar
csc functions-bad.cs && functions-bad.exe
csc functions-good.cs && functions-good.exe

# O usando dotnet script (si está instalado)
dotnet script functions-bad.cs
dotnet script functions-good.cs
```
````
