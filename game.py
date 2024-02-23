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