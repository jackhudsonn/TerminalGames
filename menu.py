from Tools import *


class BlackJack:
    class Deck:
        def __init__(self):
            self.cards = {"Ace of Spades": 11, "Two of Spades": 2, "Three of Spades": 3, "Four of Spades": 4,
                          "Five of Spades": 5,
                          "Six of Spades": 6, "Seven of Spades": 7, "Eight of Spades": 8, "Nine of Spades": 9,
                          "Ten of Spades": 10,
                          "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10,
                          "Ace of Clubs": 11, "Two of Clubs": 2, "Three of Clubs": 3, "Four of Clubs": 4,
                          "Five of Clubs": 5,
                          "Six of Clubs": 6, "Seven of Clubs": 7, "Eight of Clubs": 8, "Nine of Clubs": 9,
                          "Ten of Clubs": 10,
                          "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10,
                          "Ace of Diamonds": 11, "Two of Diamonds": 2, "Three of Diamonds": 3, "Four of Diamonds": 4,
                          "Five of Diamonds": 5, "Six of Diamonds": 6, "Seven of Diamonds": 7, "Eight of Diamonds": 8,
                          "Nine of Diamonds": 9, "Ten of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10,
                          "King of Diamonds": 10,
                          "Ace of Hearts": 11, "Two of Hearts": 2, "Three of Hearts": 3, "Four of Hearts": 4,
                          "Five of Hearts": 5,
                          "Six of Hearts": 6, "Seven of Hearts": 7, "Eight of Hearts": 8, "Nine of Hearts": 9,
                          "Ten of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10}
            self.removed_cards = {}
            self.size = 52

        def getCards(self):
            return self.cards

        def getRemovedCards(self):
            return self.removed_cards

        def remove(self, card) -> None:
            self.size -= 1
            self.removed_cards[card] = self.cards.get(card)
            try:
                self.cards.pop(card)
            except ValueError:
                raise f"The {card} is not in the deck"

        def resetDeck(self) -> None:
            self.cards.update(self.removed_cards)
            self.size = 52

    def __init__(self):
        self.deck = self.Deck()
        self.dealer_hand = []
        self.dealer_number_of_aces = 0
        self.player_hand = []
        self.player_number_of_aces = 0

        card = self.drawCard(self.dealer_hand, self.deck)
        if card[:3] == "Ace":
            self.dealer_number_of_aces += 1
        card = self.drawCard(self.dealer_hand, self.deck)
        if card[:3] == "Ace":
            self.dealer_number_of_aces += 1

        card = self.drawCard(self.player_hand, self.deck)
        if card[:3] == "Ace":
            self.player_number_of_aces += 1
        card = self.drawCard(self.player_hand, self.deck)
        if card[:3] == "Ace":
            self.player_number_of_aces += 1

    def drawCard(self, hand, deck) -> str:
        card = random.choice(list(self.deck.getCards()))
        hand.append(card)
        deck.remove(card)

        return card

    def displayHand(self, hand, player_turn) -> None:
        if player_turn:
            name = "PLAYER"
        else:
            name = "DEALER"

        print(f"{name} CARDS:")
        for card in hand:
            print(card)

    def displayWinner(self, player_total, dealer_total):
        if player_total > 21:
            print("PLAYER BUST, DEALER WINS!")
        elif dealer_total > 21:
            print("DEALER BUST, PLAYER WINS!")
        elif dealer_total > player_total:
            print(f"{dealer_total} IS GREATER THAN {player_total}, DEALER WINS!")
        elif dealer_total < player_total:
            print(f"{player_total} IS GREATER THAN {dealer_total}, DEALER WINS!")
        elif dealer_total == player_total:
            print(f"BOTH PLAYER AND DEALER HAD {dealer_total} POINTS, TIE!")
        print()

    def hitOrStand(self) -> str:
        print("WOULD YOU LIKE TO HIT OR STAND? (h/s)")
        choice = input().lower()
        while choice != 'h' and choice != 's':
            print("PLEASE ENTER AN 'h' OR AN 's':")
            choice = input()
        return choice

    def playerTurn(self, player_turn, player_total):
        if player_turn:
            user_choice = self.hitOrStand()
            while user_choice == 'h' and player_total < 21:
                self.drawCard(self.player_hand, self.deck)
                self.displayHand(self.player_hand, player_turn)
                player_total = self.getTotal(self.player_hand, player_turn)
                print(f"\nYOUR TOTAL IS {player_total}\n")
                if player_total < 21:
                    user_choice = self.hitOrStand()
        else:
            print("IT IS NOT THE PLAYER'S TURN")

    def dealerTurn(self, player_turn, dealer_total) -> int:
        if not player_turn:
            self.displayHand(self.dealer_hand, player_turn)
            print(f"\nDEALER TOTAL IS {dealer_total}\n")
            while dealer_total < 17:
                time.sleep(1)
                print("DEALER HITS...\n")
                time.sleep(3)
                self.drawCard(self.dealer_hand, self.deck)
                time.sleep(1)
                self.displayHand(self.dealer_hand, player_turn)
                dealer_total = self.getTotal(self.dealer_hand, player_turn)
                print(f"\nDEALER TOTAL IS {dealer_total}\n")
        else:
            print("IT IS NOT THE DEALERS TURN")

        return dealer_total

    def getTotal(self, hand, player_turn) -> int:
        total = 0

        for card in hand:
            total += self.deck.getRemovedCards().get(card)
            if player_turn and self.player_number_of_aces > 0 and total > 21:
                self.player_number_of_aces -= 1
                total -= 10
            elif (not player_turn) and self.dealer_number_of_aces > 0 and total > 21:
                self.dealer_number_of_aces -= 1
                total -= 10

        return total

    def play(self):
        player_turn = True
        user_choice = ""

        print(f"DEALER SHOWS:\n{self.dealer_hand[0]}\n")
        self.displayHand(self.player_hand, player_turn)
        print()
        player_total = self.getTotal(self.player_hand, player_turn)
        print(f"YOUR TOTAL IS {player_total}\n")

        if player_total != 21:
            self.playerTurn(player_turn, player_total)

        if user_choice == 's':
            print()

        player_turn = False
        dealer_total = self.getTotal(self.dealer_hand, player_turn)

        if player_total <= 21:
            dealer_total = self.dealerTurn(player_turn, dealer_total)

        self.displayWinner(player_total, dealer_total)


BlackJack().play()
