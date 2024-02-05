from average_calculator import AverageCalculator

def test_calculate_average():
    calculator = AverageCalculator()
    assert calculator.calculate_average([1, 2, 3]) == 2.0
    assert calculator.calculate_average([]) == 0
    assert calculator.calculate_average([-1, 1]) == 0.0

def test_compare_averages():
    calculator = AverageCalculator()
    assert calculator.compare_averages([1, 2, 3], [4, 5, 6]) == "Второй список имеет большее среднее значение"
    assert calculator.compare_averages([1, 2, 3], [1, 2, 3]) == "Средние значения равны"
    assert calculator.compare_averages([1, 2, 3], [0, 0, 0]) == "Первый список имеет большее среднее значение"