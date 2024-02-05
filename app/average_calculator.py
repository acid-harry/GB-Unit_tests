class AverageCalculator:
    """
    Класс для вычисления среднего значения чисел и сравнения средних значений двух списков.
    """

    def calculate_average(self, numbers):
        """
        Рассчитывает среднее значение чисел.

        :param numbers: Список чисел.
        :return: Среднее значение чисел.
        """
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1, list2):
        """
        Сравнивает средние значения двух списков и возвращает соответствующее сообщение.

        :param list1: Первый список чисел.
        :param list2: Второй список чисел.
        :return: Сообщение о сравнении средних значений.
        """
        avg1 = self.calculate_average(list1)
        avg2 = self.calculate_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"