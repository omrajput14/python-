# 299. Bulls and Cows
# You are playing the Bulls and Cows game with your friend.

from collections import Counter

def get_hint(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum((Counter(secret) & Counter(guess)).values()) - bulls
    return f"{bulls}A{cows}B"

if __name__ == "__main__":
    print(get_hint("1807", "7810"))
