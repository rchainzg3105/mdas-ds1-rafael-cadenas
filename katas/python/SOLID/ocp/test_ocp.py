"""
Tests para el principio OCP (Open/Closed Principle)
Valida tanto las implementaciones malas como las buenas
"""

import pytest
from ocp_bad import DiscountCalculator as DiscountCalculatorBad
from ocp_good import (
    DiscountCalculator as DiscountCalculatorGood,
    RegularDiscount,
    VIPDiscount,
    StudentDiscount
)


class TestOCPBad:
    """Tests para la implementación que viola OCP"""

    def test_regular_discount(self):
        """Verifica el descuento para clientes regulares"""
        calculator = DiscountCalculatorBad()
        assert calculator.calculate_discount("regular", 100) == 95.0

    def test_vip_discount(self):
        """Verifica el descuento para clientes VIP"""
        calculator = DiscountCalculatorBad()
        assert calculator.calculate_discount("vip", 100) == 80.0

    def test_student_discount(self):
        """Verifica el descuento para estudiantes"""
        calculator = DiscountCalculatorBad()
        assert calculator.calculate_discount("student", 100) == 85.0

    def test_unknown_customer_type(self):
        """Verifica que tipos desconocidos no reciban descuento"""
        calculator = DiscountCalculatorBad()
        assert calculator.calculate_discount("unknown", 100) == 100


class TestOCPGood:
    """Tests para la implementación que cumple con OCP"""

    def test_regular_discount(self):
        """Verifica el descuento para clientes regulares"""
        calculator = DiscountCalculatorGood()
        discount_strategy = RegularDiscount()
        assert calculator.calculate_discount(discount_strategy, 100) == 95.0

    def test_vip_discount(self):
        """Verifica el descuento para clientes VIP"""
        calculator = DiscountCalculatorGood()
        discount_strategy = VIPDiscount()
        assert calculator.calculate_discount(discount_strategy, 100) == 80.0

    def test_student_discount(self):
        """Verifica el descuento para estudiantes"""
        calculator = DiscountCalculatorGood()
        discount_strategy = StudentDiscount()
        assert calculator.calculate_discount(discount_strategy, 100) == 85.0

    def test_extensibility(self):
        """Verifica que se pueden agregar nuevos tipos de descuento sin modificar el calculador"""
        from ocp_good import DiscountStrategy

        # Nuevo tipo de descuento: Senior
        class SeniorDiscount(DiscountStrategy):
            def apply_discount(self, price: float) -> float:
                return price * 0.70  # 30% de descuento

        calculator = DiscountCalculatorGood()
        senior_discount = SeniorDiscount()
        assert calculator.calculate_discount(senior_discount, 100) == 70.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
