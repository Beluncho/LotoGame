
from random import randint


def random_keg(round, min_keg, max_keg):
    if round > max_keg - min_keg + 1:
        raise ValueError('Incorrect input parameters')
    ret = []
    while len(ret) < round:
        new = randint(min_keg, max_keg)
        if new not in ret:
            ret.append(new)

    return ret


class Card:
    __line = 3
    __cell = 9
    __cell_num = 5
    __emptynum = 0
    __crossednum = -1
    __data = None

    def __init__(self):
        uniques_num = self.__line * self.__cell_num
        uniques = random_keg(uniques_num, 1, 90)

        self.__data = []
        for i in range(0, self.__line):
            line = sorted(uniques[self.__cell_num * i: self.__cell_num * (i+1)])

            empty_nums_count = self.__cell - self.__cell_num
            for j in range(0, empty_nums_count):
                index = randint(0, len(line))
                line.insert(index, self.__emptynum)
            self.__data += line

    def __str__(self):
        delimiter = '-' * 30
        ret = delimiter + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__emptynum:
                ret += '  '
            elif num == self.__crossednum:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)
            if (index + 1) % self.__cell == 0:
                ret += '\n'
            else:
                ret += ' '
        return ret + delimiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossednum
                return
        raise ValueError(f'number not in card: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__emptynum, self.__crossednum}


class Game_u_vs_c:
    __user_card = None
    __comp_card = None
    __keg_in_game = 90
    __keg = []
    __game_over = None

    def __init__(self):
        self.__user_card = Card()
        self.__comp_card = Card()
        self.__keg = random_keg(self.__keg_in_game, 1, 90)

    def round_game(self):
        keg = self.__keg.pop()
        print(f'Играем боченок под номером: {keg} (осталось {len(self.__keg)} боченков ')
        print(f'-----Игрок-----\n{self.__user_card}')
        print(f'-----Comp------\n{self.__comp_card}')

        answer = input('Зачеркнуть цифру? (y/n)').lower().strip()  #убираем возможную ошибку ответа по регистру и
                                                                    # - и использование пробеловв.
        if answer == 'y' and not keg in self.__user_card or \
           answer != 'y' and keg in self.__user_card:

            return 2

        if keg in self.__user_card:
            self.__user_card.cross_num(keg)
            if self.__user_card.closed():
                return 1

        if keg in self.__comp_card:
            self.__comp_card.cross_num(keg)
            if self.__comp_card.closed():
                return 2

        return 0


class Game_u_vs_u:
    __user_card1 = None
    __user_card2 = None
    __keg_in_game = 90
    __keg = []
    __game_over = None

    def __init__(self):
        self.__user_card1 = Card()
        self.__user_card2 = Card()
        self.__keg = random_keg(self.__keg_in_game, 1, 90)

    def round_game(self):
        keg = self.__keg.pop()
        print(f'Играем боченок под номером: {keg} (осталось {len(self.__keg)} боченков ')
        print(f'-----Игрок1-----\n{self.__user_card1}')
        print(f'-----Игрок2------\n{self.__user_card2}')

        answer1 = input('Игрок1. Зачеркнуть цифру? (y/n)').lower().strip()  #убираем возможную ошибку ответа по регистру и
                                                                    # - и использование пробеловв.

        if answer1 == 'y' and not keg in self.__user_card1 or \
           answer1 != 'y' and keg in self.__user_card1:

            return 2

        answer2 = input('Игрок2. Зачеркнуть цифру? (y/n)').lower().strip()

        if answer2 == 'y' and not keg in self.__user_card2 or \
           answer2 != 'y' and keg in self.__user_card2:

            return 1

        if keg in self.__user_card1:
            self.__user_card1.cross_num(keg)
            if self.__user_card1.closed():
                return 1

        if keg in self.__user_card2:
            self.__user_card2.cross_num(keg)
            if self.__user_card2.closed():
                return 2

        return 0


class Game_c_vs_c:
    __comp_card1 = None
    __comp_card2 = None
    __keg_in_game = 90
    __keg = []
    __game_over = None

    def __init__(self):
        self.__comp_card1 = Card()
        self.__comp_card2 = Card()
        self.__keg = random_keg(self.__keg_in_game, 1, 90)

    def round_game(self):
        keg = self.__keg.pop()
        print(f'Играем боченок под номером: {keg} (осталось {len(self.__keg)} боченков ')
        print(f'-----Comp1-----\n{self.__comp_card1}')
        print(f'-----Comp2------\n{self.__comp_card2}')



        if keg in self.__comp_card1:
            self.__comp_card1.cross_num(keg)
            if self.__comp_card1.closed():
                return 1

        if keg in self.__comp_card2:
            self.__comp_card2.cross_num(keg)
            if self.__comp_card2.closed():
                return 2

        return 0
=======
from models.bag import Bag
from models.card import Card
from models.player import create_player


def is_continue_game(players):
    for item in players:
        if not (item.is_winner is None):
            return False
    return True


# создаем мешок
bag = Bag(90)
player_count = int(input('Введите количество игроков'))
# Создаем игроков и даем им карточки
players = []
for i in range(player_count):
    # Имя игрока
    name = input(f'Введите имя игрока {i + 1}')
    # Тип игрока
    player_type = input(f'Введите тип игрока CPU - 1, Human - 0')
    # Карточка
    card = Card(bag.get_random_numbers(15))
    # создаем игрока
    player = create_player(name, player_type, card)
    players.append(player)

# Играем пока кто нибудь не выиграт и не проиграет, это значит что у всех is_winner = None
while is_continue_game(players):
    # Цикл игры
    # У каждого игрока рисуем карточку и он делает ход
    # из мешка нужен номер
    number = bag.get_next_number()
    print(f'Следующий Номер: {number}')
    for player in players:
        # Рисуем карточку
        # print(player.card)
        print(f'Карточка игрока {player.name}')
        #player.card.show_numbers()
        print(player.card)
        player.turn(number)

# Объявляем победителей и проигравших ?
# Что будет если 1 выиграл, другой проиграл?
# Несколько проиграть
# Несколько выиграть
# Может 1 проиграть, дургой выиграть
# Кто то проиграть а кто то играет

# Проверим победителей
has_winner = False
has_looser = False
for player in players:
    if player.is_winner is None:
        pass
    else:
        if player.is_winner:
            has_winner = True
        else:
            has_looser = True

# Выводим результат
# Все оставшиеся будут проигравшими если has_winner
if has_winner:
    for player in players:
        if player.is_winner:
            print(player.name, 'Win!')
        else:
            print(player.name, 'Loose!')
elif has_looser:
    # Есть проигравший
    for player in players:
        if player.is_winner is None:
            print(player.name, 'Win!')
        else:
            print(player.name, 'Loose!')
else:
    print('Что то пошло не так')

