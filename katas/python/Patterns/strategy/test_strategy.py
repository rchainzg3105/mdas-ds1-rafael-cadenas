"""
Tests para el patrón Strategy
Valida tanto las implementaciones malas como las buenas
"""

import pytest
from strategy_bad import ShippingCalculator as ShippingCalculatorBad
from strategy_good import ShippingCalculator as ShippingCalculatorGood, StandardShipping, ExpressShipping, OvernightShipping


class TestStrategyBad:
    """Tests para la implementación sin patrón Strategy"""

    def test_standard_shipping_cost(self):
        """Verifica el cálculo de costo de envío estándar"""
        calculator = ShippingCalculatorBad()
        cost = calculator.calculate_shipping_cost(100, "standard")
        assert cost == 10.0

    def test_express_shipping_cost(self):
        """Verifica el cálculo de costo de envío express"""
        calculator = ShippingCalculatorBad()
        cost = calculator.calculate_shipping_cost(100, "express")
        assert cost == 20.0

    def test_overnight_shipping_cost(self):
        """Verifica el cálculo de costo de envío overnight"""
        calculator = ShippingCalculatorBad()
        cost = calculator.calculate_shipping_cost(100, "overnight")
        assert cost == 50.0

    def test_unknown_shipping_type(self):
        """Verifica el manejo de tipos de envío desconocidos"""
        calculator = ShippingCalculatorBad()
        cost = calculator.calculate_shipping_cost(100, "unknown")
        assert cost == 0


class TestStrategyGood:
    """Tests para la implementación con patrón Strategy"""

    def test_standard_shipping_strategy(self):
        """Verifica la estrategia de envío estándar"""
        strategy = StandardShipping()
        cost = strategy.calculate(100)
        assert cost == 10.0

    def test_express_shipping_strategy(self):
        """Verifica la estrategia de envío express"""
        strategy = ExpressShipping()
        cost = strategy.calculate(100)
        assert cost == 20.0

    def test_overnight_shipping_strategy(self):
        """Verifica la estrategia de envío overnight"""
        strategy = OvernightShipping()
        cost = strategy.calculate(100)
        assert cost == 50.0

    def test_calculator_with_standard_strategy(self):
        """Verifica el calculador con estrategia estándar"""
        calculator = ShippingCalculatorGood(StandardShipping())
        cost = calculator.calculate_cost(100)
        assert cost == 10.0

    def test_calculator_with_express_strategy(self):
        """Verifica el calculador con estrategia express"""
        calculator = ShippingCalculatorGood(ExpressShipping())
        cost = calculator.calculate_cost(100)
        assert cost == 20.0

    def test_calculator_with_overnight_strategy(self):
        """Verifica el calculador con estrategia overnight"""
        calculator = ShippingCalculatorGood(OvernightShipping())
        cost = calculator.calculate_cost(100)
        assert cost == 50.0

    def test_strategy_can_be_changed(self):
        """Verifica que se puede cambiar la estrategia en tiempo de ejecución"""
        calculator = ShippingCalculatorGood(StandardShipping())
        cost1 = calculator.calculate_cost(100)
        assert cost1 == 10.0

        calculator.set_strategy(ExpressShipping())
        cost2 = calculator.calculate_cost(100)
        assert cost2 == 20.0

        calculator.set_strategy(OvernightShipping())
        cost3 = calculator.calculate_cost(100)
        assert cost3 == 50.0

    def test_extensibility(self):
        """Verifica que se pueden agregar nuevas estrategias fácilmente"""
        from strategy_good import ShippingStrategy

        class SameDayShipping(ShippingStrategy):
            def calculate(self, weight: float) -> float:
                return weight * 0.75  # $0.75 por kg

        calculator = ShippingCalculatorGood(SameDayShipping())
        cost = calculator.calculate_cost(100)
        assert cost == 75.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
