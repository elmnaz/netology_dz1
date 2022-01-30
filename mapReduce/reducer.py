import sys

suit_count = 0
previouse_suit = None

for line in sys.stdin:
    suit = line.strip()
    if previouse_suit:
        if previouse_suit == suit:
            suit_count += 1
        else:
            print (previouse_suit, suit_count)
            previouse_suit = suit
            suit_count = 1
    else:
        previouse_suit = suit
        suit_count = 1

(previouse_suit, suit_count)