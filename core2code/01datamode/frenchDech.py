import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    from random import choice

    # beer_card = Card('7', 'diamonds')
    # print(beer_card)
    deck = FrenchDeck()
    # print(deck)
    # print(len(deck))
    # print(deck.suits)
    # print(deck._cards)
    # print(deck[0], deck[1], deck[-1])
    # print(choice(deck))
    # print(choice(deck))
    # print(choice(deck))
    # print(deck[:3])
    # print(deck[12::13])
    # print(Card('Q', 'hearts') in deck)
    # print(Card('7', 'beasts') in deck)  # 迭代通常是隐式的，譬如说一个集合类型没有实现__contains__ 方法，那么in 运算符就会按顺序做一次迭代搜索
    for card in sorted(deck, key=spades_high):
        print(card)
        slice