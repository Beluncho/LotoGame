class CardNumber:

    def __init__(self, number):
        self.number = number
        self.is_cross_out = False

    def __str__(self):
        return '-' if self.is_cross_out else str(self.number)

    def __gt__(self, other):
        return self.number > other.number

    def __eq__(self, other):
        return self.number == other.number


class CardNotContainsNumberError(ValueError):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'В карточке нет числа {self.number}'


class Card:

    def __init__(self, numbers):
        """
        :param numbers: 15 чисел
        """
        numbers = [CardNumber(item) for item in numbers]
        self.numbers = numbers

    # def show_numbers(self):
    #     for number in self.numbers:
    #         print(number)

    def __str__(self):
        row1 = sorted(self.numbers[:5])
        row2 = sorted(self.numbers[5:10])
        row3 = sorted(self.numbers[10:])
        result = f"""
        --------------------------
            {row1[0]} {row1[1]} {row1[2]}          {row1[3]} {row1[4]}
         {row2[0]}    {row2[1]}    {row2[2]} {row2[3]}    {row2[4]}
           {row3[0]} {row3[1]} {row3[2]}     {row3[3]}      {row3[4]}
        --------------------------
        """
        return result

    def is_empty(self):
        for item in self.numbers:
            if not item.is_cross_out:
                return False
        return True

    def __contains__(self, item):
        if isinstance(item, int):
            item = CardNumber(item)
        return item in self.numbers

    def cross_out(self, number):
        # self.numbers = []
        if isinstance(number, int):
            number = CardNumber(number)
        try:
            index = self.numbers.index(number)
        except ValueError:
            raise CardNotContainsNumberError(number)
        else:
            self.numbers[index].is_cross_out = True
