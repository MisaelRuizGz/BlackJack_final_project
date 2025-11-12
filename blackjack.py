


class BlackJackGame:
    def __init__(self,name):
        self.name = name



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
    def __init__ (self,name):
        self.name = name
    


def main():
    
    user_name = input('\nWhat is your name: ')

    prompt = f'\nWelcome {user_name} to BlackJack, are you ready to play ?\n' \
    '1. Yes, I want to play\n' \
    '2. No, Im done\n'\
    'Please enter 1 or 2 (or hit enter to end): '

    done:bool = False
    while not done:
        choice = input(prompt)
        match choice:
            case '' | '2':
                print('\nGoodbye, come again soon!\n')
                done =True
            case '1':
                blackjack()


if __name__ == '__main__':
    main()