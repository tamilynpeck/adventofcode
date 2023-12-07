from collections import Counter
from string import ascii_lowercase

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
        high_cards = [hand for hand in self.hands if hand.type == 0]
        one_pairs = [hand for hand in self.hands if hand.type == 1]
        two_pairs = [hand for hand in self.hands if hand.type == 2]
        three_of_a_kind = [hand for hand in self.hands if hand.type == 3]
        full_house = [hand for hand in self.hands if hand.type == 4]
        four_of_a_kind = [hand for hand in self.hands if hand.type == 5]
        five_of_a_kind = [hand for hand in self.hands if hand.type == 6]

        high_cards = sorted(high_cards)
        one_pairs = sorted(one_pairs)
        two_pairs = sorted(two_pairs)
        three_of_a_kind = sorted(three_of_a_kind)
        full_house = sorted(full_house)
        four_of_a_kind = sorted(four_of_a_kind)
        five_of_a_kind = sorted(five_of_a_kind)

        # ranked_hands = sorted(self.hands)
        # rank = 1
        # for hand in ranked_hands:
        #     hand.rank = rank
        #     ranked_hands.append(hand)
        #     rank += 1

        ranked_hands = []
        rank = 1
        for hand in high_cards:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        for hand in one_pairs:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        for hand in two_pairs:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        for hand in three_of_a_kind:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        for hand in full_house:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        for hand in four_of_a_kind:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        for hand in five_of_a_kind:
            hand.rank = rank
            ranked_hands.append(hand)
            rank += 1

        # yikes = [hand for hand in ranked_hands if hand.yikes() > 1]
        # print([(hand.hand, hand.rank) for hand in yikes])

        # print([(hand.hand, hand.rank, hand.compare) for hand in ranked_hands])

        return sum([hand.bid * hand.rank for hand in ranked_hands])

    def solve_part_two(self):
        # self.wild = True
        return self.solve_part_one()


class Hand:
    def __init__(self, hand, bid, wild=False):
        self.hand = hand
        self.compare = [strength[char] for char in hand]
        self.count = Counter(self.hand)
        self.bid = int(bid)
        self.rank = 0
        self.wild = wild
        self.type = None
        if self.five_of_a_kind():
            self.type = 6
        if self.four_of_a_kind():
            if self.type:
                raise Exception("Two types found for", self.hand, self.type, 5)
            self.type = 5
        elif self.full_house():
            if self.type:
                raise Exception("Two types found for", self.hand, self.type, 4)
            self.type = 4
        elif self.three_of_a_kind():
            if self.type:
                raise Exception("Two types found for", self.hand, self.type, 3)
            self.type = 3
        if self.two_pair():
            if self.type:
                raise Exception("Two types found for", self.hand, self.type, 2)
            self.type = 2
        if self.one_pair():
            if self.type:
                raise Exception("Two types found for", self.hand, self.type, 1)
            self.type = 1
        if self.high_card():
            if self.type:
                raise Exception("Two types found for", self.hand, self.type, 0)
            self.type = 0
        if self.type == None:
            raise Exception("No type found for", self.hand)

    def five_of_a_kind(self):
        if self.wild and "J" in self.count.keys():
            print(len(self.count))
            return len(self.count) <= 2
        return 5 in self.count.values()

    def four_of_a_kind(self):
        if self.wild and "J" in self.count.keys():
            j = self.count["J"]
            values = [value for key, value in self.count.items() if key != "J"]
            print(values)
            return any([value + j == 4 for value in values])
        return 4 in self.count.values()

    def full_house(self):
        if self.wild and "J" in self.count.keys():
            counts = [value for key, value in self.count.items() if key != "J"]
            return len(counts) == 2

        return 3 in self.count.values() and 2 in self.count.values()

    def three_of_a_kind(self):
        if self.wild and "J" in self.count.keys():
            j = self.count["J"]
            return any([value + j == 3 for value in self.count.values()])
        return 3 in self.count.values() and 2 not in self.count.values()

    def two_pair(self):
        if self.wild and "J" in self.count.keys():
            return False
        return 2 in self.count.values() and len(self.count) == 3

    def one_pair(self):
        if self.wild and "J" in self.count.keys():
            return len(self.count) == 5
        return 2 in self.count.values() and len(self.count) == 4

    def high_card(self):
        if self.wild and "J" in self.count.keys():
            return False
        return len(self.count) == 5

    def __gt__(self, other):
        # if self.type != other.type:
        #     return self.type > other.type

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
