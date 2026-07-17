# 288. Baseball Game
# You are keeping the scores for a baseball game with strange rules.

def cal_points(operations):
    stack = []
    for op in operations:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)

if __name__ == "__main__":
    print(cal_points(["5","2","C","D","+"]))  # 30
    print(cal_points(["5","-2","4","C","D","9","+","+"]))  # 27
