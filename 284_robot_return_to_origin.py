# 284. Robot Return to Origin
# There is a robot starting at the position (0, 0), the origin, on a 2D plane.

def judge_circle(moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

if __name__ == "__main__":
    print(judge_circle("UD"))  # True
    print(judge_circle("LL"))  # False
