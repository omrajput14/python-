class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(W, arr):
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)
    
    final_val = 0.0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            final_val += item.value
        else:
            final_val += item.value * W / item.weight
            break
            
    return final_val

if __name__ == '__main__':
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_val = fractional_knapsack(W, arr)
    print(f"Maximum value we can obtain = {max_val}")
