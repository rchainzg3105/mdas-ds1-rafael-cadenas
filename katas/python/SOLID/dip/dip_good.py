# Cumplimiento del DIP: Módulos de alto y bajo nivel dependen de la abstracción
# ✅ Solución: Introducir interfaz de la que ambos módulos dependan

from abc import ABC, abstractmethod


# ✅ Abstracción de la que ambos módulos dependen
class Database(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass


# ✅ Módulos de bajo nivel implementan la abstracción
class MySQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"Guardando en MySQL: {data}")


class PostgreSQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"Guardando en PostgreSQL: {data}")


class MongoDatabase(Database):
    def save(self, data: str) -> None:
        print(f"Guardando en MongoDB: {data}")


# ✅ Módulo de alto nivel depende de la abstracción, no de la implementación concreta
class OrderService:
    def __init__(self, database: Database):
        self.database = database  # ✅ ¡Depende de la interfaz!

    def process_order(self, order_id: str) -> None:
        print(f"Procesando pedido {order_id}")

        # ✅ ¡Puede trabajar con CUALQUIER implementación de base de datos!
        self.database.save(f"Pedido {order_id} procesado")


# ✅ Beneficios: Fácil de intercambiar bases de datos, probar y extender
if __name__ == "__main__":
    print("=== Uso Cumpliendo el DIP ===")

    mysql_db = MySQLDatabase()
    postgres_db = PostgreSQLDatabase()
    mongo_db = MongoDatabase()

    # ¡El mismo OrderService funciona con diferentes bases de datos! ✅
    order_service1 = OrderService(mysql_db)
    order_service2 = OrderService(postgres_db)
    order_service3 = OrderService(mongo_db)

    order_service1.process_order("001")
    order_service2.process_order("002")
    order_service3.process_order("003")
