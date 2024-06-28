# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import play, mrugesh, abbey, quincy, kris

def player(prev_play, player_history=[], opponent_history=[], play_order = [{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0, }]):
    opponent_history.append(prev_play)
    guess = 'P'
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    if(len(player_history) == 1000) :
        opponent_history.clear()
        opponent_history.append(prev_play)
        player_history.clear()


    if len(player_history) < 4:
        player_history.append('P')
        return 'P'
    
    enemy = "".join(opponent_history[1:4])
    if enemy == 'RPP':
      choices = ["R", "R", "P", "P", "S"]
      next_move = choices[(len(player_history) + 1)% len(choices)]
      guess = ideal_response[next_move]

    if enemy == 'PPS':
        last_two = "".join(player_history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1

        potential_plays = [
            player_history[-1] + "R",
            player_history[-1] + "P",
            player_history[-1] + "S",
        ]

        sub_order = {
          k: play_order[0][k]
          for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]

        next_move = ideal_response[prediction]
        guess = ideal_response[next_move]

    if enemy == 'PSS':
        next_move = ideal_response[player_history[-1]]
        guess = ideal_response[next_move]

    if enemy == 'RRS':
        last_ten = player_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)

        if most_frequent == '':
            most_frequent = "S"

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        next_move = ideal_response[most_frequent]
        guess = ideal_response[next_move]

    player_history.append(guess)
    return guess


    

