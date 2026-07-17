# 277. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not.

def can_place_flowers(flowerbed, n):
    count = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
    return count >= n

if __name__ == "__main__":
    print(can_place_flowers([1,0,0,0,1], 1))  # True
    print(can_place_flowers([1,0,0,0,1], 2))  # False
