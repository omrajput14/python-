def bell_number(n):
    bell = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bell[0][0] = 1
    
    for i in range(1, n + 1):
        # Explicitly filling for j = 0
        bell[i][0] = bell[i - 1][i - 1]
        
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
            
    return bell[n][0]

if __name__ == '__main__':
    for n in range(6):
        print(f"Bell Number {n} is {bell_number(n)}")
