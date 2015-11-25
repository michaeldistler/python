import math
import random

deck_card_list = []


class Die(object):
    def __init__(self, side_count):
        self.side_count = side_count

    def roll(self):
        result = random.randint(1, self.side_count)
        return "Player 1 rolled a %d with a %s sided die." % (result, self.side_count)


class Game(object):
    def __init__(self, game_type):
        self.game_type = game_type

    def get_game_type(self):
        return self.game_type


class Planeswalker(object):
    def __init__(self, health=None):
        if health is None:
            self.health = []
        self.health = health
        game_type = get_game_type()

    def set_health(self):
        if game_type is standard:
            self.health = 20
            return "Game type: Standard \n Health: %s" % (self.health)


class Deck(object):
    def __init__(self, name, deck_type, card_count):
        self.name = name
        self.deck_type = deck_type
        self.card_count = card_count

    def add_card(self, card):
        if deck_card_list.count(card) == 4:
            return "%s cannot be added.  There is a 4 card limit of any card in a deck." % (card.name)
        elif deck_card_list.count(card) < 4:
            if deck_card_list.count(card) == 2:
                deck_card_list.append(card)
                return "%s added to %s deck.  You can add %d more %s to the deck." % (card.name, self.name, (4 - deck_card_list.count(card)), card.name)
            elif deck_card_list.count(card) == 3:
                deck_card_list.append(card)
                return "%s added to %s deck.  You can add %d %s's to the deck." % (card.name, self.name, (4 - deck_card_list.count(card)), card.name)
            else:
                deck_card_list.append(card)
                return "%s added to %s deck.  You can add %d more %s's to the deck." % (card.name, self.name, (4 - deck_card_list.count(card)), card.name)

    def remove_card(self, card):
        if card in deck_card_list:
            if deck_card_list.count(card) > 2 or deck_card_list.count(card) == 1:
                deck_card_list.remove(card)
                return "%s removed.  %d %s's remaining." % (card.name, deck_card_list.count(card), card.name)
            elif deck_card_list.count(card) > 1:
                deck_card_list.remove(card)
                return "%s removed.  %d %s remaining." % (card.name, deck_card_list.count(card), card.name)
        else:
            return "%s is not in this deck." % (card.name)


class Card(object):
    def __init__(self, name, card_type, mana_cost,
                 power, toughness, ability=None, tapped=False):
        self.name = name
        self.card_type = card_type
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness
        if ability is None:
            ability = []
        self.ability = ability
        self.tapped = tapped

    def tap(self):
        if not self.tapped:
            self.tapped = True
            return "tapped: " + str(self.tapped)
        else:
            return "The card is already tapped."

    def untap(self):
        if self.tapped:
            self.tapped = False
            return self.tapped
        else:
            return "The card is already untapped."

    def attack(self, defending_creature):
        # Attacking Creature values
        attack_value = self.power
        defense_value = self.toughness

        #Defending Creature(dc) Values
        dc_toughness = defending_creature.toughness
        dc_power = defending_creature.power

        #############################
        # Combat Phase Calculations #
        #############################

        # Tap Card  to attack
        self.tap()

        # If negative, the blocking creature successfully blocked and killed
        # attacking creature.
        # If 0, the blocking creature blocked successfully but died as well.
        attack_value_remaining = attack_value - dc_toughness
        defense_value_remaining = defense_value - dc_power

        if attack_value_remaining <= 0 and defense_value_remaining <= 0:
            return "%s blocked and killed the %s but died as well." % (defending_creature.name, self.name)
        elif attack_value_remaining <= 0:
            if attack_value_remaining < 0 and defense_value_remaining <= 0:
                return "%s successfully blocked and killed %s with %s health points remaining" % (defending_creature.name, self.name, math.fabs(attack_value_remaining))
            elif attack_value_remaining < 0 and defense_value_remaining > 0:
                return "%s successfully blocked %s" % (defending_creature.name, self.name)
        elif attack_value_remaining > 0:
            return "%s has %s points to attack with remaining.  %s died an unfortunate death." % (self.name, attack_value_remaining, defending_creature.name)



        return attack_value_remaining, defense_value_remaining

    def use_ability(self):
        pass


def main():
    card1 = Card("Mahamoti Djinn", "Creature - Djinn", "Water", 2, 2)
    card2 = Card("Scroll Thief", "Creature - Merfolk Rogue", "Water", 6, 2)
    result = card1.attack(card2)
    deck1 = Deck("WhiteBlue", "White/Blue", 60)
    print deck1.add_card(card1)
    print deck1.add_card(card1)

    print deck1.add_card(card2)
    print deck1.add_card(card2)
    print card1.tapped
    print result


if __name__ == "__main__":
    main()
