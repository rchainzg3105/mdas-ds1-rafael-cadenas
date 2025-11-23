"""
Tests para el concepto de Polimorfismo en OOP
Valida tanto las implementaciones malas como las buenas
"""

import pytest
from polymorphism_bad import process_payment_bad
from polymorphism_good import CreditCard, PayPal, Bitcoin, PaymentProcessor


class TestPolymorphismBad:
    """Tests para la implementación sin polimorfismo"""

    def test_process_credit_card_payment(self):
        """Verifica el procesamiento de pago con tarjeta de crédito"""
        result = process_payment_bad("credit_card", 100)
        assert "Procesando pago de $100 con tarjeta de crédito" in result

    def test_process_paypal_payment(self):
        """Verifica el procesamiento de pago con PayPal"""
        result = process_payment_bad("paypal", 200)
        assert "Procesando pago de $200 con PayPal" in result

    def test_process_bitcoin_payment(self):
        """Verifica el procesamiento de pago con Bitcoin"""
        result = process_payment_bad("bitcoin", 300)
        assert "Procesando pago de $300 con Bitcoin" in result

    def test_unknown_payment_method(self):
        """Verifica el manejo de métodos de pago desconocidos"""
        result = process_payment_bad("unknown", 100)
        assert "Método de pago desconocido" in result


class TestPolymorphismGood:
    """Tests para la implementación con polimorfismo"""

    def test_credit_card_payment(self):
        """Verifica el procesamiento de pago con tarjeta de crédito"""
        payment = CreditCard()
        result = payment.process(100)
        assert "Procesando pago de $100 con tarjeta de crédito" in result

    def test_paypal_payment(self):
        """Verifica el procesamiento de pago con PayPal"""
        payment = PayPal()
        result = payment.process(200)
        assert "Procesando pago de $200 con PayPal" in result

    def test_bitcoin_payment(self):
        """Verifica el procesamiento de pago con Bitcoin"""
        payment = Bitcoin()
        result = payment.process(300)
        assert "Procesando pago de $300 con Bitcoin" in result

    def test_polymorphic_behavior(self):
        """Verifica el comportamiento polimórfico"""
        processor = PaymentProcessor()

        # Diferentes métodos de pago, misma interfaz
        payments = [
            CreditCard(),
            PayPal(),
            Bitcoin()
        ]

        amounts = [100, 200, 300]

        for payment_method, amount in zip(payments, amounts):
            result = processor.execute_payment(payment_method, amount)
            assert f"${amount}" in result

    def test_extensibility(self):
        """Verifica que se pueden agregar nuevos métodos de pago fácilmente"""
        from polymorphism_good import PaymentMethod

        class ApplePay(PaymentMethod):
            def process(self, amount: float) -> str:
                return f"Procesando pago de ${amount} con Apple Pay"

        processor = PaymentProcessor()
        apple_pay = ApplePay()
        result = processor.execute_payment(apple_pay, 150)
        assert "Apple Pay" in result
        assert "$150" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
