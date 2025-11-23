"""
Tests para el principio LSP (Liskov Substitution Principle)
Valida tanto las implementaciones malas como las buenas
"""

import pytest
from lsp_bad import Rectangle as RectangleBad, Square as SquareBad
from lsp_good import Rectangle as RectangleGood, Square as SquareGood


class TestLSPBad:
    """Tests para la implementación que viola LSP"""

    def test_rectangle_area(self):
        """Verifica el cálculo del área de un rectángulo"""
        rect = RectangleBad(5, 4)
        assert rect.get_area() == 20

    def test_square_area(self):
        """Verifica el cálculo del área de un cuadrado"""
        square = SquareBad(5)
        assert square.get_area() == 25

    def test_lsp_violation(self):
        """Demuestra la violación de LSP: Square no puede sustituir a Rectangle"""
        # Con Rectangle funciona como se espera
        rect = RectangleBad(5, 4)
        rect.set_width(3)
        assert rect.get_area() == 12  # 3 * 4

        # Con Square el comportamiento es inesperado
        square = SquareBad(5)
        square.set_width(3)
        # Al cambiar el ancho, también cambia el alto (violación de LSP)
        assert square.get_area() == 9  # 3 * 3, no 3 * 5


class TestLSPGood:
    """Tests para la implementación que cumple con LSP"""

    def test_rectangle_area(self):
        """Verifica el cálculo del área de un rectángulo"""
        rect = RectangleGood(5, 4)
        assert rect.get_area() == 20

    def test_rectangle_modification(self):
        """Verifica la modificación independiente de dimensiones"""
        rect = RectangleGood(5, 4)
        rect.set_width(3)
        rect.set_height(6)
        assert rect.get_area() == 18

    def test_square_area(self):
        """Verifica el cálculo del área de un cuadrado"""
        square = SquareGood(5)
        assert square.get_area() == 25

    def test_square_set_side(self):
        """Verifica el cambio de lado del cuadrado"""
        square = SquareGood(5)
        square.set_side(7)
        assert square.get_area() == 49

    def test_lsp_compliance(self):
        """Verifica que las clases cumplen con LSP mediante polimorfismo"""
        from lsp_good import Shape

        shapes = [
            RectangleGood(5, 4),
            SquareGood(5)
        ]

        # Todas las formas pueden calcular su área
        areas = [shape.get_area() for shape in shapes]
        assert areas == [20, 25]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
