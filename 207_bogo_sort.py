import random

def is_sorted(data):
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def bogo_sort(data):
    while not is_sorted(data):
        random.shuffle(data)
    return data

if __name__ == "__main__":
    print(bogo_sort([3,1,2]))