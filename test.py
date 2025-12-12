import random 
from typing import Optional

class BlackJackGame:
# Display rules, handles betting, dealing, player and dealer turns

    # Constructor, initializes game state
    def __init__(self, user_name):
        self.user_name = user_name
        self.player: Optional['Player'] = None 
        self.deck: Optional['Deck'] = None      
        self.dealer: Optional['Player'] = None  
        self.bet = 0
        self.player = Player()
    
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

    # Displays hand and name, can hide first card for dealer
    @staticmethod
    def display_hand(hand, name="Player", hide_first=False):
        if hide_first:
            print(f"{name}: [Hidden] " + " ".join(hand[1:]))
        else:
            print(f"{name}: " + " ".join(hand))

    # Gets bet amount from player 
    def get_bet(self):
        while True:
            try:
                bet = int(input(f"Your balance: {self.player.balance}. Enter bet (1-{min(500, self.player.balance)}): "))
                if 1 <= bet <= min(500, self.player.balance):
                    self.bet = bet
                    break
                else:
                    print("Invalid bet.")
            except ValueError:
                print("Enter a number.")

    # Initial deal of two cards each to player and dealer
    def initial_deal(self):
        self.deck = Deck()
        self.player.hand = []
        self.dealer = Player()
        self.dealer.hand = []
        
        # Deal two cards each to player and dealer
        for _ in range(2):
            self.player.hand.append(self.deck.deal())
            self.dealer.hand.append(self.deck.deal())

    # Check for blackjacks 
    def check_blackjacks(self):
        player_val = self.calculate_value(self.player.hand)
        dealer_val = self.calculate_value(self.dealer.hand)
        
        player_blackjack = len(self.player.hand) == 2 and player_val == 21
        dealer_blackjack = len(self.dealer.hand) == 2 and dealer_val == 21
        
        # Show initial hands
        print(f"\nYour hand: {' '.join(self.player.hand)}")
        print(f"Value: {player_val}\n")
        print(f"Dealer hand: [Hidden] {self.dealer.hand[1]}")
        print("Value: ?\n")
        
        # handles dealer blackjack and player blackjack
        if dealer_blackjack:
            print(f"Dealer reveals: {' '.join(self.dealer.hand)}")
            print(f"Dealer Value: {dealer_val}\n")
            
            if player_blackjack:
                print("Both have Blackjack! It's a push!")
                return "push"
            else:
                print("Dealer has Blackjack! You lose!")
                self.player.balance -= self.bet
                return "dealer_blackjack"
        
        # Handle player blackjack
        elif player_blackjack:
            print(f"Dealer hand: {' '.join(self.dealer.hand)}")
            print(f"Value: {dealer_val}\n")
            print("Blackjack! You win 3:2!")
            winnings = int(self.bet * 1.5)
            self.player.balance += winnings
            print(f"You won {winnings} chips!")
            return "player_blackjack"
        
        return "continue"

    # Handle player's turn
    def player_turn(self):
        while self.calculate_value(self.player.hand) < 21:
            choice = input("Hit (h) or Stand (s)? ").lower()
            if choice == 'h':
                self.player.hand.append(self.deck.deal())
                print(f"\nYour hand: {' '.join(self.player.hand)}")
                print(f"Value: {self.calculate_value(self.player.hand)}\n")
                if self.calculate_value(self.player.hand) > 21:
                    print("Bust! You lose.")
                    self.player.balance -= self.bet
                    return "bust"
            elif choice == 's':
                break
            else:
                print("Invalid choice.")
        return "stand"
    
    #handle dealer's turn
    def dealer_turn(self):
        print(f"\nDealer hand: {' '.join(self.dealer.hand)}")
        print(f"Value: {self.calculate_value(self.dealer.hand)}\n")
        
        while self.calculate_value(self.dealer.hand) < 17:
            self.dealer.hand.append(self.deck.deal())
            print("Dealer hits")
            print(f"Dealer hand: {' '.join(self.dealer.hand)}")
            print(f"Value: {self.calculate_value(self.dealer.hand)}\n")
        
        return self.calculate_value(self.dealer.hand)

    # Determine winner and handle payouts
    def determine_winner(self, dealer_val):
        player_val = self.calculate_value(self.player.hand)
        
        # Determine outcome
        if dealer_val > 21:
            print("Dealer busts! You win!")
            winnings = int(self.bet * 1.5)
            self.player.balance += winnings
            print(f"You won {winnings} chips!")
                
        elif player_val > dealer_val:
            print("You win!")
            winnings = int(self.bet * 1.5)
            self.player.balance += winnings
            print(f"You won {winnings} chips!")
                
        elif player_val < dealer_val:
            print("Dealer wins!")
            self.player.balance -= self.bet
            print(f"You lost {self.bet} chips.")
        else:
            print("Push!")
            print("No chips exchanged.")

    # Play a single round of blackjack
    def play_round(self):
        self.get_bet()
        self.initial_deal()
        
        # Check for blackjacks
        blackjack_result = self.check_blackjacks()
        if blackjack_result != "continue":
            return  
        
        # Player's turn
        player_result = self.player_turn()
        if player_result == "bust":
            return 
        
        # Dealer's turn
        dealer_val = self.dealer_turn()
        
        # Determine winner
        self.determine_winner(dealer_val)

    def game(self):
        # Main game loop
        print(f"Welcome {self.user_name}! You start with {self.player.balance} chips.")
        
        while True:
            if self.player.balance < 1:
                print("You're out of chips!")
                break
            
            self.play_round()
            
            again = input("Play again? (y/n): ").lower()
            if again != 'y':
                break
        
        print(f"Final balance: {self.player.balance}\n")

# player class to manage player state
class Player:
    def __init__(self, balance=1000):
        self.balance = balance
        self.hand = []

# deck class to manage the deck of cards
class Deck:
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['♠︎' , '♥︎' , '♦︎' , '♣︎']

    def __init__(self):
        self.mixed_deck = []
        for _ in range(6):
            self.mixed_deck.extend([card + ' ' + suit for card in self.cards for suit in self.suits])
        random.shuffle(self.mixed_deck)

    def deal(self):
        return self.mixed_deck.pop()

# Main function to start the game
def main():
    prompt = '''\nWelcome to Misael's online casino, would you like to play BlackJack ?\n''' \
    '1. Yes\n' \
    '2. No \n'\
    'Please enter 1 or 2 (or hit enter to end): '

    done: bool = False
    while not done:
        choice = input(prompt)
        match choice:
            case '' | '2':
                print('\nGoodbye, come again soon!\n')
                done = True
            case '1':
                user_name = input('\nOkay lets get started that, what is your name: ')
                print(f"\nOkay {user_name}, The rules of BlackJack are simple")
                BlackJackGame.rules()
                game = BlackJackGame(user_name)
                game.game()
                done = True


if __name__ == '__main__':
    main()