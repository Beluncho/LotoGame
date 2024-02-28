from pytest import raises
from card import Card, CardNumber, CardNotContainsNumberError


class TestCardNumber:

    def setup(self):
        self.number = CardNumber(3)
        self.other = CardNumber(4)

    def test_str(self):
        assert str(self.number) == '3'
        self.number.is_cross_out = True
        assert str(self.number) == '-'

    def test_gt_lt(self):
        assert self.other > self.number
        assert self.number < self.other

    def test_eq(self):
        eq_number = CardNumber(3)
        assert eq_number == self.number
        assert self.other != self.number


class TestCard:

    def setup(self):
        self.numbers_list = [9, 43, 62, 74, 90, 2, 27, 75, 78, 82, 41, 56, 63, 76, 86]
        self.card = Card(self.numbers_list)

    def test_is_empty(self):
        assert not self.card.is_empty()
        # Если вычеркнуть все чифры?
        for item in self.numbers_list:
            self.card.cross_out(item)

        assert self.card.is_empty()

    def test_str(self):
        result = """
        --------------------------
            9 43 62          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert result == str(self.card)

    def test_contains(self):
        assert 9 in self.card
        assert 99 not in self.card
        assert CardNumber(9) in self.card
        assert CardNumber(99) not in self.card

    def test_cross_out(self):
        # Зачеркиваем число которое есть
        self.card.cross_out(43)
        result = """
        --------------------------
            9 - 62          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert str(self.card) == result

        self.card.cross_out(CardNumber(62))
        result = """
        --------------------------
            9 - -          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert str(self.card) == result

        # В карточке нет такого числа
        with raises(CardNotContainsNumberError):
            self.card.cross_out(CardNumber(99))
