""" Lib providing basic APIs """
import re
from enum import IntEnum
from os.path import dirname, join

InputFileList = [
    "./input_sample_1.txt",
    "./input_sample_2.txt",
    "./input.txt",
]

card_dict ={
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14,
}

card_dict_with_joker = {
    'J' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    "Q" : 11,
    "K" : 12,
    "A" : 13,
}

class InputLoc(IntEnum):
    """ Enum to select input file """
    SAMPLE_INPUT_1 = 0
    SAMPLE_INPUT_2 = 1
    ORIGINAL_INPUT = 2

class HandType(IntEnum):
    """ Enum for hand type """
    UNKNOW_TYPE = 0
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

class Hand():
    """ Data structure to represet a hand """
    cards = []
    hand_type = HandType.UNKNOW_TYPE
    bid = 0

    def __init__(self, card_list = None,
                 bid = 0, hand_type = HandType.UNKNOW_TYPE):
        self.cards = card_list
        self.bid = bid
        self.hand_type = hand_type

class Day7lib():
    """ Base class for Day 7 puzzle """
    max_row = 0
    max_column = 0
    hands = None
    hand_regex = r'(^[A|K|Q|J|T|\d]+) (\d+)'
    hand_type_to_rank_map = {}

    def __init__( self ):
        self.hand_pattern = re.compile(self.hand_regex)
        self.hands = {}

    def read_file_content( self, input_type ):
        """ Open input file and return its content """
        current_dir = dirname( __file__ )
        input_file_path = join( current_dir, InputFileList[input_type] )

        with open(input_file_path, "r+", encoding="utf8") as input_file:
            lines = input_file.readlines()
        input_file.close()

        self.max_row = len(lines)
        self.max_column = len(lines[0]) - 1
        return lines

    def find_hand_type(self, card_list):
        """ Return the type of the hand """
        hand_type = HandType.UNKNOW_TYPE

        set_len = len(set( card_list ))
        if set_len == 5:
            hand_type = HandType.HIGH_CARD
        elif set_len == 4:
            hand_type = HandType.ONE_PAIR
        elif set_len == 3:
            # Two possibilities (3+1+1) or (2+2+1)
            for card in card_list:
                if card_list.count(card) == 3:
                    hand_type = HandType.THREE_OF_A_KIND
                    break
                hand_type = HandType.TWO_PAIR
        elif set_len == 2:
            # Two possibilities (4+1) or (3+2)
            first_card_count = card_list.count(card_list[0])
            if first_card_count in (4,1):
                hand_type = HandType.FOUR_OF_A_KIND
            else:
                hand_type = HandType.FULL_HOUSE
        else:
            hand_type = HandType.FIVE_OF_A_KIND
        return hand_type

    def find_hand_type_with_joker(self, card_list):
        """ Return the type of the hand, after substituing Joker """
        hand_type = self.find_hand_type(card_list)
        joker_count = card_list.count('J')

        if joker_count:
            # In One Pair, there can be only one joker
            if hand_type == HandType.HIGH_CARD:
                hand_type = HandType.ONE_PAIR

            elif hand_type == HandType.ONE_PAIR:
                # If pair is Joker, it becomes 3
                # If pair is not Joker, joker can be 1 and it still becomes 3
                hand_type = HandType.THREE_OF_A_KIND

            elif hand_type == HandType.TWO_PAIR:
                # If neither pair is a joker, it becomes full house (3+2)
                # If any pair is a Joker, it becomes FOUR of a kind
                if joker_count == 1:
                    hand_type = HandType.FULL_HOUSE
                elif joker_count == 2:
                    hand_type = HandType.FOUR_OF_A_KIND

            elif hand_type == HandType.THREE_OF_A_KIND:
                # If joker is the three, hand becomes four of a kind
                # If joker is not three, hand still becomes 4 or a kind
                hand_type = HandType.FOUR_OF_A_KIND

            elif hand_type in {HandType.FULL_HOUSE,
                               HandType.FOUR_OF_A_KIND,
                               HandType.FIVE_OF_A_KIND}:
                # No comments needed
                hand_type = HandType.FIVE_OF_A_KIND

        # For debugging
        #print(f"For hand {card_list} type is {hand_type.name} ")
        return hand_type

    def update_map(self, hand_type):
        """ Update map of hand type to its rank """
        if not bool(self.hand_type_to_rank_map):
            self.hand_type_to_rank_map[hand_type] = 1
        else:
            for hand_type_old in sorted(self.hand_type_to_rank_map):
                if hand_type_old > hand_type:
                    self.hand_type_to_rank_map[hand_type_old] += 1
                else:
                    valid_rank = self.hand_type_to_rank_map[hand_type_old] + 1
            self.hand_type_to_rank_map[hand_type] = valid_rank

    def populate_hand_details(self, content, joker=False):
        """ Populate hand details from the input file """
        for line in content:
            hand_match = self.hand_pattern.findall(line)
            card_list = [*hand_match[0][0]]
            bid = int(hand_match[0][1])
            if not joker:
                hand_type = self.find_hand_type(card_list)
            else:
                hand_type = self.find_hand_type_with_joker(card_list)
            hand = Hand(card_list, bid, hand_type)

            # Group
            if hand_type not in self.hands:
                self.update_map(hand_type)
                self.hands.update({hand_type:[]})
                self.hands[hand_type].append(hand)
            else:
                self.hands[hand_type].append(hand)

    def card_compare(self, hand1, hand2):
        """ Compare which is best hand """
        for (i,j) in zip(hand1.cards, hand2.cards):
            if card_dict[i] < card_dict[j]:
                return -1
            if card_dict[i] > card_dict[j]:
                return 1
        return 0

    def card_compare_with_joker(self, hand1, hand2):
        """ Compare which is best hand """
        for (i,j) in zip(hand1.cards, hand2.cards):
            if card_dict_with_joker[i] < card_dict_with_joker[j]:
                return -1
            if card_dict_with_joker[i] > card_dict_with_joker[j]:
                return 1
        return 0
