
from db import player_db
from typing import List, Tuple

def get_playername(player: Tuple[str, str, int,int,List[str]]) -> str:
    return  player[0]


def get_teams(player: Tuple[str, str, int, List[str]]) -> str:
    return player[1]


def get_start_year(player: Tuple[str, str, int, List[str]]) -> int:
    return player[2]


def get_end_year(player: Tuple[str, str, int, List[str]]) -> int:
    return player[3]


def get_stats(player: Tuple[str, str, int, List[str]]) -> List[str]:
    return player[4]


# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def name_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    # ["1974"]
    year = int(matches[0])
    result = []
    for player in player_db:
        if get_start_year(player) <= year <= get_end_year(player):
            result.append(get_playername(player))
    return result

