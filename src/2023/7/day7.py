from collections import Counter

strength = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


class Day7:
    def __init__(self, data, wild=False):
        self.data = data
        self.hands = []
        for line in self.data:
            hand, bid = line.split(" ")
            self.hands.append(Hand(hand, bid, wild=wild))
        self.wild = wild

    def solve_part_one(self):
        ranked_hands = sorted(self.hands)
        # print([(hand.hand, hand.type_strength) for hand in ranked_hands])

        rank = 1
        for hand in ranked_hands:
            hand.rank = rank
            print(hand.hand, hand.type_strength, hand.rank)
            rank += 1

        return sum([hand.bid * hand.rank for hand in ranked_hands])

    def solve_part_two(self):
        return self.solve_part_one()


class Hand:
    def __init__(self, hand, bid, wild=False):
        self.hand = hand
        self.compare = [strength[char] for char in hand]
        self.count = Counter(self.hand)
        self.bid = int(bid)
        self.rank = 0
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
