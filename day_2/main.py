WIN_BONUS = 6
TIE_BONUS = 3


def parse_strategy(my_input):
    total_score = 0
    replace_strat = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    for line in iter(my_input.splitlines()):
        if len(line.strip()) > 0:
            opponent, me = line.strip().split(" ")

            me_score = replace_strat.get(me, 0)
            opponent_score = replace_strat.get(opponent, 0)

            # Determine the game_bonus
            game_bonus = (
                WIN_BONUS + me_score
                if me_score - opponent_score == 1 or me_score - opponent_score == -2
                else int((me_score - opponent_score) == 0) * TIE_BONUS + me_score
            )

            total_score += game_bonus

    print(f"Your total score: {total_score}")


if __name__ == "__main__":
    my_strategy = """
    A Y
    B X
    C Z
    """

    parse_strategy(my_strategy)
