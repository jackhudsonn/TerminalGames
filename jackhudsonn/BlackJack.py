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
        self.player_hand = []

        self.drawCard(self.dealer_hand, self.deck)
        self.drawCard(self.dealer_hand, self.deck)

        self.drawCard(self.player_hand, self.deck)
        self.drawCard(self.player_hand, self.deck)

    def drawCard(self, hand, deck) -> str:
        card = random.choice(list(self.deck.getCards()))
        hand.append(card)
        deck.remove(card)

        return card

    def displayHand(self, player_turn, player_total: str, dealer_total: str) -> None:
        print("PLAYER CARDS:                 DEALER CARDS:")
        for i in range(max(len(self.player_hand), len(self.dealer_hand))):
            if (player_turn and i != 0) or i >= len(self.dealer_hand):
                print(self.player_hand[i])
            elif i >= len(self.player_hand):
                print(' ' * 30 + self.dealer_hand[i])
            else:
                print(self.player_hand[i] + (' ' * (30 - len(self.player_hand[i]))) + self.dealer_hand[i])

        print()
        print(f"PLAYER TOTAL IS {player_total}", end='')
        if len(player_total) == 1:
            print(" ", end='')
        print(f"{' ' * 12}DEALER TOTAL IS {dealer_total}")

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
        hit_or_stand = input().lower()
        while hit_or_stand != 'h' and hit_or_stand != 's':
            print("PLEASE ENTER AN 'h' OR AN 's':")
            hit_or_stand = input()
        return hit_or_stand

    def playerTurn(self, player_turn, player_total, dealer_total) -> int:
        if player_turn:
            wait(2)
            print()
            user_choice = self.hitOrStand()
            while user_choice == 'h' and player_total < 21:
                switchScreen()
                print("           JACKHUDSONN BLACKJACK")
                print("           ---------------------")
                self.drawCard(self.player_hand, self.deck)
                player_total = self.getTotal(self.player_hand)
                self.displayHand(player_turn, str(player_total), dealer_total)
                print()
                if player_total < 21:
                    user_choice = self.hitOrStand()
        else:
            print("IT IS NOT THE PLAYER'S TURN")

        return player_total

    def dealerTurn(self, player_turn, player_total, dealer_total) -> int:
        if not player_turn:
            print("           JACKHUDSONN BLACKJACK")
            print("           ---------------------")
            self.displayHand(player_turn, str(player_total), str(dealer_total))
            while dealer_total < 17:
                time.sleep(1)
                print("DEALER HITS...\n")
                time.sleep(3)
                self.drawCard(self.dealer_hand, self.deck)
                time.sleep(1)
                switchScreen()
                print("           JACKHUDSONN BLACKJACK")
                print("           ---------------------")
                dealer_total = self.getTotal(self.dealer_hand)
                self.displayHand(player_turn, str(player_total), str(dealer_total))
        else:
            print("IT IS NOT THE DEALERS TURN")

        return dealer_total

    def getTotal(self, hand) -> int:
        total = 0
        num_aces = 0

        for card in hand:
            total += self.deck.getRemovedCards().get(card)

            if self.deck.getRemovedCards().get(card) == 11:
                num_aces += 1

            if num_aces > 0 and total > 21:
                num_aces -= 1
                total -= 10

        return total

    def play(self):
        player_turn = True
        user_choice = ""

        print("           JACKHUDSONN BLACKJACK")
        print("           ---------------------")

        player_total = self.getTotal(self.player_hand)
        dealer_total = '?'

        self.displayHand(player_turn, str(player_total), dealer_total)

        if player_total != 21:
            player_total = self.playerTurn(player_turn, player_total, dealer_total)
            if player_total > 21:
                print("PLAYER BUST, DEALER WINS!")
                return

        switchScreen()

        if user_choice == 's':
            print()

        player_turn = False
        dealer_total = self.getTotal(self.dealer_hand)

        if player_total <= 21:
            dealer_total = self.dealerTurn(player_turn, player_total, dealer_total)

        self.displayWinner(player_total, dealer_total)


BlackJack().play()
