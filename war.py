import random
from typing import Any

#Deck config
suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

#Card Class
class Card:
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    
    def __str__(self) -> str:

        return self.rank + " of " + self.rank
    

class Deck:
    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits: 
            for rank in ranks: 
                self.all_cards.append(Card(suit,rank))


    def shuffle(self):

        random.shuffle(self.all_cards)


    def deal_one(self):

        return self.all_cards.pop()
    

class Player:
    
    def __init__(self,name) -> None:

        self.name = name

        self.all_cards = []
 
    def remove_one(self):

        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards"
    

# Setting up players 

player_one = Player("Mika")
player_two = Player("Louie")

# Setting up players
new_deck = Deck()
# Shuffle deck
new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0 


while game_on:

    round_num += 1
    print(f"Round {round_num}")


    if len(player_one.all_cards) == 0:
        print(f"{player_one}, out of cards! {player_two} wins!")
        game_on = False
        break

    
    if len(player_two.all_cards) == 0:
        print(f"{player_two}, out of cards! {player_one} wins!")
        game_on = False
        break


    # Start a new round 

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
                         
        else:
            print(f"There's a WAR going on between {player_one} and {player_two}")

            if len(player_one.all_cards) < 5:
                print(f"{player_one} unable to declare war")
                print(f"{player_two} WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print(f"{player_two} unable to declare war")
                print(f"{player_one} WINS!")
                game_on = False
                break

            else:

                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())