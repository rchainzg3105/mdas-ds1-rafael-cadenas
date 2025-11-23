````markdown
# Clean Code: Formato - Ejemplo

## 🎯 Objetivos de aprendizaje

- Mantener líneas de código cortas (formato horizontal)
- Usar espaciado vertical para separar conceptos
- Aplicar formato consistente en todo el código
- Agrupar código relacionado y separar conceptos diferentes

## 📋 El problema: Código Difícil de Leer

**Regla:** _El formato del código debe facilitar su lectura y comprensión_

### ¿Qué está mal aquí? 🚫

```csharp
// ❌ Formato horizontal malo - línea demasiado larga
public class ProductService {
  private List<Product> products = new List<Product> { new Product { Id = 1, Name = "Laptop", Price = 1200 } };
  public Product FindProductById(int id) { return products.FirstOrDefault(p => p.Id == id); }
}

// ❌ Formato vertical malo - todo junto sin espacios
public class OrderProcessor {
  private List<Order> orders = new List<Order>();
  public bool ProcessOrder(List<OrderItem> items) {
    decimal total = 0;
    for (int i = 0; i < items.Count; i++) { total += items[i].Price; }
    orders.Add(new Order { Total = total });
    return true;
  }
  public List<Order> GetOrders() { return orders; }
}
```

**Problemas:**

- **Horizontal**: Líneas demasiado largas, difíciles de leer
- **Vertical**: Sin espacios entre métodos, todo amontonado
- **Inconsistente**: Mezcla de estilos de formato
- **Agrupación**: Código relacionado está separado

## 🔧 Tu tarea

1. **Estudia** `format-bad.cs` - intenta leer código con mal formato
2. **Implementa** tu solución en `format-exercise.cs` antes de ver la propuesta
3. **Observa** `format-good.cs` y compara con tu solución

## 🎯 Puntos clave

- Líneas cortas (80-120 caracteres)
- Espaciado vertical separa conceptos
- Formato consistente en todo el código
- Código relacionado agrupado junto

## ⏱️ Verificación rápida

Pregúntate:

- ¿Las líneas son cortas y legibles?
- ¿Hay espacios entre conceptos diferentes?
- ¿El formato es consistente?

## 🚀 Cómo ejecutar

```bash
# Compilar y ejecutar
csc format-bad.cs && format-bad.exe
csc format-good.cs && format-good.exe

# O usando dotnet script (si está instalado)
dotnet script format-bad.cs
dotnet script format-good.cs
```
````
