


class BlackJackGame:

    @staticmethod
    def rules():
        print('\nBlackJack Rules: \n' \
        '1. Get as close to 21 as possible without going over\n' \
        '2. J , Q , K cards are worth 10 points\n' \
        '3. Aces can be worth 1 or 11 points\n' \
        '4. Dealer must hit until their cards total 17 or higher\n' \
        '5. If you go over 21, you bust and lose the game\n' \
        '6. If you and the dealer have the same total, it is a push (tie)\n'
        )

    def game(user_name):

        return


class Cards:
    '''
    2-10 are worth their face value
    J , Q , K are worth 10 
    Aces can be 1 or 11, depending on which benefits the player, 
    '''
    def __init__ (self,name):
        
        self.name = name

'''manages the players hand'''
class Player:
    def __init__ (self,name):
        self.name = name

'''needs a shuffled list of cards, contains 52 cards '''
class Deck:
    ''' Cards and their suits, need to figure out how to 
    combine and only have one of each'''

    cards = ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','J ','Q ','K ','A ']
    suits = ['♠︎' , '♥︎' , '♦︎' , '♣︎']

    ''' creates a place for the mixed cards to go after sorting'''
    mixed_deck = []

    '''sorts the cards into '''
    for card in cards:
        for suit in suits:
            temp_card_hold = (card + suit)
            mixed_deck.append(temp_card_hold)


    ''' 
    This is for testing to make sure i have all 52 cards 
    
    for i in range(0, len(mixed_deck), 4):
        print(*mixed_deck[i:i+4])

    print(len(mixed_deck))

    '''

''' add betting functionality '''
def main():
    
   

    prompt = f'''\nWelcome to Misael's online casino, would you like to play BlackJack ?\n''' \
    '1. Yes, I want to play\n' \
    '2. No\n'\
    'Please enter 1 or 2 (or hit enter to end): '

    done:bool = False
    while not done:
        choice = input(prompt)
        match choice:
            case '' | '2':
                print('\nGoodbye, come again soon!\n')
                done =True
            case '1':
                user_name = input('\nOkay lets get started that, what is your name: ')
                print(f"\nOkay {user_name} the rules of BlackJack are simple")
                BlackJackGame.rules()
                BlackJackGame.game(user_name)

                done =True

                


if __name__ == '__main__':
    main()