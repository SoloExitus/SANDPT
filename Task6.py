class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def is_correct(strategy:list[str]) -> bool:
    if not len(strategy) == 2:
        return False

    if strategy[1] in ['P', 'S', 'R']:
        return True

    return False

RPS = {}
RPS[('R','R')] = True
RPS[('R','S')] = True
RPS[('R','P')] = False
RPS[('S','S')] = True
RPS[('S','P')] = True
RPS[('S','R')] = False
RPS[('P','P')] = True
RPS[('P','R')] = True
RPS[('P','S')] = False

def rps_game_winner(players):
    if len(players) > 2:
        raise WrongNumberOfPlayersError("More then 2 players")

    for player in players:
         if not is_correct(player):
             raise NoSuchStrategyError(player)

    player1 = players[0]
    player2 = players[1]

    if RPS[(player1[1], player2[1])]:
        return player1
    return player2

#rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])  # = > WrongNumberOfPlayersError
#rps_game_winner([['player1', 'P'], ['player2', 'A']])  # = > NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # = > 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  # = > 'player1 P'