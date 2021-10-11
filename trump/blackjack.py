from card.Trump import Card as c, DeckAction as d, Game as g
from card.BET import Bet as b

# BJ　持ち点計算
def point_check(hands):
    sum_point = 0
    for i in hands:
        point = i[-1]
        if point == 'J' or point == 'Q' or point =='K' or point == '0':
            sum_point += 10
        elif point == 'A':
            if sum_point > 10:
                sum_point += 1
            else:
                sum_point += 11
        else:
            sum_point += int(point)
        
        if sum_point > 21 and 'A' in player:
            sum_point -= 10

    return sum_point

# burst_check
def burst_check(point):
    if point > 21:
        print('BURST')
        return True
    else:
        return False

# ゲーム開始
game_flag = True    
chips = 100
return_chip = 0
bet_chip = 0
p_burst, d_burst = False, False
p_bj, d_bj = False, False
doubledown = False

while game_flag:
    bet_chip = b.bet_chip(chips)
    chips -= bet_chip
    # カードを作りシャッフル
    card = c.make_card_white()
    deck = d.shuffle(card)
    dealer = []
    player = []

    for i in range(2):
        dealer.append(d.draw(deck))
        player.append(d.draw(deck))

    print('OPEN_HANDS')
    player_p = point_check(player)
    print('dealer_hands', dealer[0], ' * ')
    print('player_hands', player, '>', player_p)

    input('PLEASE ENTER >>> ')
    # player turn
    if player_p == 21:
        print('BLACK JACK!!')
        print(player, point_check(player))

    else:
        print('doubledoWn')
        dd = input('Y or N')
        if dd == 'Y' or dd == 'y':
            doubledown = True
        while not p_burst:
            if doubledown:
                print('DOUBLE DOWN')
                chips -= bet_chip
                bet_chip *= 2
                player.append(d.draw(deck))
                print(player[-1])

            if player_p < 21 and not doubledown:
                draw_flag = d.draw_check()
            else:
                draw_flag = False
            
            if draw_flag:
                print('HIT')
                player.append(d.draw(deck))
                print(player[-1])
            elif doubledown:
                print()
            else:
                print('STAND')
                break

            player_p = point_check(player)
            print(player, '>', player_p)
            
            p_burst = burst_check(player_p)

            if doubledown:
                break

    input('PLEASE ENTER >>> ')
    # dealer　turn
    print('OPEN')
    dealer_p = point_check(dealer)
    print(dealer, dealer_p)

    if dealer_p == 21:
        print('BLACK JACK!!')

    while True: 
        if dealer_p < 17:
            print('HIT')
            dealer.append(d.draw(deck))
            print(dealer[-1])
        else:
            print('STAND')
            break
        dealer_p = point_check(dealer)
        print(dealer, dealer_p)
    if dealer_p > 21:
        print('BURST!!')
        d_burst = True

    input('PLEASE ENTER >>> ')

    print('player', player, player_p)
    print('dealer', dealer, dealer_p)

    if player_p < dealer_p <= 21 or (p_burst and not d_burst):
        print('dealer_win')
    elif dealer_p < player_p <= 21 or (d_burst and not p_burst):
        print('player_win')
        chips += bet_chip * 2
    else:
        print('draw')
    
    print(chips)

    game_flag = g.next_game(chips)
    input('PLEASE ENTER >>> ')
