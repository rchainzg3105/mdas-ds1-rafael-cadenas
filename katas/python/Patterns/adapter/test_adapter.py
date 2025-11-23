"""
Tests para el patrón Adapter
Valida tanto las implementaciones malas como las buenas
"""

import pytest
from adapter_bad import LegacyPaymentSystem, process_payment_bad
from adapter_good import LegacyPaymentSystem as LegacyPaymentSystemGood, PaymentAdapter, ModernPaymentProcessor


class TestAdapterBad:
    """Tests para la implementación sin patrón Adapter"""

    def test_legacy_payment_system(self):
        """Verifica que el sistema legacy funciona"""
        legacy = LegacyPaymentSystem()
        result = legacy.make_payment_old_way("123", 100)
        assert "Procesando pago antiguo" in result
        assert "Account: 123" in result
        assert "Amount: 100" in result

    def test_process_payment_wrapper(self):
        """Verifica que la función wrapper convierte la interfaz"""
        result = process_payment_bad("456", 200)
        assert "Procesando pago antiguo" in result
        assert "456" in result
        assert "200" in result


class TestAdapterGood:
    """Tests para la implementación con patrón Adapter"""

    def test_legacy_system(self):
        """Verifica que el sistema legacy funciona"""
        legacy = LegacyPaymentSystemGood()
        result = legacy.make_payment_old_way("123", 100)
        assert "Procesando pago antiguo" in result

    def test_payment_adapter(self):
        """Verifica que el adapter adapta la interfaz legacy a la moderna"""
        legacy = LegacyPaymentSystemGood()
        adapter = PaymentAdapter(legacy)
        result = adapter.process_payment("456", 200)
        assert "Procesando pago antiguo" in result
        assert "456" in result
        assert "200" in result

    def test_modern_processor_with_adapter(self):
        """Verifica que el procesador moderno puede usar el sistema legacy a través del adapter"""
        legacy = LegacyPaymentSystemGood()
        adapter = PaymentAdapter(legacy)
        processor = ModernPaymentProcessor()

        result = processor.execute(adapter, "789", 300)
        assert "Ejecutando pago moderno" in result
        assert "Procesando pago antiguo" in result

    def test_adapter_interface_compatibility(self):
        """Verifica que el adapter implementa la interfaz moderna"""
        from adapter_good import PaymentProcessor

        legacy = LegacyPaymentSystemGood()
        adapter = PaymentAdapter(legacy)

        # El adapter debería tener el método process_payment
        assert hasattr(adapter, 'process_payment')

        # El adapter puede ser usado donde se espera un PaymentProcessor
        result = adapter.process_payment("test", 100)
        assert result is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
