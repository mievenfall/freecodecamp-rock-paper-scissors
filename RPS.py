# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

counter = {'R': 'P', 'P': 'S', 'S': 'R'}
moves = {}

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    hist = opponent_history

    guess = 'R'

    n = 6
    
    if len(hist) > n:
        sequence = "".join(hist[-n:])

        moves["".join(hist[-(n+1):])] = moves.get("".join(hist[-(n+1):]), 0) + 1

        possibilities = [sequence+"R", sequence+"P", sequence+"S"]

        sub_moves = { k: moves[k] for k in possibilities if k in moves.keys()}


        if sub_moves:
            predict = max(sub_moves, key=sub_moves.get)
            guess = predict[-1]

    return counter[guess]
