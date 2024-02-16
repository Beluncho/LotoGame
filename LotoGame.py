from game import Game_u_vs_c, Game_u_vs_u, Game_c_vs_c

if __name__ == '__main__':
    game = Game_u_vs_c()
    game2 = Game_u_vs_u()
    game3 = Game_c_vs_c()
    loto = None

    print('Кто будет играть?')
    print('1. user vs comp?')
    print('2. user1 vs user2?')
    print('3. comp vs comp?')
    answer = input('Ответ: ')

    while True:

        if answer == '1':
            loto = game.round_game()

            if loto == 1:
                print('You win!')
                break
            elif loto == 2:
                print('You lose!')
                break
        elif answer == '2':
            loto = game2.round_game()

            if loto == 1:
                print('Win user 1!')
                break
            elif loto == 2:
                print('Win user 2!')
                break

        elif answer == '3':
            loto = game3.round_game()

            if loto == 1:
                print('Win comp1')
                break
            elif loto == 2:
                print('Win comp2')
                break
