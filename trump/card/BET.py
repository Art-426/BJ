class Bet:
    # bet時　入力が正しいか判定
    def bet_chip(pos):
        while True:
            bet = input(f'現在の所持枚数{pos}枚 >>> ')
            if bet.isnumeric():
                bet = int(bet)
                if bet == 0:
                    print('チップを賭けてください')
                    continue
                elif bet <= pos:
                    break
                else:
                    print('所持チップより多い枚数は賭けられません')
                    continue
            else:
                print('正しい数値を入力してください')
                continue
        return bet
