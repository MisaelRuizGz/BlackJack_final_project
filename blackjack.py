


class BlackJackGame:

    @staticmethod
    def rules():
        print("""
    Objective:
        Get your hand as close to 21 as possible without going over.

    Card Values:
        - Number cards (2–10): Face value
        - J, Q, K: 10 points each
        - Ace (A): Counts as 1 or 11, whichever is better for the hand

    Dealer Rules:
        - The dealer must hit until their total is 17 or higher.

    Bust:
        - If your total goes over 21, you bust and automatically lose.

    Push (Tie):
        - If you and the dealer have the same total, it's a push (tie).

    Betting:
        - You may bet up to 500 chips per round.
        - Winning pays 3:2 (Example: bet 100 → win 150).
    """
)


    def game(self, user_name):
    


        return


class Cards:
    # 2-10 are worth their face value 
    # J , Q , K are worth 10 Aces can be 1 or 11, depending on which benefits the player

    def __init__ (self,name):
        
        self.name = name
class Player:





    def __init__ (self,name):
        self.name = name


class Deck:

    #  Cards and their suits, need to figure out how to combine and only have one of each'''
    cards = ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','J ','Q ','K ','A ']
    suits = ['♠︎' , '♥︎' , '♦︎' , '♣︎']

    #  creates a place for the mixed cards to go after sorting
    mixed_deck = []

    #  sorts the cards into 
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

class Betting():

    def chips():
        return 


def main():
    prompt = f'''\nWelcome to Misael's online casino, would you like to play BlackJack ?\n''' \
    '1. Yes\n' \
    '2. No \n'\
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
                print(f"*\n*\n*\n*\nOkay {user_name}, The rules of BlackJack are simple")
                BlackJackGame.rules()
                BlackJackGame.game(user_name)
                done =True

                


if __name__ == '__main__':
    main()