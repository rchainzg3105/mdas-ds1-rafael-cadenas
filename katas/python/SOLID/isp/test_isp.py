"""
Tests para el principio ISP (Interface Segregation Principle)
Valida tanto las implementaciones malas como las buenas
"""

import pytest
from isp_bad import Robot as RobotBad, Human as HumanBad
from isp_good import Robot as RobotGood, Human as HumanGood


class TestISPBad:
    """Tests para la implementación que viola ISP"""

    def test_human_work(self):
        """Verifica que los humanos pueden trabajar"""
        human = HumanBad("Juan")
        assert human.work() == "Juan está trabajando"

    def test_human_eat(self):
        """Verifica que los humanos pueden comer"""
        human = HumanBad("Juan")
        assert human.eat() == "Juan está comiendo"

    def test_robot_work(self):
        """Verifica que los robots pueden trabajar"""
        robot = RobotBad("R2D2")
        assert robot.work() == "R2D2 está trabajando"

    def test_robot_eat_violation(self):
        """Demuestra la violación de ISP: Robot debe implementar eat() pero no lo necesita"""
        robot = RobotBad("R2D2")
        # Robot se ve forzado a implementar eat() aunque no tiene sentido
        with pytest.raises(NotImplementedError):
            robot.eat()


class TestISPGood:
    """Tests para la implementación que cumple con ISP"""

    def test_human_work(self):
        """Verifica que los humanos pueden trabajar"""
        human = HumanGood("Juan")
        assert human.work() == "Juan está trabajando"

    def test_human_eat(self):
        """Verifica que los humanos pueden comer"""
        human = HumanGood("Juan")
        assert human.eat() == "Juan está comiendo"

    def test_robot_work(self):
        """Verifica que los robots pueden trabajar"""
        robot = RobotGood("R2D2")
        assert robot.work() == "R2D2 está trabajando"

    def test_interface_segregation(self):
        """Verifica que las interfaces están correctamente segregadas"""
        human = HumanGood("Juan")
        robot = RobotGood("R2D2")

        # Human implementa ambas interfaces
        assert hasattr(human, 'work')
        assert hasattr(human, 'eat')

        # Robot solo implementa la interfaz de trabajo
        assert hasattr(robot, 'work')
        # Robot NO tiene método eat() - cumple ISP
        assert not hasattr(robot, 'eat')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
