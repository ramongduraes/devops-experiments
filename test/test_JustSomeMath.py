from complexoperations.JustSomeMath import JustSomeMath


class TestJustSomeMath:

    def test1(self):
        # Arrange
        complexop = JustSomeMath()
        number = 1

        sem_uso = 0
        # Act
        result = complexop.operate(number)

        # Assert
        assert result > 0

        pass
