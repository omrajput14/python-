# 294. Flip Game II
# You are playing a Flip Game with your friend.
# Determine if the starting player can guarantee a win.

def can_win(currentState):
    memo = {}
    def dfs(state):
        if state in memo: return memo[state]
        for i in range(len(state) - 1):
            if state[i:i+2] == "++":
                next_state = state[:i] + "--" + state[i+2:]
                if not dfs(next_state):
                    memo[state] = True
                    return True
        memo[state] = False
        return False
    return dfs(currentState)

if __name__ == "__main__":
    print(can_win("++++"))
