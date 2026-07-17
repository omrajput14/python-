# 273. Distribute Candies
# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

def distribute_candies(candyType):
    return min(len(candyType) // 2, len(set(candyType)))

if __name__ == "__main__":
    print(distribute_candies([1,1,2,2,3,3]))  # 3
    print(distribute_candies([1,1,2,3]))      # 2
