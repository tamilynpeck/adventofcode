from collections import Counter


class Day7:
    def __init__(self, data, wild=False):
        self.data = data
        self.strength = "23456789TJQKA"
        self.wild = wild

    def build_hands(self):
        self.hands = []
        for line in self.data:
            hand, bid = line.split(" ")
            self.hands.append(Hand(hand, bid, wild=self.wild, strength=self.strength))

    def solve_part_one(self):
        self.build_hands()
        ranked_hands = sorted(self.hands)

        rank = 1
        for hand in ranked_hands:
            hand.rank = rank
            print(hand.hand, hand.type_strength, hand.rank, hand.bid)
            rank += 1

        return sum([hand.bid * hand.rank for hand in ranked_hands])

    def solve_part_two(self):
        self.strength = "J23456789TQKA"
        self.wild = True
        self.build_hands()
        return self.solve_part_one()


class Hand:
    def __init__(self, hand, bid, strength="23456789TJQKA", wild=False):
        self.hand = hand
        self.bid = int(bid)
        self.rank = 0

        self.compare = [strength.index(char) for char in hand]
        self.count = Counter(self.hand)
        self.wild = wild
        self.type_strength = self.get_strength()

    def get_strength(self):
        if self.wild and "J" in self.count and self.count["J"] == 5:
            return 4
        if self.wild and "J" in self.count:
            counts = self.count.copy()
            j = counts.pop("J")
            return max(counts.values()) + j - (len(set(self.hand)) - 1)
        return max(self.count.values()) - len(set(self.hand))

    def __gt__(self, other):
        if self.type_strength != other.type_strength:
            return self.type_strength > other.type_strength

        if self.compare[0] != other.compare[0]:
            return self.compare[0] > other.compare[0]
        if self.compare[1] != other.compare[1]:
            return self.compare[1] > other.compare[1]
        if self.compare[2] != other.compare[2]:
            return self.compare[2] > other.compare[2]
        if self.compare[3] != other.compare[3]:
            return self.compare[3] > other.compare[3]
        if self.compare[4] != other.compare[4]:
            return self.compare[4] > other.compare[4]
