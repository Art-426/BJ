import random
# トランプ52枚の生成
class Card:
    SUITS = ['♠️',  '❤️', '♦︎', '♣️']
    SUITS_white = ['♤', '♡', '♢', '♧']
    NUMBERS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  

    def make_card():
        return [Card.SUITS[s] + Card.NUMBERS[n] for s in range(4) for n in range(13)]
    
    def make_card_white():
        return [Card.SUITS_white[s] + Card.NUMBERS[n] for s in range(4) for n in range(13)]
    
    def change_num():
        return

    def make_jokcer():
        return 

class DeckAction:
    def shuffle(card):
        return random.sample(card, len(card))
    
    def draw_check():
        print('カードを引きますか？ Yes or No')
        draw_flag = False
        while True:
            ans = input('Y or N >>> ')
            if ans == 'y' or ans == 'Y':
                draw_flag = True
                return draw_flag
            elif ans == 'n' or ans == 'N':
                draw_flag = False
                return draw_flag



    def draw(deck):
        draw_card = deck.pop(0)
        return draw_card

class Game:
    def next_game(chips):
        if chips <= 0:
            game_flag = False
            print('チップがなくなったため終了します')
        else:
            print('続けますか？ Yes or No')
            while True:
                next_game = input('Y or N >>> ')
                if next_game == 'y' or next_game == 'Y':
                    print('次のゲームが始まります')
                    game_flag = True
                    return game_flag
                elif next_game == 'n' or next_game == 'N':
                    print('ゲームを終了します')
                    game_flag = False
                    return game_flag
