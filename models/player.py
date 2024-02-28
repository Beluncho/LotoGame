class CPUPlayer:

    def __init__(self, name, card):
        self.name = name
        self.card = card
        # True - победитель, False - проигравший, None - еще играет
        self.is_winner = None

    def turn(self, number):
        if number in self.card:
            self.card.cross_out(number)
            # Комп всегда зачеркивает
            if self.card.is_empty():
                self.is_winner = True


class HumanPlayer(CPUPlayer):

    def turn(self, number):
        answer = input('Зачеркнуть? y/n')
        if answer == 'y':
            # Если число есть в карточке - зачеркиваем
            if number in self.card:
                self.card.cross_out(number)
                # Если он все зачеркнул, то он выиграл
                if self.card.is_empty():
                    self.is_winner = True
            else:
                # А если числа нет, то он проиграл
                self.is_winner = False
        else:
            # Это ответ нет
            # Если число есть в карточке - то он проиграл
            if number in self.card:
                self.is_winner = False
            # Если не зачеркнул то игра продолжается


def create_player(name, player_type, card):
    players = {
        '1': CPUPlayer,
        '0': HumanPlayer
    }

    player = players[player_type](name, card)
    return player
