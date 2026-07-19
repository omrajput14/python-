# 293. Flip Game
# You are playing a Flip Game with your friend.
# You are allowed to replace two consecutive '++' with '--'.

def generate_possible_next_moves(currentState):
    return [currentState[:i] + "--" + currentState[i+2:] for i in range(len(currentState) - 1) if currentState[i:i+2] == "++"]

if __name__ == "__main__":
    print(generate_possible_next_moves("++++"))
