import random 

class BlackJackGame:

    # Display rules
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

    # Calculates the hand value
    @staticmethod
    def calculate_value(hand):
        value = sum(BlackJackGame.get_value(card) for card in hand)
        aces = sum(1 for card in hand if card.startswith('A '))
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    # Gets card value, helper for calculate_value
    @staticmethod
    def get_value(card):
        rank = card.split()[0]
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)

    # Displays hand
    @staticmethod
    def display_hand(hand, name="Player", hide_first=False):
        if hide_first:
            print(f"{name}: [Hidden] " + " ".join(hand[1:]))
        else:
            print(f"{name}: " + " ".join(hand))

    # Main game loop, handles betting, dealing, player and dealer turns
    def game(self, user_name):
        player = Player()
        print(f"Welcome {user_name}! You start with {player.balance} chips.")
        while True:
            if player.balance < 1:
                print("You're out of chips!")
                break
            deck = Deck()
            player.hand = []
            dealer = Player()  
            dealer.hand = []
           
           # Place bet
            while True:
                try:
                    bet = int(input(f"Your balance: {player.balance}. Enter bet (1-{min(500, player.balance)}): "))
                    if 1 <= bet <= min(500, player.balance):
                        break
                    else:
                        print("Invalid bet.")
                except ValueError:
                    print("Enter a number.")

            # Initial deal
            player.hand.append(deck.deal())
            dealer.hand.append(deck.deal())
            player.hand.append(deck.deal())
            dealer.hand.append(deck.deal())
           
           # Show initial hands
            print(f"\nYour hand: {' '.join(player.hand)}")
            print(f"Value: {BlackJackGame.calculate_value(player.hand)}\n")

            print(f"Dealer hand: {' '.join(dealer.hand)}")
            print(f"Value: {BlackJackGame.calculate_value(dealer.hand)}\n")

            # Player's turn
            while BlackJackGame.calculate_value(player.hand) < 21:
                choice = input("Hit (h) or Stand (s)? ").lower()
                if choice == 'h':
                    player.hand.append(deck.deal())
                    print(f"\nYour hand: {' '.join(player.hand)}")
                    print(f"Value: {BlackJackGame.calculate_value(player.hand)}\n")
                    if BlackJackGame.calculate_value(player.hand) > 21:
                        print("Bust! You lose.")
                        player.balance -= bet
                        break
                elif choice == 's':
                    break
                else:
                    print("Invalid choice.")
            else:
            
                if len(player.hand) == 2 and BlackJackGame.calculate_value(player.hand) == 21:
                    print("Blackjack! You win 3:2!")
                    player.balance += int(bet * 1.5)
                    continue

                # Dealer's turn, only if player hasn't busted
            if BlackJackGame.calculate_value(player.hand) > 21:
                pass  
            else:
                
                print(f"\nDealer hand: {' '.join(dealer.hand)}")
                print(f"Value: {BlackJackGame.calculate_value(dealer.hand)}\n")
                while BlackJackGame.calculate_value(dealer.hand) < 17:
                    dealer.hand.append(deck.deal())
                    print("Dealer hits")
                    print(f"Dealer hand: {' '.join(dealer.hand)}")
                    print(f"Value: {BlackJackGame.calculate_value(dealer.hand)}\n")
                dealer_val = BlackJackGame.calculate_value(dealer.hand)
                if dealer_val > 21:
                    print("Dealer busts! You win!")
                    player.balance += int(bet * 1.5)
                else:
                    player_val = BlackJackGame.calculate_value(player.hand)
                    if player_val > dealer_val:
                        print("You win!")
                        player.balance += int(bet * 1.5)
                    elif player_val < dealer_val:
                        print("Dealer wins!")
                        player.balance -= bet
                    else:
                        print("Push!")
           
            again = input("Play again? (y/n): ").lower()
            if again != 'y':
                break
        print(f"Final balance: {player.balance}\n")


class Player:

    def __init__(self, balance=1000):
        self.balance = balance
        self.hand = []







class Deck:

    #  Cards and their suits, need to figure out how to combine and only have one of each'''
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['♠︎' , '♥︎' , '♦︎' , '♣︎']

    def __init__(self):
        self.mixed_deck = []
        for _ in range(6):
            self.mixed_deck.extend([card + ' ' + suit for card in self.cards for suit in self.suits])
        random.shuffle(self.mixed_deck)

    def deal(self):
        return self.mixed_deck.pop()

 

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
                BlackJackGame().game(user_name)

                done =True

                


if __name__ == '__main__':
    main()