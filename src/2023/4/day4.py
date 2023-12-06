class Scratchcards:
    def __init__(self, data):
        self.cards = data

    def get_card_total(self):
        card_totals = []
        for card in self.cards:
            _, card_data = card.split(":")
            card_total = self.get_card_value(card_data)
            if card_total == 0:
                continue
            compute = 1 if card_total == 1 else 2 ** (card_total - 1)
            card_totals.append(compute)

        return sum(card_totals)

    @staticmethod
    def get_card_value(card):
        winning, scratchcard = card.split("|")
        winning = winning.strip().split(" ")
        scratchcard = scratchcard.replace("  ", " ")
        scratchcard = scratchcard.strip().split(" ")
        matches = [value for value in scratchcard if value in winning]
        return len(matches)

    def get_total_scratchcards(self):
        cards = [Card.parse_card(card) for card in self.cards]
        for card in cards:
            if not card.matches:
                continue

            copies_to_add = card.copies
            for i, _ in enumerate(card.matches):
                next_card = cards[card.card_id + i]
                next_card.add_copy(copies_to_add)

        return sum([card.copies for card in cards])


class Card:
    def __init__(self, card_id, winning_numbers, your_numbers, matches):
        self.card_id = card_id
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers
        self.matches = matches
        self.copies = 1

    def parse_card(card_data):
        card_data = card_data.replace("   ", " ")
        card_data = card_data.replace("  ", " ")
        card_id, card_numbers = card_data.split(":")
        card_id = int(card_id.split(" ")[1])
        winning_numbers, your_numbers = card_numbers.split("|")
        winning_numbers = winning_numbers.strip().split(" ")
        your_numbers = your_numbers.replace("  ", " ")
        your_numbers = your_numbers.strip().split(" ")
        matches = [value for value in your_numbers if value in winning_numbers]
        return Card(card_id, winning_numbers, your_numbers, matches)

    def add_copy(self, number_of_copies):
        self.copies += number_of_copies
