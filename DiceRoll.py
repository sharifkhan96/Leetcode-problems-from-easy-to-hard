
'''
# a simpleer version of this dice rolling game
import random

# loop
while True:

    # take input from the user dice the roll? y/n
    input1 = input("Would you like to dice the roll? Y/N ").lower()

    # if yes:
    if input1 == "y":
        random1 = random.randint(1, 10)
        random2 = random.randint(1, 10)

        # print the dice
        print(f' ({random1}, {random2}) ')

    # if no
    elif input1 == "n":
        # thank u
        print("Thank you for playing..")
        break
    # else invalid value
    else:
        print("Invalid option!!")
---------------------------------------------------------------------
'''

from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Optional, Tuple, List, Dict


@dataclass(frozen=True)
class Dice:
    sides: int = 10

    def roll(self, rng: random.Random) -> int:
        if self.sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        return rng.randint(1, self.sides)


@dataclass
class GameStats:
    sides: int
    history: List[Tuple[int, int]] = field(default_factory=list)

    freq_die1: Dict[int, int] = field(init=False)
    freq_die2: Dict[int, int] = field(init=False)
    freq_all: Dict[int, int] = field(init=False)

    def __post_init__(self) -> None:
        self.freq_die1 = {face: 0 for face in range(1, self.sides + 1)}
        self.freq_die2 = {face: 0 for face in range(1, self.sides + 1)}
        self.freq_all = {face: 0 for face in range(1, self.sides + 1)}

    def record(self, d1: int, d2: int) -> None:
        self.history.append((d1, d2))
        self.freq_die1[d1] += 1
        self.freq_die2[d2] += 1
        self.freq_all[d1] += 1
        self.freq_all[d2] += 1

    @property
    def total_rolls(self) -> int:
        return len(self.history)

    @property
    def total_faces_observed(self) -> int:
        return self.total_rolls * 2


def prompt_yes_no(prompt: str = "Would you like to roll the dice? [y/n] ") -> Optional[bool]:
    answer = input(prompt).strip().lower()
    if answer in {"y", "yes"}:
        return True
    if answer in {"n", "no"}:
        return False
    return None


def roll_two_dice(die: Dice, rng: random.Random) -> Tuple[int, int]:
    return die.roll(rng), die.roll(rng)


def play_game(sides: int) -> None:
    rng = random.Random()
    die = Dice(sides=sides)
    stats = GameStats(sides=sides)

    print(f"🎲 Dice Roller | Two dice | {sides}-sided")
    print("Type 'y' to roll, 'n' to quit.\n")

    while True:
        choice = prompt_yes_no()

        if choice is None:
            print("Enter a valid option. Please type 'y' or 'n'.\n")
            continue

        if choice is False:
            print(f"\nTotal rolls: {stats.total_rolls}")
            print("Thanks for playing 👋")
            return

        d1, d2 = roll_two_dice(die, rng)
        stats.record(d1, d2)
        print(f"Result: ({d1}, {d2})\n")


def main() -> None:
    play_game(sides=10)


if __name__ == "__main__":
    main()
