def generate(numRows):
    res = [[1]]
    for i in range(1, numRows):
        temp1 = res[-1] + [0]
        temp2 = [0] + res[-1]
        res.append([temp1[i]+temp2[i] for i in range(len(temp1))])
    return res

if __name__ == "__main__":
    print(generate(5))