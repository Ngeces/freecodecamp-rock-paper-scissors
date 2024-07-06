# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
# idea from https://github.com/Captainspockears/freecodecampMLprojects/blob/master/RockPaperScissor/RPS.py but optimized into only 2 guesses
from RPS_game import play, mrugesh, abbey, quincy, kris
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}


def player(prev_play, player_history=[], opponent_history=[]):
    opponent_history.append(prev_play)
    guess = 'P'
    if(len(player_history) == 1000) :
        opponent_history.clear()
        opponent_history.append(prev_play)
        player_history.clear()


    if len(player_history) < 3:
        player_history.append('P')
        return 'P'
    
    enemy = "".join(opponent_history[1:3])


    if enemy == 'RP':
        guess = defeat_quency(len(player_history))

    if enemy == 'PP':
        guess = defeat_abbey(player_history)

    if enemy == 'PS':
        guess = defeat_kris(player_history)
    if enemy == 'RR':
        guess = defeat_mrugesh(player_history)

    player_history.append(guess)
    return guess


def defeat_quency(panjang):
    choices = ["R", "R", "P", "P", "S"]
    next_move = choices[(panjang + 1)% len(choices)]
    guess = ideal_response[next_move]
    return guess

def defeat_mrugesh(player_history=[]):
    last_ten = player_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    next_move = ideal_response[most_frequent]
    return ideal_response[next_move]
 

def defeat_kris(player_history=[]):
    next_move = ideal_response[player_history[-1]]
    return ideal_response[next_move]

def defeat_abbey(player_history=[]):
        play_order = [{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0, }]

        player_full_history = player_history
        player_full_history[0] = 'R'
        prev_opponent_play = player_full_history[-1]
        last_two = "".join(player_history[-2:])
        for i in range(len(player_full_history) - 1):
            last_two = "".join(player_full_history[i:i + 2])
            play_order[0][last_two] += 1
        
        potential_plays = [
            prev_opponent_play + "R",
            prev_opponent_play + "P",
            prev_opponent_play + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]
        return ideal_response[ideal_response[prediction]]