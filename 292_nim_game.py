# 292. Nim Game
# You are playing the following Nim Game with your friend:
# There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.

def can_win_nim(n):
    return n % 4 != 0

if __name__ == "__main__":
    print(can_win_nim(4))
