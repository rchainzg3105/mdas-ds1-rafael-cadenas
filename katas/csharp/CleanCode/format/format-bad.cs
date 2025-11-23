using System;
using System.Collections.Generic;
using System.Linq;

// Violación de Clean Code: Mal Formato
// ❌ Problemas: Formato horizontal y vertical incorrecto

// ❌ Líneas demasiado largas (formato horizontal malo)
public class ProductService
{
  private List<Product> products = new List<Product>
    {
        new Product { Id = 1, Name = "Laptop", Price = 1200, Category = "Electronics", Stock = 50, Supplier = "TechCorp", Warranty = "2 years" },
        new Product { Id = 2, Name = "Mouse", Price = 25, Category = "Accessories", Stock = 200, Supplier = "TechCorp", Warranty = "1 year" }
    };
  public Product FindProductByIdAndUpdateStockAndCalculateDiscountAndSendNotification(int id, int quantity, decimal discountRate)
  {
    var product = products.FirstOrDefault(p => p.Id == id);
    if (product != null)
    {
      product.Stock -= quantity;
      var discountedPrice = product.Price * discountRate;
      Console.WriteLine($"Producto {product.Name} actualizado. Stock: {product.Stock}, Precio con descuento: {discountedPrice}");
      return new Product { Id = product.Id, Name = product.Name, Price = product.Price, Category = product.Category, Stock = product.Stock, Supplier = product.Supplier, Warranty = product.Warranty, DiscountedPrice = discountedPrice };
    }
    return null;
  }
}

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

// ❌ Sin espaciado vertical - todo junto
public class OrderProcessor
{
  private List<Order> orders = new List<Order>();
  public bool ProcessOrder(int customerId, List<OrderItem> items, string paymentMethod)
  {
    if (customerId == 0 || items == null || items.Count == 0)
    {
      return false;
    }
    decimal total = 0;
    for (int i = 0; i < items.Count; i++)
    {
      total += items[i].Price * items[i].Quantity;
    }
    if (total > 100)
    {
      total = total * 0.9m;
    }
    var order = new Order { Id = DateTime.Now.Ticks, CustomerId = customerId, Items = items, Total = total, Date = DateTime.Now, Status = "pending" };
    orders.Add(order);
    Console.WriteLine($"Orden procesada: ${total}");
    return true;
  }
  public List<Order> GetOrders()
  {
    return orders;
  }
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

// ❌ Formato inconsistente y mezcla de estilos
public class UserManager
{
  private List<User> users = new List<User>();
  public User AddUser(string name, string email, int age)
  {
    var user = new User { Name = name, Email = email, Age = age, CreatedAt = DateTime.Now };
    users.Add(user);
    return user;
  }

  public User FindUser(string email)
  {
    for (int i = 0; i < users.Count; i++)
    {
      if (users[i].Email == email)
      {
        return users[i];
      }
    }
    return null;
  }

  public void DeleteUser(string email)
  {
    users = users.Where(u => u.Email != email).ToList();
  }
}

public class User
{
  public string Name { get; set; }
  public string Email { get; set; }
  public int Age { get; set; }
  public DateTime CreatedAt { get; set; }
}

// Uso
class Program
{
  static void Main()
  {
    Console.WriteLine("=== Violación de Formato en Clean Code ===");
    var service = new ProductService();
    var product = service.FindProductByIdAndUpdateStockAndCalculateDiscountAndSendNotification(1, 5, 0.8m);
    Console.WriteLine(product?.Name);
    var processor = new OrderProcessor();
    processor.ProcessOrder(1, new List<OrderItem> { new OrderItem { Price = 100, Quantity = 2 } }, "credit_card");
  }
}
