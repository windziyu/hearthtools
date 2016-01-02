from data.my_collection import cards as my_col
# from data.nastya_collection import cards as my_col
from dataobjects.collection import Collection
from dataobjects.deck import Deck
from dataobjects import constants

my_col_object = Collection()
my_col_object.cards = my_col

player_class = raw_input('Input your class: ')
start_card = my_col_object.get_closest_name(raw_input('First card in deck? '))
is_arena_deck = raw_input('Type y if it is arena deck') == 'y'

deck = Deck(my_col=my_col)
deck.add_card(start_card)
deck.player_class = player_class
if is_arena_deck:
    deck.type = constants.ARENA_DECK

while sum(deck.cards.values()) < 30:
    next_card, card_syn_value = deck.get_advice()
    print 'Adding %s : %f' % (next_card, card_syn_value)
    deck.add_card(next_card)

if raw_input("Refine? (y/n)") == 'y':
    deck.refine_deck()

print('Final deck:')
for card in deck.cards:
    print "%s : %d" % (card, deck.cards[card])
