import argparse
from collections import deque, Counter
from typing import List, Tuple, TextIO


KINGDOM_OF_SHAN = "SPACE"

KINGDOM_TO_EMBLEM = {
    "space": "gorilla",
    "land": "panda",
    "water": "octopus",
    "ice": "mammoth",
    "air": "owl",
    "fire": "dragon",
}

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def _rotate_left(letters: str, num: int) -> str:
    """
    The function rotates each character in letters num times
    to the left returns the resulting str.

    For example:

        Given a string 'abcdef'

        >>> _rotate_left('abcdef', 3)
        'defabc'

           +---------------------------+
       ... | a | b | c | d | e | f | g | ...
           +---------------------------+
             |   |   |   |   |   |   |
             |   |   |   |   |   |   |
             v   v   v   v   v   v   v
           +---------------------------+
       ... | d | e | f | a | b | c | d | ...
           +---------------------------+

                                               +---+---+---+---+---+---+
                                               | a | b | c | d | e | f |
        +---+---+---+---+---+---+---+          +---+---+---+-+-+-+-+-+-+
    ... | a | b | c | d | e | f | g | ...                    |   |   |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+            +-----------+   |   |
          |   |   |   |   |   |   |              |   +-----------+   |
          |   |   |   |   |   |   |              |   |   +-----------+
          v   v   v   v   v   v   v              |   |   |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+            |   |   |
    ... | d | e | f | a | b | c | d | ...        |   |   |
        +---+---+---+---+---+---+---+          +-+-+-+-+-+-+---+---+---+
                                               | a | b | c | d | e | f |
                                               +---+---+---+---+---+---+

           +---+---+---+---+---+---+
           | a | b | c | d | e | f |
           +---+---+---+-+-+-+-+-+-+
                         |   |   |
             +-----------+   |   |
             |   +-----------+   |
             |   |   +-----------+
             |   |   |
             |   |   |
             |   |   |
           +-+-+-+-+-+-+---+---+---+
           | a | b | c | d | e | f |
           +---+---+---+---+---+---+




    """
    letterings = deque(letters)
    letterings.rotate(-num)
    return "".join(letterings)


def decrypt(msg: str, kingdom: str) -> str:
    """Decrypt the msg using the kingdom's emblem length as key
    and returns the resulting str.

    The function joins each character retrieved from the mapping
    created using rotated_letters -> letters and returns the final str.
    The rotated_letters is created depeding on the length of the kingdom emblem.

    For example:
        Say kingdom 'Air' has embelm 'owl'. Now the letters are to be rotated left 3 times,
        since there are 3 characters in the string 'Air'.
    """
    num = len(KINGDOM_TO_EMBLEM[kingdom.lower()])
    rotated_letters = _rotate_left(LETTERS, num)
    letter_map = dict(zip(rotated_letters, LETTERS))
    return "".join(letter_map.get(c.lower(), "") for c in msg.lower())


def is_ally(kingdom: str, msg: str) -> bool:
    """Return true if the decrypted message contains the minimum character count
    from that of the emblem letters.

    For example:

        decrypted_msg = 'olwl'
        emblem        = 'owl'

        Then, this satifies the minimum count.
        ...
    """
    decrypted_msg = decrypt(msg, kingdom)
    emblem = KINGDOM_TO_EMBLEM[kingdom.lower()]

    emblem_letter_count = Counter(emblem)
    decrypted_msg_letter_count = Counter(decrypted_msg)

    return all(
        value <= decrypted_msg_letter_count[key]
        for key, value in emblem_letter_count.items()
    )


def get_allies(input_data: List[Tuple[str, str]]) -> List[str]:
    """Get the ally names by decrypting the messages from the input_data
    and returns the list of allies found.
    """
    allies = []
    for kingdom, msg in input_data:
        if is_ally(kingdom, msg):
            allies.append(kingdom)
    return allies


def _load_from(stream: TextIO) -> List[Tuple[str, str]]:
    data = []
    for line in stream:
        line = line.rstrip()
        if line:
            kingdom, _, msg = line.partition(" ")
            kingdom = kingdom.strip()
            msg = msg.strip()
            data.append((kingdom, msg))
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType("r"))
    args = parser.parse_args()
    with args.infile as file:
        data = _load_from(file)
    allies = get_allies(data)

    num_of_allies = len(allies)
    if num_of_allies >= 3:
        output = " ".join(
            [KINGDOM_OF_SHAN] + allies
        ).upper()  # .upper() incase the ally name was in lower
        print(output)
    else:
        print("NONE")


if __name__ == "__main__":
    main()

