import random

cards=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"] * 4
random.shuffle(cards)
Blackjack=False
player_choice=None

def win(player_hand, dealer_hand):
    pass

def calculate_hand_value(hand):
    value=0
    aces=0
    for card in hand:
        if card in (2,3,4,5,6,7,8,9,10):
            value+=card
        elif card in ("J","Q","K"):
            value+=10
        else:
            value+=11
            aces+=1
    while value>21 and aces>0:
        value-=10
        aces-=1
    return value


player_hand=[cards.pop(), cards.pop()]
dealer_hand=[cards.pop(), cards.pop()]

print(f"diiler näitab {dealer_hand[0]} ({dealer_hand})")
print(f"sul on {player_hand[0]} ja {player_hand[1]}")

while player_choice != "s" or Blackjack==True:
    if calculate_hand_value(player_hand)==21:
        print("Blackjack")
        Blackjack=True
        break
    player_choice=input("(h)it või (s)tand: ")
    if player_choice=="h":
        player_hand.append(cards.pop())
        print(f"tõmbasid {player_hand[-1]}")
        print(player_hand)
        if calculate_hand_value(player_hand)>21:
            print("põlesid läbi")
            break
        elif calculate_hand_value(player_hand)==21:
            print("Blackjack")
            break
        else:
            continue
    else:
        break

while calculate_hand_value(dealer_hand)<17:
    if calculate_hand_value(dealer_hand)==21:
        print("diiwleril on blackjack")
    elif calculate_hand_value(dealer_hand)<17:
        dealer_hand.append(cards.pop())
        print(f"dealer tõmabs {dealer_hand[-1]}")
        print(dealer_hand)
        if calculate_hand_value(dealer_hand)>21:
            print("diiler põles läbi")
    else:
        print(dealer_hand)
