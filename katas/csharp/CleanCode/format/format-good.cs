using System;
using System.Collections.Generic;
using System.Linq;

// Cumplimiento de Clean Code: Buen Formato
// ✅ Solución: Formato horizontal y vertical correcto

// ✅ Líneas cortas (idealmente max 80-120 caracteres)
// ✅ Espaciado apropiado entre operadores y elementos

public class Product
{
  public int Id { get; set; }
  public string Name { get; set; }
  public decimal Price { get; set; }
  public string Category { get; set; }
  public int Stock { get; set; }
  public string Supplier { get; set; }
  public string Warranty { get; set; }
  public decimal? DiscountedPrice { get; set; }
}

public class ProductService
{
  private List<Product> products = new List<Product>
    {
        new Product
        {
            Id = 1,
            Name = "Laptop",
            Price = 1200,
            Category = "Electronics",
            Stock = 50,
            Supplier = "TechCorp",
            Warranty = "2 years"
        },
        new Product
        {
            Id = 2,
            Name = "Mouse",
            Price = 25,
            Category = "Accessories",
            Stock = 200,
            Supplier = "TechCorp",
            Warranty = "1 year"
        }
    };

  // ✅ Líneas cortas, una acción por línea
  public Product FindProductByIdAndUpdateStockAndCalculateDiscountAndSendNotification(
      int productId,
      int quantity,
      decimal discountRate)
  {
    var product = FindProductById(productId);

    if (product == null)
    {
      return null;
    }

    product.Stock -= quantity;
    var discountedPrice = CalculateDiscountedPrice(product.Price, discountRate);

    Console.WriteLine(
        $"Producto {product.Name} actualizado. " +
        $"Stock: {product.Stock}, " +
        $"Precio con descuento: {discountedPrice}");

    return new Product
    {
      Id = product.Id,
      Name = product.Name,
      Price = product.Price,
      Category = product.Category,
      Stock = product.Stock,
      Supplier = product.Supplier,
      Warranty = product.Warranty,
      DiscountedPrice = discountedPrice
    };
  }

  private Product FindProductById(int id)
  {
    return products.FirstOrDefault(product => product.Id == id);
  }

  private decimal CalculateDiscountedPrice(decimal price, decimal discountRate)
  {
    return price * discountRate;
  }
}

// ✅ Espaciado vertical apropiado
// ✅ Líneas en blanco separan conceptos relacionados
// ✅ Métodos relacionados están cerca

public class OrderItem
{
  public decimal Price { get; set; }
  public int Quantity { get; set; }
}

public class Order
{
  public long Id { get; set; }
  public int CustomerId { get; set; }
  public List<OrderItem> Items { get; set; }
  public decimal Total { get; set; }
  public DateTime Date { get; set; }
  public string Status { get; set; }
}

public class OrderProcessor
{
  private const decimal DISCOUNT_THRESHOLD = 100;
  private const decimal DISCOUNT_RATE = 0.9m;

  private List<Order> orders = new List<Order>();

  // ✅ Grupo 1: Procesamiento de órdenes
  public bool ProcessOrder(int customerId, List<OrderItem> items, string paymentMethod)
  {
    if (!IsValidOrder(customerId, items))
    {
      return false;
    }

    decimal total = CalculateTotal(items);
    var order = CreateOrder(customerId, items, total);

    SaveOrder(order);
    LogOrderProcessed(total);

    return true;
  }

  private bool IsValidOrder(int customerId, List<OrderItem> items)
  {
    return customerId > 0 && items != null && items.Count > 0;
  }

  private decimal CalculateTotal(List<OrderItem> items)
  {
    decimal total = items.Sum(item => item.Price * item.Quantity);

    if (total > DISCOUNT_THRESHOLD)
    {
      total = total * DISCOUNT_RATE;
    }

    return total;
  }

  private Order CreateOrder(int customerId, List<OrderItem> items, decimal total)
  {
    return new Order
    {
      Id = DateTime.Now.Ticks,
      CustomerId = customerId,
      Items = items,
      Total = total,
      Date = DateTime.Now,
      Status = "pending"
    };
  }

  private void SaveOrder(Order order)
  {
    orders.Add(order);
  }

  private void LogOrderProcessed(decimal total)
  {
    Console.WriteLine($"Orden procesada: ${total}");
  }

  // ✅ Grupo 2: Consultas de órdenes (separado por línea en blanco)
  public List<Order> GetOrders()
  {
    return orders;
  }

  // ✅ Grupo 3: Cancelación de órdenes (separado por línea en blanco)
  public bool CancelOrder(long orderId)
  {
    var order = orders.FirstOrDefault(o => o.Id == orderId);

    if (order != null)
    {
      orders.Remove(order);
      return true;
    }

    return false;
  }
}

// ✅ Formato consistente en toda la clase
// ✅ Espaciado uniforme, indentación correcta

public class User
{
  public string Name { get; set; }
  public string Email { get; set; }
  public int Age { get; set; }
  public DateTime CreatedAt { get; set; }
}

public class UserManager
{
  private List<User> users = new List<User>();

  public User AddUser(string name, string email, int age)
  {
    var user = new User
    {
      Name = name,
      Email = email,
      Age = age,
      CreatedAt = DateTime.Now
    };

    users.Add(user);
    return user;
  }

  public User FindUser(string email)
  {
    return users.FirstOrDefault(user => user.Email == email);
  }

  public void DeleteUser(string email)
  {
    users = users.Where(user => user.Email != email).ToList();
  }
}

// Uso - También con buen formato
class Program
{
  static void Main()
  {
    Console.WriteLine("=== Cumplimiento de Formato en Clean Code ===");

    var service = new ProductService();
    var product = service.FindProductByIdAndUpdateStockAndCalculateDiscountAndSendNotification(
        1, 5, 0.8m);
    Console.WriteLine(product?.Name);

    var processor = new OrderProcessor();
    var items = new List<OrderItem> { new OrderItem { Price = 100, Quantity = 2 } };
    processor.ProcessOrder(1, items, "credit_card");
  }
}
