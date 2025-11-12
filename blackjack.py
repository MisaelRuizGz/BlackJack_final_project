


class BlackJackGame:
    def __init__(self,name):
        self.name = name



class Cards:
    def __init__ (self,name):
        self.name = name

'''manages the players hand'''
class Player:
    def __init__ (self,name):
        self.name = name

'''needs a shuffled list of cards'''
class Deck:
    def __init__ (self,name):
        self.name = name
    


def main():
    done: bool = False
    name = input('What is your name:')

    prompt = '\nWelcome to BlackJack, are you ready to play ?\n' \
    '1. Yes, I want to play\n' \
    '2. No, Im done\n'\
    'Please enter 1 or 2 (or hit enter to end)\n'

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                print('Goodbye, come again soon')
                done =True
            case '1':
                blackjack()
            case '2':
                print('Goodbye, come again soon')
                done = True

            



    


if __name__ == '__main__':
    main()